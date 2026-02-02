from textblob import TextBlob

def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    return "Neutral"

if __name__ == "__main__":
    print(detect_emotion("I love building data projects"))
