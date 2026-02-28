"""
Financial Analysis Chatbot Prototype
Responds to predefined financial queries using analyzed data.
"""
import sys
from pathlib import Path

# Add project root for imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
from data.analysis_summary import load_and_analyze


def format_currency(amount: float) -> str:
    """Format number as currency (millions)."""
    if amount >= 1_000_000:
        return f"${amount / 1_000_000:.1f} million"
    return f"${amount:,.0f}"


def build_responses():
    """Build canned responses from analyzed financial data."""
    data = load_and_analyze()
    return {
        "total_revenue": (
            f"The total revenue (latest year) is {format_currency(data['total_revenue_latest'])}."
        ),
        "net_income_change": (
            f"Net income has increased by {data['net_income_change_pct']}% over the last year, "
            f"from {format_currency(data['net_income_prior'])} to {format_currency(data['net_income_latest'])}."
        ),
        "operating_expenses": (
            f"Operating expenses in the latest period are {format_currency(data['operating_expenses_latest'])}."
        ),
        "total_assets": (
            f"Total assets are {format_currency(data['total_assets_latest'])} (latest year)."
        ),
        "revenue_growth": (
            f"Revenue has grown by {data['revenue_change_pct']}% year-over-year, "
            f"from {format_currency(data['total_revenue_prior'])} to {format_currency(data['total_revenue_latest'])}."
        ),
    }


# Predefined query variations mapped to response keys
QUERY_MAPPINGS = [
    ("what is the total revenue", "total_revenue"),
    ("total revenue", "total_revenue"),
    ("how has net income changed over the last year", "net_income_change"),
    ("net income change", "net_income_change"),
    ("what are the operating expenses", "operating_expenses"),
    ("operating expenses", "operating_expenses"),
    ("what are total assets", "total_assets"),
    ("total assets", "total_assets"),
    ("how has revenue grown", "revenue_growth"),
    ("revenue growth", "revenue_growth"),
]

FALLBACK_MESSAGE = (
    "Sorry, I can only provide information on predefined queries. "
    "Try: 'What is the total revenue?', 'How has net income changed over the last year?', "
    "'What are the operating expenses?', 'What are total assets?', 'How has revenue grown?'"
)


def simple_chatbot(user_query: str) -> str:
    """
    Match user input to predefined queries and return the corresponding response.
    """
    if not user_query or not user_query.strip():
        return "Please enter a question about the financial data."
    normalized = user_query.strip().lower()
    # Remove trailing punctuation for matching
    normalized = normalized.rstrip("?.!")
    responses = build_responses()
    for pattern, key in QUERY_MAPPINGS:
        if pattern in normalized or normalized in pattern:
            return responses[key]
    return FALLBACK_MESSAGE


def run_cli():
    """Command-line interaction loop."""
    print("Financial Analysis Chatbot")
    print("Ask a predefined question (or 'quit' to exit).\n")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye.")
            break
        reply = simple_chatbot(user_input)
        print(f"Chatbot: {reply}\n")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--query":
        # Single query from command line
        q = " ".join(sys.argv[2:])
        print(simple_chatbot(q))
    else:
        run_cli()
