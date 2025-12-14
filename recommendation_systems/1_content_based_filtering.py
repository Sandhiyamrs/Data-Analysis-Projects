import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

items = pd.DataFrame({
    "item": ["Movie A", "Movie B", "Movie C"],
    "action": [1, 0, 1],
    "romance": [0, 1, 1]
})

similarity = cosine_similarity(items.iloc[:, 1:])
sim_df = pd.DataFrame(similarity, index=items.item, columns=items.item)
print(sim_df)
