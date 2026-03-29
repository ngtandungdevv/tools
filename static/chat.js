/* static/chat.js */
document.addEventListener('DOMContentLoaded', () => {
    // Inject HTML
    const widgetHtml = `
    <div class="chat-widget" id="chat-widget">
        <button class="chat-btn" id="chat-btn" aria-label="Open Chat">
            <i class="fas fa-comment-dots"></i>
        </button>
        <div class="chat-panel" id="chat-panel">
            <div class="chat-header">
                <div class="chat-header-info">
                    <div class="chat-avatar"><i class="fas fa-headset"></i></div>
                    <div>
                        <div class="chat-title">Tan Dung Support</div>
                        <div class="chat-status">● Online</div>
                    </div>
                </div>
                <button class="chat-close" id="chat-close"><i class="fas fa-times"></i></button>
            </div>
            <div class="chat-body" id="chat-body">
                <div class="chat-msg admin">Xin chào! Tôi có thể giúp gì cho bạn?</div>
            </div>
            <div class="chat-footer">
                <input type="text" class="chat-input" id="chat-input" placeholder="Nhắn tin cho admin..." autocomplete="off">
                <button class="chat-send" id="chat-send"><i class="fas fa-paper-plane"></i></button>
            </div>
        </div>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', widgetHtml);

    const btn = document.getElementById('chat-btn');
    const panel = document.getElementById('chat-panel');
    const closeBtn = document.getElementById('chat-close');
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('chat-send');
    const body = document.getElementById('chat-body');

    let isOpen = false;
    let lastId = 0;
    let pollInterval = null;

    btn.addEventListener('click', () => {
        isOpen = !isOpen;
        if(isOpen) {
            panel.classList.add('show');
            btn.innerHTML = '<i class="fas fa-chevron-down"></i>';
            scrollToBottom();
            input.focus();
            if(!pollInterval) pollInterval = setInterval(syncMessages, 3000);
            syncMessages();
        } else {
            panel.classList.remove('show');
            btn.innerHTML = '<i class="fas fa-comment-dots"></i>';
            if(pollInterval) { clearInterval(pollInterval); pollInterval=null; }
        }
    });

    closeBtn.addEventListener('click', () => {
        isOpen = false;
        panel.classList.remove('show');
        btn.innerHTML = '<i class="fas fa-comment-dots"></i>';
        if(pollInterval) { clearInterval(pollInterval); pollInterval=null; }
    });

    function scrollToBottom() {
        body.scrollTop = body.scrollHeight;
    }

    function addMessage(msg, senderCls) {
        const div = document.createElement('div');
        div.className = `chat-msg ${senderCls}`;
        div.textContent = msg;
        body.appendChild(div);
        scrollToBottom();
    }

    async function syncMessages() {
        try {
            const res = await fetch(`/api/chat/sync?last_id=${lastId}`);
            const data = await res.json();
            if(data.success && data.messages.length > 0) {
                data.messages.forEach(m => {
                    const cls = m.sender === 'visitor' ? 'visitor' : 'admin';
                    addMessage(m.message, cls);
                    if(m.id > lastId) lastId = m.id;
                });
            }
        } catch(e) {}
    }

    async function sendMessage() {
        const text = input.value.trim();
        if(!text) return;
        input.value = '';
        input.focus();
        // Optimistic UI update disabled to prevent duplicate if synced fast
        // We will just let sync pull it.
        try {
            await fetch('/api/chat/send', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ message: text })
            });
            syncMessages(); // immediately sync
        } catch(e) {}
    }

    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => {
        if(e.key === 'Enter') sendMessage();
    });
});
