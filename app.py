from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, send_from_directory
import requests
import sqlite3
import json
import os
import uuid
import base64
from datetime import datetime
from functools import wraps
from io import BytesIO
from ai_engine import ioe_master
import utils_cccd
import utils_mb
import utils_vebay
import utils_vcb
import utils_downtt
import utils_voice
import subprocess
import sys
import logging
import traceback
import re
from logging.handlers import RotatingFileHandler

active_processes = {}

app = Flask(__name__)
app.secret_key = 'tokyo_tech_secret_key_2024_v2_ai'

# ============================================================
# ERROR LOGGER — writes ALL errors to error_log.txt
# ============================================================
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error_log.txt')

# Xóa log cũ mỗi khi khởi động server
with open(LOG_PATH, 'w', encoding='utf-8') as _f:
    _f.write(f"=== Server started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

_file_handler = RotatingFileHandler(LOG_PATH, maxBytes=5*1024*1024, backupCount=3, encoding='utf-8')
_file_handler.setLevel(logging.DEBUG)
_file_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s %(name)s — %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))

# Root logger: catches everything
logging.root.setLevel(logging.DEBUG)
logging.root.addHandler(_file_handler)

# Flask app logger
app_logger = logging.getLogger('app')

# Also attach to Flask's own logger & werkzeug
logging.getLogger('werkzeug').addHandler(_file_handler)
app.logger.addHandler(_file_handler)
app.logger.setLevel(logging.DEBUG)

def _log_exception(exc_type, exc_value, exc_tb):
    """Catch ALL uncaught exceptions and write to error_log.txt"""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_tb)
        return
    msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    app_logger.critical(f'Uncaught exception:\n{msg}')
    sys.__excepthook__(exc_type, exc_value, exc_tb)

sys.excepthook = _log_exception
app_logger.info('=== App started ===')

