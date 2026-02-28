"""
Flask web app for the Financial Analysis Chatbot.
Run: flask --app app run
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flask import Flask, request, jsonify, render_template_string

from chatbot import simple_chatbot

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Analysis Chatbot</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: system-ui, sans-serif; max-width: 600px; margin: 2rem auto; padding: 0 1rem; }
        h1 { color: #1a365d; font-size: 1.5rem; }
        .chat { border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; min-height: 320px; background: #f8fafc; }
        .message { margin: 0.75rem 0; padding: 0.6rem 0.9rem; border-radius: 8px; max-width: 85%; }
        .user { background: #3182ce; color: white; margin-left: auto; }
        .bot { background: #e2e8f0; color: #1a202c; }
        .input-row { display: flex; gap: 0.5rem; margin-top: 1rem; }
        input[type="text"] { flex: 1; padding: 0.6rem; border: 1px solid #cbd5e0; border-radius: 6px; font-size: 1rem; }
        button { padding: 0.6rem 1.2rem; background: #3182ce; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 1rem; }
        button:hover { background: #2c5282; }
        .hint { font-size: 0.85rem; color: #718096; margin-top: 0.5rem; }
    </style>
</head>
<body>
    <h1>Financial Analysis Chatbot</h1>
    <p>Ask a predefined financial question below.</p>
    <div class="chat" id="chat">
        <div class="message bot">Hello! I can answer questions about total revenue, net income change, operating expenses, total assets, and revenue growth. What would you like to know?</div>
    </div>
    <div class="input-row">
        <input type="text" id="query" placeholder="Type your question..." autocomplete="off">
        <button type="button" onclick="send()">Send</button>
    </div>
    <p class="hint">Examples: "What is the total revenue?", "How has net income changed over the last year?"</p>
    <script>
        const chat = document.getElementById('chat');
        const input = document.getElementById('query');
        function addMessage(text, isUser) {
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'bot');
            div.textContent = text;
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }
        function send() {
            const q = input.value.trim();
            if (!q) return;
            addMessage(q, true);
            input.value = '';
            fetch('/api/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ query: q }) })
                .then(r => r.json())
                .then(d => addMessage(d.response, false))
                .catch(() => addMessage('Sorry, something went wrong.', false));
        }
        input.onkeydown = (e) => { if (e.key === 'Enter') send(); };
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    query = data.get("query", "").strip()
    response = simple_chatbot(query)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
