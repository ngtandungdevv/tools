import openai
import anthropic
import os
import re
import requests
import base64
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class QuestionType(Enum):
    LISTENING = "listening"
    READING = "reading" 
    GRAMMAR = "grammar"
    VOCABULARY = "vocabulary"
    MATCHING = "matching"
    ORDERING = "ordering"
    FILL_BLANK = "fill_blank"
    SPEAKING = "speaking"
    WRITING = "writing"

@dataclass
class IOEQuestion:
    id: str
    type: QuestionType
    content: str
    options: List[str]
    image_url: Optional[str] = None
    audio_url: Optional[str] = None
    context: str = ""

class IOEMasterAI:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        self.anthropic_client = anthropic.Anthropic(api_key=anthropic_key) if anthropic_key else None
        self.groq_api = os.getenv("GROQ_API_KEY")
        
        # Context đặc thù IOE để đạt 99% accuracy
        self.ioe_context = """
You are IOE-GPT, the world's leading expert in Vietnamese English Olympiad (IOE) examinations.
ABSOLUTE RULES for 99% accuracy:
1. Analyze grammar structures meticulously (tenses, voices, conditionals, clauses)
2. For vocabulary: prioritize collocations and phrasal verbs over direct translation
3. For reading: identify topic sentences, transition words, and inference patterns
4. For listening: focus on intonation cues and paraphrased answers, not word-for-word matching
5. For ordering: look for chronological markers (first, then, finally) and logical flow (problem-solution, cause-effect)
6. Never guess - provide linguistic evidence for every choice
7. IOE often uses British English preferences (present perfect with just/already/yet, "at weekends")
8. Distractors analysis: eliminate options with absolute words (always, never, all) unless 100% certain
"""
        
    def analyze_question(self, question_data: Dict) -> IOEQuestion:
        q_type = self._classify_type(question_data)
        
        return IOEQuestion(
            id=str(question_data.get('id', '0')),
            type=q_type,
            content=question_data.get('content', ''),
            options=question_data.get('options', []),
            image_url=question_data.get('image'),
            audio_url=question_data.get('audio')
        )
    
    def _classify_type(self, q: Dict) -> QuestionType:
        content = str(q.get('content', '')).lower()
        q_type = q.get('type', 1)
        
        type_map = {
            1: QuestionType.GRAMMAR,
            2: QuestionType.FILL_BLANK,
            3: QuestionType.ORDERING,
            5: QuestionType.MATCHING,
            7: QuestionType.MATCHING,
            8: QuestionType.FILL_BLANK,
            10: QuestionType.GRAMMAR,
        }
        
        if 'listen' in content or q.get('hasAudio') or q.get('audio'):
            return QuestionType.LISTENING
        if len(str(q.get('content', ''))) > 300 or 'read' in content:
            return QuestionType.READING
            
        return type_map.get(q_type, QuestionType.VOCABULARY)
    
    def solve_with_gpt4(self, question: IOEQuestion, image_base64: Optional[str] = None) -> Tuple[Optional[str], float]:
        """Primary solver using GPT-4 Turbo Vision"""
        messages = [{"role": "system", "content": self.ioe_context}]
        
        content = []
        content.append({"type": "text", "text": self._build_prompt(question)})
        
        if image_base64:
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}
            })
            
        messages.append({"role": "user", "content": content})
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",  # Latest GPT-4o for best vision+text
                messages=messages,
                temperature=0.05,  # Very low for consistency
                max_tokens=800,
                top_p=0.95
            )
            
            answer = self._extract_answer(response.choices[0].message.content, question)
            confidence = self._calculate_confidence(response.choices[0].message.content)
            return answer, confidence
            
        except Exception as e:
            print(f"GPT-4 Error: {e}")
            return None, 0.0
    
    def solve_with_claude(self, question: IOEQuestion) -> Tuple[Optional[str], float]:
        """Secondary solver using Claude 3.5 Sonnet"""
        if not self.anthropic_client:
            return None, 0.0
        try:
            message = self.anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=800,
                temperature=0.05,
                system=self.ioe_context,
                messages=[{
                    "role": "user",
                    "content": self._build_prompt(question)
                }]
            )
            
            answer = self._extract_answer(message.content[0].text, question)
            confidence = self._calculate_confidence(message.content[0].text)
            return answer, confidence
            
        except Exception as e:
            print(f"Claude Error: {e}")
            return None, 0.0
    
    def solve_with_ensemble(self, question_data: Dict, image_data: Optional[bytes] = None) -> Dict:
        """Ensemble: GPT-4 + Claude consensus for 99% accuracy"""
        question = self.analyze_question(question_data)
        image_b64 = base64.b64encode(image_data).decode() if image_data else None
        
        results = {}
        confidences = {}
        
        # Parallel/Sequential calls (implement parallel with threading for production)
        ans_gpt4, conf_gpt4 = self.solve_with_gpt4(question, image_b64)
        if ans_gpt4:
            results['gpt4'] = ans_gpt4
            confidences['gpt4'] = conf_gpt4
            
        ans_claude, conf_claude = self.solve_with_claude(question)
        if ans_claude:
            results['claude'] = ans_claude
            confidences['claude'] = conf_claude
            
        # Fallback to Groq if both fail
        if not results:
            ans_groq = self._solve_with_groq(question)
            if ans_groq:
                results['groq'] = ans_groq
                confidences['groq'] = 0.85
                
        # Consensus with confidence weighting
        final_answer = self._consensus_vote(results, confidences)
        avg_confidence = sum(confidences.values()) / len(confidences) if confidences else 0.5
        
        return {
            "answer": final_answer,
            "confidence": avg_confidence,
            "sources": list(results.keys()),
            "reasoning": f"Consensus of {len(results)} models"
        }
    
    def _build_prompt(self, q: IOEQuestion) -> str:
        specific = {
            QuestionType.LISTENING: "LISTENING: Focus on implied meaning, not exact words. Check for homophones and numbers/dates.",
            QuestionType.READING: "READING: Identify skimming (gist) vs scanning (detail). Watch for 'except', 'not stated' tricks.",
            QuestionType.GRAMMAR: "GRAMMAR: Check subject-verb agreement, tense consistency, preposition collocation first.",
            QuestionType.FILL_BLANK: "FILL BLANK: Determine POS (noun/verb/adj/adv) from context before choosing.",
            QuestionType.ORDERING: "ORDERING: Find chronological/logical connectors (however, therefore, subsequently).",
            QuestionType.MATCHING: "MATCHING: Check parallel structure and lexical sets (synonyms/antonyms)."
        }.get(q.type, "Analyze carefully.")
        
        prompt = f"""IOE Question #{q.id} | Type: {q.type.value}
{specific}

Content: {q.content}
"""
        if q.options:
            prompt += "\nOptions:\n" + "\n".join([f"- {opt}" for opt in q.options])
            
        prompt += "\n\nREQUIRED OUTPUT FORMAT:\nANSWER: [exact answer text or option letter]\nCONFIDENCE: [0.0-1.0]\nREASON: [one sentence linguistic justification]"
        
        return prompt
    
    def _extract_answer(self, response: str, question: IOEQuestion) -> str:
        patterns = [
            r'ANSWER:\s*(.+?)(?:\n|CONFIDENCE|$)',
            r'Đáp án:\s*(.+?)(?:\n|$)',
            r'^\s*([A-D])(?:[.):])',
            r'\"([^\"]+)\"'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, response, re.MULTILINE | re.IGNORECASE)
            if match:
                ans = match.group(1).strip()
                ans = re.sub(r'[\"\'\)\(]', '', ans)
                return ans
        
        lines = [l.strip() for l in response.split('\n') if l.strip() and not any(x in l.lower() for x in ['reason', 'confidence', 'step'])]
        return lines[0][:200] if lines else response[:200]
    
    def _calculate_confidence(self, response: str) -> float:
        score = 0.75
        
        high_conf = ['certainly', 'definitely', 'clearly', 'chắc chắn', 'correct', 'accurate']
        low_conf = ['maybe', 'perhaps', 'possibly', 'unsure']
        
        text_lower = response.lower()
        if any(w in text_lower for w in high_conf):
            score += 0.2
        if any(w in text_lower for w in low_conf):
            score -= 0.25
            
        # Parse explicit confidence
        conf_match = re.search(r'CONFIDENCE:\s*([0-9.]+)', response)
        if conf_match:
            try:
                explicit = float(conf_match.group(1))
                if 0 <= explicit <= 1:
                    score = explicit
            except:
                pass
                
        return max(0.0, min(1.0, score))
    
    def _consensus_vote(self, results: Dict[str, str], confidences: Dict[str, float]) -> str:
        if not results:
            return ""
            
        if len(results) == 1:
            return list(results.values())[0]
            
        # Normalize answers
        votes = {}
        for model, ans in results.items():
            key = ans.lower().strip().rstrip('.')
            if key not in votes:
                votes[key] = []
            votes[key].append((model, confidences[model]))
            
        # Weighted voting
        best_score = 0
        best_ans = list(results.values())[0]
        
        for norm_ans, model_votes in votes.items():
            score = sum(v[1] for v in model_votes)
            # Boost if GPT-4 and Claude agree
            models = [v[0] for v in model_votes]
            if 'gpt4' in models and 'claude' in models:
                score *= 1.5  # High confidence boost for agreement
                
            if score > best_score:
                best_score = score
                # Return original case from highest confidence model
                best_model = max(model_votes, key=lambda x: x[1])[0]
                best_ans = results[best_model]
                
        return best_ans
    
    def _solve_with_groq(self, question: IOEQuestion) -> Optional[str]:
        if not self.groq_api:
            return None
            
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {self.groq_api}"},
                json={
                    "model": "mixtral-8x7b-32768",
                    "messages": [
                        {"role": "system", "content": self.ioe_context},
                        {"role": "user", "content": self._build_prompt(question)}
                    ],
                    "temperature": 0.1,
                    "max_tokens": 500
                },
                timeout=10
            )
            
            if response.status_code == 200:
                content = response.json()['choices'][0]['message']['content']
                return self._extract_answer(content, question)
        except:
            pass
        return None

# Singleton
ioe_master = IOEMasterAI()
