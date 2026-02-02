from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text, top_n=5):
    vectorizer = CountVectorizer(stop_words="english")
    X = vectorizer.fit_transform([text])
    words = vectorizer.get_feature_names_out()
    counts = X.toarray().sum(axis=0)

    return sorted(
        zip(words, counts),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]

if __name__ == "__main__":
    print(extract_keywords("data science data analytics machine learning data"))
