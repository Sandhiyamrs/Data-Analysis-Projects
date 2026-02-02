from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = ["data science", "machine learning", "deep learning"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

similarity = cosine_similarity(X)
print(similarity)
