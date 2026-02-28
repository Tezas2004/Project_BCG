"""
Tests for the Financial Analysis Chatbot.
Run: python -m pytest test_chatbot.py -v
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chatbot import simple_chatbot


def test_total_revenue():
    r = simple_chatbot("What is the total revenue?")
    assert "revenue" in r.lower()
    assert "million" in r.lower() or "$" in r


def test_net_income_change():
    r = simple_chatbot("How has net income changed over the last year?")
    assert "net income" in r.lower() or "increased" in r.lower() or "decreased" in r.lower()


def test_operating_expenses():
    r = simple_chatbot("What are the operating expenses?")
    assert "operating" in r.lower() or "expenses" in r.lower()


def test_total_assets():
    r = simple_chatbot("What are total assets?")
    assert "assets" in r.lower()


def test_revenue_growth():
    r = simple_chatbot("How has revenue grown?")
    assert "revenue" in r.lower() or "grown" in r.lower() or "%" in r


def test_fallback():
    r = simple_chatbot("What is the stock price?")
    assert "sorry" in r.lower() or "predefined" in r.lower()


def test_empty_input():
    r = simple_chatbot("")
    assert "please" in r.lower() or len(r) > 0
