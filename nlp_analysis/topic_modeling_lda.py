"""
LDA topic modeling pipeline (text -> LDA).
Requires: gensim, nltk, pandas
"""
import pandas as pd
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def preprocess(texts):
    stop = set(stopwords.words('english'))
    tokenized = [[w for w in word_tokenize(doc.lower()) if w.isalpha() and w not in stop] for doc in texts]
    return tokenized

def run_lda(docs, num_topics=5):
    texts = preprocess(docs)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = gensim.models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)
    for i in range(num_topics):
        print(f"Topic {i}:", lda.print_topic(i))
    return lda

if __name__ == "__main__":
    sample_docs = ["I love data science and machine learning", "Python is great for NLP tasks", "Deep learning enables advanced models"]
    run_lda(sample_docs, num_topics=2)
