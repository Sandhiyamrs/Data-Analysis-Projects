import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z ]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in stopwords.words("english")]
    return tokens

if __name__ == "__main__":
    print(preprocess("This is a Sample TEXT for NLP Processing!"))
