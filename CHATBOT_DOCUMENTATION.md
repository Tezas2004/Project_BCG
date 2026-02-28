# Financial Analysis Chatbot — Documentation

## Overview

This is a **simplified prototype** of an AI-style chatbot for financial analysis. It does not use machine learning or NLP; it matches user input to **predefined queries** and returns **canned responses** built from analyzed financial data. It fits learning objectives and time constraints while illustrating the basics of chatbot design.

## How It Works

1. **Data**: Financial metrics (revenue, net income, operating expenses, total assets) are stored in `data/financial_data.csv` for three years (2022–2024).
2. **Analysis**: `data/analysis_summary.py` loads the CSV and computes summary statistics (e.g. latest values, year-over-year changes). The chatbot uses these to build answers.
3. **Matching**: `chatbot.py` normalizes the user’s question (lowercase, strip punctuation) and checks it against a list of predefined phrases (e.g. “what is the total revenue”, “net income change”).
4. **Responses**: Each matched phrase maps to a response key. The response text is generated using the analysis summary (e.g. “The total revenue is $158.0 million.”).

## Predefined Queries and Responses

| Query (examples) | Topic | Response content |
|------------------|--------|-------------------|
| “What is the total revenue?” / “total revenue” | Total revenue | Latest year revenue from data |
| “How has net income changed over the last year?” / “net income change” | Net income change | YoY % change and prior vs latest values |
| “What are the operating expenses?” / “operating expenses” | Operating expenses | Latest year operating expenses |
| “What are total assets?” / “total assets” | Total assets | Latest year total assets |
| “How has revenue grown?” / “revenue growth” | Revenue growth | YoY % growth and prior vs latest revenue |

The bot accepts minor wording variations (e.g. with or without “?”) as long as the key phrase is present.

## How to Run

### 1. Environment

```bash
cd project_BCG
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Command-line (interactive)

```bash
python chatbot.py
```

Then type questions and press Enter. Type `quit` or `exit` to stop.

### 3. Single query from command line

```bash
python chatbot.py --query "What is the total revenue?"
```

### 4. Web interface (Flask)

```bash
python app.py
# or: flask --app app run
```

Open http://127.0.0.1:5000 in a browser and use the chat box.

### 5. Tests

```bash
pip install pytest
python -m pytest test_chatbot.py -v
```

## Limitations

- **Predefined only**: The bot only answers the 3–5 financial questions above. Any other question receives a fallback message suggesting the predefined queries.
- **No real NLP**: No intent detection or entity extraction; matching is phrase-based (substring/key phrase).
- **Static data**: Responses are based on the current `financial_data.csv`. Updating the CSV and re-running will change the numbers in the answers.
- **No memory**: Each turn is independent; the bot does not remember previous messages or user context.
- **English only**: Queries and responses are in English; no translation or multi-language support.

## Files to Submit (for zip)

- `chatbot.py` — core chatbot logic
- `app.py` — Flask web app (optional)
- `data/financial_data.csv` — sample financial data
- `data/analysis_summary.py` — data loading and summary
- `requirements.txt` — dependencies
- `test_chatbot.py` — tests
- `CHATBOT_DOCUMENTATION.md` — this documentation

## Refreshing the Data (Task 1 link)

To align the chatbot with your own Task 1 analysis:

1. Replace or edit `data/financial_data.csv` with your analyzed figures (same or similar columns).
2. If your metrics differ, adjust `data/analysis_summary.py` so it still returns a dictionary with the keys used in `chatbot.py` (e.g. `total_revenue_latest`, `net_income_change_pct`).
3. Re-run the chatbot; responses will reflect the new data.
