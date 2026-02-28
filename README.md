# Financial Analysis Chatbot Prototype

A simplified chatbot that answers **predefined financial queries** using analyzed data. Built for learning objectives with CLI and optional Flask web UI.

## Quick start

```bash
pip install -r requirements.txt
python chatbot.py
```

Type a question (e.g. *What is the total revenue?*) and press Enter. Type `quit` to exit.

**Web UI:** `python app.py` then open http://127.0.0.1:5000  
**Single query:** `python chatbot.py --query "What is the total revenue?"`  
**Tests:** `python -m pytest test_chatbot.py -v`

See **[CHATBOT_DOCUMENTATION.md](CHATBOT_DOCUMENTATION.md)** for how it works, predefined queries, and limitations.
