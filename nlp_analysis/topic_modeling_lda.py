from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "machine learning algorithms",
    "deep learning neural networks",
    "data science analytics"
]

vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(docs)

lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(X)

print("Topics learned")
