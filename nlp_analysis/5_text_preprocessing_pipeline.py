import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return tokens

print(preprocess("NLP is AMAZING! This is a sample text."))
