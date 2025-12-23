import numpy as np

R = np.array([
    [5,4,0],
    [3,0,2],
    [0,1,4]
])

U, S, Vt = np.linalg.svd(R)
reconstructed = np.dot(U, np.dot(np.diag(S), Vt))
print(reconstructed)