# Config
ADMIN_PASSWORD = 'ntd942010'
DB_PATH = 'visitor_logs.db'
CONFIG_PATH = 'tools_config.json'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# IOE Constants
BASE_URL = "https://api-edu.go.vn/ioe-service/v2/game"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  ip TEXT,
                  action TEXT,
                  timestamp TEXT,
                  user_agent TEXT,
                  path TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS music
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  filename TEXT,
                  url TEXT,
                  is_upload INTEGER DEFAULT 0,
                  order_index INTEGER DEFAULT 0,
                  created_at TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS social_links
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  platform TEXT,
                  url TEXT,
                  icon TEXT,
                  display_name TEXT,
                  order_index INTEGER DEFAULT 0,
                  created_at TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS discord_tokens
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nickname TEXT,
                  token TEXT,
                  created_at TEXT)''')
                  
    c.execute('''CREATE TABLE IF NOT EXISTS live_chat
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  session_id TEXT,
                  sender TEXT,
                  message TEXT,
                  timestamp TEXT,
                  is_read INTEGER DEFAULT 0)''')

    c.execute('''CREATE TABLE IF NOT EXISTS discord_friends
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  discord_id TEXT UNIQUE,
                  display_name TEXT,
                  avatar_url TEXT,
                  discriminator TEXT,
                  added_at TEXT)''')
    
    conn.commit()
    conn.close()

def init_config():
    if not os.path.exists(CONFIG_PATH):
        default_config = {
            "tools": {
                "ioe": {"name": "IOE Solver Pro", "enabled": True, "icon": "🎯", "desc": "AI-Powered Auto Solve 99% Accuracy"},
                "data_miner": {"name": "Data Miner", "enabled": False, "icon": "📊", "desc": "Extract data"},
                "crypto": {"name": "Crypto Vault", "enabled": False, "icon": "🔐", "desc": "Encryption tool"},
                "speed": {"name": "Speed Boost", "enabled": False, "icon": "⚡", "desc": "Network optimize"}
            }
        }
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4)

init_db()
init_config()

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

def log_visitor(action, path=None):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if ',' in ip:
            ip = ip.split(',')[0].strip()
        
        c.execute("INSERT INTO logs (ip, action, timestamp, user_agent, path) VALUES (?, ?, ?, ?, ?)",
                 (ip, action, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                  str(request.user_agent), path or request.path))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Logging error: {e}")

def get_client_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ',' in ip:
        ip = ip.split(',')[0].strip()
    return ip

@app.before_request
def before_request():
    if not request.path.startswith('/static'):
        log_visitor(f"Access {request.method}", request.path)

@app.route('/')
def index():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    enabled_tools = {k: v for k, v in config['tools'].items() if v['enabled']}
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT platform, url, icon, display_name FROM social_links ORDER BY order_index")
    social_links = c.fetchall()
    
    c.execute("SELECT title, filename, url, is_upload FROM music ORDER BY order_index")
    playlist = c.fetchall()
    conn.close()
    
    return render_template('index.html', tools=enabled_tools, visitor_ip=get_client_ip(), 
                         social_links=social_links, playlist=playlist)

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form.get('password', '')
        if password == ADMIN_PASSWORD:
            session['is_admin'] = True
            log_visitor("Admin login successful")
            return redirect(url_for('admin_panel'))
        else:
            log_visitor("Admin login failed")
            flash('Sai mật khẩu!', 'error')
    
    if session.get('is_admin'):
        return redirect(url_for('admin_panel'))
    
    return render_template('admin_login.html')

@app.route('/admin/panel')
@admin_required
def admin_panel():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 200")
    logs = c.fetchall()
    
    c.execute("SELECT COUNT(DISTINCT ip) FROM logs WHERE timestamp >= date('now')")
    unique_ips = c.fetchone()[0] or 0
    
    c.execute("SELECT COUNT(*) FROM logs WHERE timestamp >= date('now')")
    total_visits = c.fetchone()[0] or 0
    
    c.execute("SELECT * FROM music ORDER BY order_index")
    music_list = c.fetchall()
    
    c.execute("SELECT * FROM social_links ORDER BY order_index")
    social_list = c.fetchall()
    
    conn.close()
    
    return render_template('admin.html', 
                         config=config, 
                         logs=logs, 
                         unique_ips=unique_ips, 
                         total_visits=total_visits,
                         current_ip=get_client_ip(),
                         music_list=music_list,
                         social_list=social_list)

@app.route('/admin/music/add', methods=['POST'])
@admin_required
def add_music():
    title = request.form.get('title')
    url = request.form.get('url')
    file = request.files.get('file')
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    try:
        if file and file.filename:
            ext = file.filename.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            c.execute("INSERT INTO music (title, filename, url, is_upload, created_at) VALUES (?, ?, ?, 1, ?)",
                     (title, filename, f"/static/uploads/{filename}", datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        elif url:
            c.execute("INSERT INTO music (title, url, is_upload, created_at) VALUES (?, ?, 0, ?)",
                     (title, url, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        log_visitor("Admin added music")
    except Exception as e:
        print(f"Music add error: {e}")
    finally:
        conn.close()
    
    return redirect(url_for('admin_panel'))

@app.route('/admin/music/delete/<int:id>', methods=['POST'])
@admin_required
def delete_music(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT filename, is_upload FROM music WHERE id=?", (id,))
    result = c.fetchone()
    
    if result and result[1] == 1:
        try:
            os.remove(os.path.join(UPLOAD_FOLDER, result[0]))
        except:
            pass
    
    c.execute("DELETE FROM music WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route('/admin/social/add', methods=['POST'])
@admin_required
def add_social():
    platform = request.form.get('platform')
    url = request.form.get('url')
    display_name = request.form.get('display_name')
    
    icons = {
        'facebook': 'fab fa-facebook',
        'discord': 'fab fa-discord',
        'telegram': 'fab fa-telegram',
        'tiktok': 'fab fa-tiktok',
        'youtube': 'fab fa-youtube',
        'github': 'fab fa-github',
        'twitter': 'fab fa-twitter',
        'instagram': 'fab fa-instagram',
        'zalo': 'fas fa-comment-dots',
        'email': 'fas fa-envelope',
        'website': 'fas fa-globe'
    }
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO social_links (platform, url, icon, display_name, created_at) VALUES (?, ?, ?, ?, ?)",
             (platform, url, icons.get(platform, 'fas fa-link'), display_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()
    log_visitor(f"Admin added social {platform}")
    return redirect(url_for('admin_panel'))

@app.route('/admin/social/delete/<int:id>', methods=['POST'])
@admin_required
def delete_social(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM social_links WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route('/admin/toggle-tool', methods=['POST'])
@admin_required
def toggle_tool():
    tool = request.json.get('tool')
    enabled = request.json.get('enabled')
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    if tool in config['tools']:
        config['tools'][tool]['enabled'] = enabled
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)
        
        log_visitor(f"Admin toggled tool {tool} to {enabled}")
        return jsonify({"success": True})
    
    return jsonify({"success": False}), 400

@app.route('/admin/clear-logs', methods=['POST'])
@admin_required
def clear_logs():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM logs")
    conn.commit()
    conn.close()
    log_visitor("Admin cleared logs")
    return jsonify({"success": True})

@app.route('/admin/logout')
def admin_logout():
    session.pop('is_admin', None)
    return redirect(url_for('admin_login'))

@app.route('/ioe')
def ioe_page():
    log_visitor("View IOE tool")
    return render_template('ioe.html')

@app.route('/call-spam')
def spam_page():
    log_visitor("View Call Spam tool")
    return render_template('spam.html')

@app.route('/sms-spam')
def sms_spam_page():
    log_visitor("View SMS Spam tool")
    return render_template('sms_spammer.html')

@app.route('/discord-quest')
def discord_quest_page():
    log_visitor("View Discord Quest tool")
    return render_template('discord_quest.html')

@app.route('/cccd')
def cccd_page():
    log_visitor("View CCCD Generator tool")
    return render_template('cccd.html')

@app.route('/mb-bank')
def mb_bank_page():
    log_visitor("View MB Bank Bill Generator tool")
    return render_template('mb_bank.html', nen_names=utils_mb.NEN_NAMES)


# IOE API Endpoints
@app.route('/api/ioe/getinfo', methods=['POST'])
def ioe_getinfo():
    try:
        data = request.json
        resp = requests.post(f"{BASE_URL}/getinfo", json=data, timeout=10)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e), "IsSuccessed": False}), 500

@app.route('/api/ioe/startgame', methods=['POST'])
def ioe_startgame():
    try:
        data = request.json
        resp = requests.post(f"{BASE_URL}/startgame", json=data, timeout=10)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e), "IsSuccessed": False}), 500

@app.route('/api/ioe/answercheck', methods=['POST'])
def ioe_answercheck():
    try:
        data = request.json
        resp = requests.post(f"{BASE_URL}/answercheck", json=data, timeout=10)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e), "IsSuccessed": False}), 500

@app.route('/api/ioe/finishgame', methods=['POST'])
def ioe_finishgame():
    try:
        data = request.json
        resp = requests.post(f"{BASE_URL}/finishgame", json=data, timeout=15)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e), "IsSuccessed": False}), 500

# AI Super Engine Endpoints
@app.route('/api/ioe/solve-with-ai', methods=['POST'])
def solve_with_ai():
    """IOE-GPT Master Engine Endpoint"""
    try:
        data = request.json
        question = data.get('question', {})
        
        # Xử lý image nếu có
        image_data = None
        if question.get('image'):
            try:
                if question['image'].startswith('http'):
                    resp = requests.get(question['image'], timeout=5)
                    image_data = resp.content
                else:
                    image_data = base64.b64decode(question['image'])
            except:
                pass
        
        # Gọi AI Engine
        result = ioe_master.solve_with_ensemble(question, image_data)
        
        return jsonify({
            "success": True,
            "answer": result['answer'],
            "confidence": result['confidence'],
            "method": "ensemble",
            "sources": result['sources'],
            "explanation": result['reasoning']
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "answer": None
        }), 500

@app.route('/api/ioe/transcribe', methods=['POST'])
def transcribe_audio():
    """Whisper API for Listening questions"""
    try:
        audio_url = request.json.get('audio_url')
        if not audio_url:
            return jsonify({"error": "No audio URL"}), 400
            
        audio_resp = requests.get(audio_url, timeout=10)
        audio_file = BytesIO(audio_resp.content)
        audio_file.name = "audio.mp3"
        
        transcript = ioe_master.openai_client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
        
        return jsonify({
            "success": True,
            "transcript": transcript,
            "language": "en"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================
# DISCORD TOKEN CRUD API
# ============================================================
@app.route('/api/discord/tokens', methods=['GET'])
def get_discord_tokens():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, nickname, token, created_at FROM discord_tokens ORDER BY id")
    rows = c.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "nickname": r[1], "token": r[2], "created_at": r[3]} for r in rows])

@app.route('/api/discord/tokens', methods=['POST'])
def add_discord_token():
    data = request.json
    nickname = data.get('nickname', '').strip()
    token = data.get('token', '').strip()
    if not token:
        return jsonify({"success": False, "message": "Token không được để trống"}), 400
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO discord_tokens (nickname, token, created_at) VALUES (?, ?, ?)",
              (nickname or f"Token {datetime.now().strftime('%H:%M:%S')}", token, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    token_id = c.lastrowid
    conn.commit()
    conn.close()
    log_visitor("Added Discord token")
    return jsonify({"success": True, "id": token_id})

@app.route('/api/discord/tokens/<int:token_id>', methods=['PUT'])
def update_discord_token(token_id):
    data = request.json
    nickname = data.get('nickname', '').strip()
    token = data.get('token', '').strip()
    if not token:
        return jsonify({"success": False, "message": "Token không được để trống"}), 400
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE discord_tokens SET nickname=?, token=? WHERE id=?", (nickname, token, token_id))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route('/api/discord/tokens/<int:token_id>', methods=['DELETE'])
def delete_discord_token(token_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM discord_tokens WHERE id=?", (token_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

# ============================================================
# DISCORD QUEST RUNNER – token queue
# ============================================================
# ANSI escape sequence regex
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

discord_quest_state = {
    "running": False,
    "queue": [],        # list of {id, nickname, token}
    "current_idx": -1,
    "statuses": {},     # token_id -> "waiting"|"running"|"done"|"failed"
    "process": None,
    "logs": [],
    "live": {           # Live parsed data for the current token
        "account": None,
        "id": None,
        "orbs": None,
        "quests": []    # List of {id, name, type, reward, remaining, status}
    }
}

def _run_next_discord_token():
    state = discord_quest_state
    idx = state["current_idx"] + 1
    abs_root = os.path.dirname(os.path.abspath(__file__))
    tool_dir = os.path.join(abs_root, 'Discord-Auto-Quests-Discord-Tool')

    # Auto npm install if node_modules missing
    if not os.path.isdir(os.path.join(tool_dir, 'node_modules')):
        state["logs"].append("[Setup] node_modules not found, running npm install...")
        try:
            result = subprocess.run('npm install', cwd=tool_dir, shell=True,
                                    capture_output=True, text=True, timeout=120)
            if result.returncode == 0:
                state["logs"].append("[Setup] npm install OK")
            else:
                state["logs"].append(f"[Setup] npm install FAILED: {result.stderr[:200]}")
                state["running"] = False
                return
        except Exception as e:
            state["logs"].append(f"[Setup] npm install error: {e}")
            state["running"] = False
            return

    while idx < len(state["queue"]):
        entry = state["queue"][idx]
        state["current_idx"] = idx
        state["statuses"][entry["id"]] = "running"
        state["live"] = {"account": None, "id": None, "orbs": None, "quests": []}
        
        env_path = os.path.join(tool_dir, '.env')
        # Write token to .env
        with open(env_path, 'w') as f:
            f.write(f"TOKEN={entry['token']}\n")
        
        try:
            proc = subprocess.Popen(
                'npm run go',
                cwd=tool_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
            state["process"] = proc
            state["logs"].append(f"[{entry['nickname']}] Started...")
            
            # Stream output line by line
            for line in proc.stdout:
                line = line.rstrip()
                if not line: continue
                
                # Strip ANSI codes for clean logs
                clean_line = ANSI_ESCAPE.sub('', line)
                if not clean_line.strip(): continue
                
                state["logs"].append(f"  {clean_line}")
                if len(state["logs"]) > 200:
                    state["logs"] = state["logs"][-200:]
                
                # PARSING LOGIC for Live Dashboard
                # Example: ⦿ Account: username | ID: 123 | Orbs: 🔮 500 | 12:00:00
                if "Account:" in clean_line:
                    m_acc = re.search(r'Account:\s*([^\s|]+)', clean_line)
                    m_id = re.search(r'ID:\s*([^\s|]+)', clean_line)
                    m_orbs = re.search(r'Orbs:\s*🔮\s*(\d+)', clean_line)
                    if m_acc: state["live"]["account"] = m_acc.group(1)
                    if m_id: state["live"]["id"] = m_id.group(1)
                    if m_orbs: state["live"]["orbs"] = m_orbs.group(1)
                
                # Parse Table Rows (e.g. │ 1 │ Watch Trailer │ 🎬 │ 50 Orbs │ 2m 30s │ ⟳ RUN │)
                if clean_line.startswith('│') and 'QUEST' not in clean_line and '─' not in clean_line:
                    parts = [p.strip() for p in clean_line.split('│')]
                    if len(parts) >= 7: # [empty, #, QUEST, TYPE, REWARD, REMAINING, STATUS, empty]
                        q_data = {
                            "index": parts[1],
                            "name": parts[2],
                            "type": parts[3],
                            "reward": parts[4],
                            "remaining": parts[5],
                            "status": parts[6]
                        }
                        # Update or add quest
                        found = False
                        for q in state["live"]["quests"]:
                            if q["name"] == q_data["name"]:
                                q.update(q_data)
                                found = True
                                break
                        if not found:
                            state["live"]["quests"].append(q_data)

            proc.wait()
            rc = proc.returncode
            state["statuses"][entry["id"]] = "done" if rc == 0 else "failed"
            state["logs"].append(f"[{entry['nickname']}] Finished (exit {rc})")
        except Exception as e:
            state["statuses"][entry["id"]] = "failed"
            state["logs"].append(f"[{entry['nickname']}] Error: {e}")
        
        state["process"] = None
        idx += 1
    
    state["running"] = False
    state["logs"].append("All tokens processed.")


@app.route('/api/discord-quest/start', methods=['POST'])
def start_discord_quest():
    state = discord_quest_state
    if state["running"]:
        return jsonify({"success": False, "message": "Đang chạy, hãy dừng trước"})
    data = request.json
    token_ids = data.get('token_ids', [])
    if not token_ids:
        return jsonify({"success": False, "message": "Chưa chọn token nào"})
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    placeholders = ','.join('?' * len(token_ids))
    c.execute(f"SELECT id, nickname, token FROM discord_tokens WHERE id IN ({placeholders})", token_ids)
    rows = c.fetchall()
    conn.close()
    if not rows:
        return jsonify({"success": False, "message": "Không tìm thấy token"})
    state["running"] = True
    state["queue"] = [{"id": r[0], "nickname": r[1], "token": r[2]} for r in rows]
    state["current_idx"] = -1
    state["statuses"] = {r[0]: "waiting" for r in rows}
    state["logs"] = ["Queue started..."]
    state["process"] = None
    import threading
    t = threading.Thread(target=_run_next_discord_token, daemon=True)
    t.start()
    log_visitor(f"Started Discord Quest for {len(rows)} tokens")
    return jsonify({"success": True, "message": f"Đang chạy {len(rows)} token(s)"})

@app.route('/api/discord-quest/stop', methods=['POST'])
def stop_discord_quest():
    state = discord_quest_state
    state["running"] = False
    if state["process"]:
        try:
            state["process"].terminate()
        except: pass
        state["process"] = None
    for tid in state["statuses"]:
        if state["statuses"][tid] in ("waiting", "running"):
            state["statuses"][tid] = "failed"
    state["logs"].append("Stopped by user.")
    return jsonify({"success": True, "message": "Đã dừng"})

@app.route('/api/discord-quest/status', methods=['GET'])
def discord_quest_status():
    return jsonify({
        "running": discord_quest_state["running"],
        "statuses": discord_quest_state["statuses"],
        "logs": discord_quest_state["logs"][-100:],
        "live": discord_quest_state["live"],
        "current_idx": discord_quest_state["current_idx"]
    })

@app.route('/api/system/logs', methods=['GET'])
def get_system_logs():
    """Returns last 100 lines of error_log.txt"""
    try:
        if not os.path.exists(LOG_PATH):
            return jsonify({"success": True, "logs": "Log file not found."})
        with open(LOG_PATH, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
            # Get last 100 lines
            last_lines = lines[-100:]
            return jsonify({"success": True, "logs": "".join(last_lines)})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/api/call-spam/start', methods=['POST'])
def start_call_spam():
    """Background execution of CALL Spam tool (nat1.py)"""
    data = request.json
    phone = data.get('phone')
    count = data.get('count', 1)
    
    if not phone:
        return jsonify({"success": False, "message": "Thiếu số điện thoại"})
        
    try:
        script_path = os.path.join(os.path.dirname(__file__), 'toolspamsms', 'nat1.py')
        flags = 0x00000010 if os.name == 'nt' else 0
        process = subprocess.Popen([sys.executable, script_path, str(phone), str(count)], creationflags=flags)
        active_processes[phone] = process
        
        log_visitor(f"Started CALL Attack on {phone} ({count}x)")
        return jsonify({"success": True, "message": "Call Attack initiated successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/api/call-spam/stop', methods=['POST'])
def stop_call_spam():
    phone = request.json.get('phone')
    if phone in active_processes:
        try:
            active_processes[phone].terminate()
            del active_processes[phone]
            return jsonify({"success": True, "message": "Đã chặn cuộc tấn công thành công!"})
        except Exception as e:
            return jsonify({"success": False, "message": str(e)})
    return jsonify({"success": False, "message": "Không tìm thấy bot đang chạy trên số này."})

@app.route('/api/sms-spam/start', methods=['POST'])
def start_sms_spam():
    """Background execution of SMS Spam tool (spamsms.py)"""
    data = request.json
    phone = data.get('phone')
    count = data.get('count', 1)
    
    if not phone:
        return jsonify({"success": False, "message": "Thiếu số điện thoại"})
        
    try:
        script_path = os.path.join(os.path.dirname(__file__), 'spamsms.py')
        flags = 0x00000010 if os.name == 'nt' else 0
        process = subprocess.Popen([sys.executable, script_path, str(phone), str(count)], creationflags=flags)
        active_processes[phone] = process
        
        log_visitor(f"Started SMS Attack on {phone} ({count}x)")
        return jsonify({"success": True, "message": "SMS Attack initiated successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/api/sms-spam/stop', methods=['POST'])
def stop_sms_spam():
    phone = request.json.get('phone')
    if phone in active_processes:
        try:
            active_processes[phone].terminate()
            del active_processes[phone]
            return jsonify({"success": True, "message": "Đã chặn cuộc tấn công SMS thành công!"})
        except Exception as e:
            return jsonify({"success": False, "message": str(e)})
    return jsonify({"success": False, "message": "Không tìm thấy tiến trình trên số này."})

# ============================================================
# CCCD COMMANDS API
# ============================================================
@app.route('/api/cccd/generate', methods=['POST'])
def generate_cccd():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Dữ liệu không hợp lệ"}), 400
    
    log_visitor("Generated CCCD Image")
    result = utils_cccd.generate_cccd_base64(data)
    if result.get("success"):
        return jsonify(result)
    else:
        return jsonify({"success": False, "message": result.get("error")}), 500

# ============================================================
# MB BANK COMMANDS API
# ============================================================
@app.route('/api/mb/generate', methods=['POST'])
def generate_mb():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Dữ liệu không hợp lệ"}), 400
    
    log_visitor("Generated MB Bank Bill")
    result = utils_mb.generate_mb_bank_base64(data)
    if result.get("success"):
        return jsonify(result)
    else:
        return jsonify({"success": False, "message": result.get("error")}), 500

# ============================================================
# NEW TOOLS API (VEBAY, VCB, DOWNTT)
# ============================================================
@app.route('/api/vebay/generate', methods=['POST'])
def generate_vebay():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Dữ liệu không hợp lệ"}), 400
    
    log_visitor("Generated Vietnam Airlines Ticket")
    result = utils_vebay.generate_vebay_base64(data)
    if result.get("success"):
        return jsonify(result)
    else:
        return jsonify({"success": False, "message": result.get("error")}), 500

@app.route('/api/vcb/generate', methods=['POST'])
def generate_vcb():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Dữ liệu không hợp lệ"}), 400
    
    log_visitor("Generated Vietcombank Bill")
    result = utils_vcb.generate_vcb_base64(data)
    if result.get("success"):
        return jsonify(result)
    else:
        return jsonify({"success": False, "message": result.get("error")}), 500

@app.route('/api/downtt/process', methods=['POST'])
def process_downtt():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"success": False, "message": "Thiếu URL"}), 400
    
    log_visitor("Accessed TikTok Downloader API")
    result = utils_downtt.process_downtt(url)
    if result.get("success"):
        return jsonify(result)
    else:
        return jsonify({"success": False, "message": result.get("error")}), 500

# ============================================================
# LIVE CHAT SUPPORT API
# ============================================================
@app.route('/api/chat/send', methods=['POST'])
def chat_send():
    data = request.json
    msg = data.get('message', '').strip()
    if not msg:
        return jsonify({"success": False})
        
    session_id = get_client_ip()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO live_chat (session_id, sender, message, timestamp, is_read) VALUES (?, ?, ?, ?, ?)",
              (session_id, 'visitor', msg, timestamp, 0))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route('/api/chat/sync', methods=['GET'])
def chat_sync():
    session_id = get_client_ip()
    last_id = request.args.get('last_id', 0, type=int)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, sender, message, timestamp FROM live_chat WHERE session_id = ? AND id > ? ORDER BY id ASC", 
              (session_id, last_id))
    rows = c.fetchall()
    conn.close()
    
    messages = [{"id": r[0], "sender": r[1], "message": r[2], "timestamp": r[3]} for r in rows]
    return jsonify({"success": True, "messages": messages})

@app.route('/admin/api/chat/sessions', methods=['GET'])
@admin_required
def admin_chat_sessions():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT session_id, MAX(timestamp) as last_time,
               (SELECT COUNT(*) FROM live_chat as t2 WHERE t2.session_id = t1.session_id AND sender='visitor' AND is_read=0) as unread
        FROM live_chat as t1
        GROUP BY session_id
        ORDER BY last_time DESC
    """)
    rows = c.fetchall()
    conn.close()
    sessions = [{"session_id": r[0], "last_time": r[1], "unread": r[2]} for r in rows]
    return jsonify({"success": True, "sessions": sessions})

@app.route('/admin/api/chat/history', methods=['GET'])
@admin_required
def admin_chat_history():
    session_id = request.args.get('session_id')
    if not session_id:
        return jsonify({"success": False})
        
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE live_chat SET is_read = 1 WHERE session_id = ? AND sender = 'visitor'", (session_id,))
    conn.commit()
    
    c.execute("SELECT id, sender, message, timestamp FROM live_chat WHERE session_id = ? ORDER BY id ASC", (session_id,))
    rows = c.fetchall()
    conn.close()
    
    messages = [{"id": r[0], "sender": r[1], "message": r[2], "timestamp": r[3]} for r in rows]
    return jsonify({"success": True, "messages": messages})

@app.route('/admin/api/chat/send', methods=['POST'])
@admin_required
def admin_chat_send():
    data = request.json
    session_id = data.get('session_id')
    msg = data.get('message', '').strip()
    
    if not session_id or not msg:
        return jsonify({"success": False})
        
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO live_chat (session_id, sender, message, timestamp, is_read) VALUES (?, ?, ?, ?, ?)",
              (session_id, 'admin', msg, timestamp, 1))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

# ============================================================
# REG MAIL API (MAIL.TM WRAPPER)
# ============================================================
@app.route('/api/mail/register', methods=['POST'])
def mail_register():
    data = request.json
    count = data.get('count', 1)
    if count > 50: count = 50
    results = []
    
    try:
        resp = requests.get("https://api.mail.tm/domains", timeout=10)
        resp.raise_for_status()
        domains = [m["domain"] for m in resp.json()["hydra:member"]]
        if not domains:
            return jsonify({"success": False, "message": "List domain rỗng!"})
            
        import random, string
        def rand_str(n=8): return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))
        
        for _ in range(count):
            address = f"{rand_str()}@{random.choice(domains)}"
            password = rand_str(12)
            
            r = requests.post("https://api.mail.tm/accounts", json={"address": address, "password": password}, timeout=10)
            if not r.ok: continue
            
            r2 = requests.post("https://api.mail.tm/token", json={"address": address, "password": password}, timeout=10)
            if r2.ok:
                token = r2.json()["token"]
                results.append({"mail": address, "pwd": password, "token": token})
                
        return jsonify({"success": True, "accounts": results})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/api/mail/inbox', methods=['POST'])
def mail_inbox():
    token = request.json.get('token')
    if not token:
        return jsonify({"success": False})
        
    try:
        resp = requests.get("https://api.mail.tm/messages", headers={"Authorization": f"Bearer {token}"}, timeout=10)
        if resp.ok:
            msgs = resp.json().get("hydra:member", [])
            return jsonify({"success": True, "messages": msgs})
        return jsonify({"success": False, "message": "Failed to fetch inbox"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/api/mail/read', methods=['POST'])
def mail_read():
    token = request.json.get('token')
    msg_id = request.json.get('msg_id')
    if not token or not msg_id: return jsonify({"success": False})
    
    try:
        resp = requests.get(f"https://api.mail.tm/messages/{msg_id}", headers={"Authorization": f"Bearer {token}"}, timeout=10)
        if resp.ok:
            data = resp.json()
            body = data.get("html", data.get("text", "(trống)"))
            return jsonify({"success": True, "content": body})
        return jsonify({"success": False, "message": "Error reading msg"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/reg_mail')
@app.route('/reg-mail')
def tool_reg_mail():
    log_visitor("Accessed Reg Mail", "/reg-mail")
    return render_template('reg_mail.html')

@app.route('/vebay')
def tool_vebay():
    log_visitor("Accessed Vé Bay", "/vebay")
    return render_template('vebay.html')

@app.route('/vcb')
def tool_vcb():
    log_visitor("Accessed VCB Bill", "/vcb")
    return render_template('vcb.html')

@app.route('/downtt')
def tool_downtt():
    log_visitor("Accessed DownTT", "/downtt")
    return render_template('downtt.html')

@app.route('/voice')
def tool_voice():
    log_visitor("Accessed Voice Generator", "/voice")
    return render_template('voice.html')

# ============================================================
# VOICE API
# ============================================================
@app.route('/api/voice/generate', methods=['POST'])
def generate_voice():
    data = request.json
    text = data.get('text', '').strip()
    lang = data.get('lang', 'vi')
    if not text:
        return jsonify({"success": False, "message": "Thiếu nội dung"}), 400
    log_visitor("Generated Voice MP3")
    result = utils_voice.generate_voice(text, lang)
    if result.get("success"):
        return jsonify(result)
    return jsonify({"success": False, "message": result.get("error")}), 500

# ============================================================
# DISCORD FRIENDS API (public)
# ============================================================
@app.route('/api/friends', methods=['GET'])
def get_friends():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT id, discord_id, display_name, avatar_url, discriminator, added_at FROM discord_friends ORDER BY id ASC")
        rows = c.fetchall()
        conn.close()
        friends = []
        for r in rows:
            friends.append({
                "id": r[0], "discord_id": r[1], "display_name": r[2],
                "avatar_url": r[3], "discriminator": r[4], "added_at": r[5]
            })
        return jsonify({"success": True, "friends": friends})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# ============================================================
# DISCORD FRIENDS ADMIN API
# ============================================================
def get_discord_token():
    return os.getenv('DISCORD_BOT_TOKEN', '')

@app.route('/admin/api/friends/lookup', methods=['POST'])
@admin_required
def lookup_discord_user():
    data = request.json
    discord_id = str(data.get('discord_id', '')).strip()
    if not discord_id:
        return jsonify({"success": False, "message": "Thiếu Discord ID"}), 400
    
    token = get_discord_token()
    if token:
        try:
            # Load environment locally to ensure it reads hot updates if any, but since it's in os.environ already.
            headers = {"Authorization": f"Bot {token}"}
            resp = requests.get(f"https://discord.com/api/v10/users/{discord_id}", headers=headers, timeout=10)
            if resp.status_code == 200:
                u = resp.json()
                avatar_hash = u.get("avatar")
                if avatar_hash:
                    avatar_url = f"https://cdn.discordapp.com/avatars/{discord_id}/{avatar_hash}.png?size=256"
                else:
                    avatar_url = f"https://cdn.discordapp.com/embed/avatars/{int(discord_id) % 5}.png"
                
                discriminator = u.get("discriminator", "0")
                global_name = u.get("global_name") or u.get("username", f"User_{discord_id}")
                username = u.get("username", f"User_{discord_id}")
                display_name = global_name if global_name else username

                return jsonify({
                    "success": True,
                    "discord_id": discord_id,
                    "display_name": display_name,
                    "username": username,
                    "avatar_url": avatar_url,
                    "discriminator": discriminator
                })
            else:
                return jsonify({"success": False, "message": f"Discord API Error {resp.status_code}: User not found"}), 404
        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 500
    else:
        return jsonify({"success": False, "message": "Bot token chưa được cấu hình"}), 500

@app.route('/admin/api/friends/add', methods=['POST'])
@admin_required
def add_discord_friend():
    data = request.json
    discord_id = str(data.get('discord_id', '')).strip()
    display_name = data.get('display_name', '').strip()
    avatar_url = data.get('avatar_url', '').strip()
    discriminator = data.get('discriminator', '0').strip()
    
    if not discord_id or not display_name:
        return jsonify({"success": False, "message": "Thiếu thông tin bắt buộc"}), 400
    
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            "INSERT OR REPLACE INTO discord_friends (discord_id, display_name, avatar_url, discriminator, added_at) VALUES (?,?,?,?,?)",
            (discord_id, display_name, avatar_url, discriminator, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )
        conn.commit()
        conn.close()
        log_visitor(f"Added Discord Friend: {display_name}")
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/admin/api/friends/delete/<int:friend_id>', methods=['POST'])
@admin_required
def delete_discord_friend(friend_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("DELETE FROM discord_friends WHERE id=?", (friend_id,))
        conn.commit()
        conn.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
