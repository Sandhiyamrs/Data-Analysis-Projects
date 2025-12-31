from sklearn.feature_extraction.text import CountVectorizer

text = ["data science is fun and data is powerful"]
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(text)

print(vectorizer.get_feature_names_out())
