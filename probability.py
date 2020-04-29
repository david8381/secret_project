import numpy as np
def get_probabilities(N):
    S = 10000000
    C = np.random.randint(0,2,N*S)
    C = C.reshape(-1,N)
    C = C.sum(axis=1)
    unique, counts = np.unique(C, return_counts=True)
    probabilities = counts / S
    return probabilities
