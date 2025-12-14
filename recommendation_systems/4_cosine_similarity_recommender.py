from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

ratings = pd.DataFrame({
    "A": [5, 4, 0],
    "B": [4, 0, 3],
    "C": [0, 5, 4]
})

similarity = cosine_similarity(ratings)
print(similarity)
