from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

docs = ["I love data science", "Data science is amazing"]
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(docs)

print(cosine_similarity(X))
