from textblob import TextBlob

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

print("AI Sentiment Analyzer")
text = input("Enter a sentence: ")
print("Sentiment:", analyze_sentiment(text))

