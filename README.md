# AI Sentiment Analyzer

A beginner-friendly Python AI project that analyzes the sentiment of a sentence
and classifies it as Positive, Negative, or Neutral using Natural Language Processing (NLP).

---

## 🚀 Features
- Analyzes text sentiment
- Classifies sentiment as:
  - Positive
  - Negative
  - Neutral
- Simple command-line interface
- Beginner-friendly AI project

---

## 🧠 How It Works
This project uses the **TextBlob** NLP library.
TextBlob calculates a **polarity score**:
- Polarity > 0 → Positive
- Polarity < 0 → Negative
- Polarity = 0 → Neutral

---

## 🛠 Tech Stack
- Python
- TextBlob (NLP)

---

## ▶️ How to Run the Project

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
