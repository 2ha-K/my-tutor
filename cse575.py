import numpy as np

# Training data
X = np.array([
    [0, 0], [1, 0], [2, 0],
    [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [100, 1],
    [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [100, 2],
    [3, 3], [4, 3], [5, 3], [100, 3]
], dtype=float)

# C1: second coordinate <= 2
# C2: otherwise
C1 = X[X[:, 1] <= 2]
C2 = X[X[:, 1] > 2]

# Mean vectors
m1 = np.mean(C1, axis=0)
m2 = np.mean(C2, axis=0)

# Within-class scatter matrices
S1 = np.zeros((2, 2))
for x in C1:
    d = (x - m1).reshape(2, 1)
    S1 += d @ d.T

S2 = np.zeros((2, 2))
for x in C2:
    d = (x - m2).reshape(2, 1)
    S2 += d @ d.T

# Within-class scatter matrix
Sw = S1 + S2

# Fisher's Linear Discriminant
w = np.linalg.inv(Sw) @ (m2 - m1)

print("m1 =")
print(m1)

print("\nm2 =")
print(m2)

print("\nS1 =")
print(S1)

print("\nS2 =")
print(S2)

print("\nSw =")
print(Sw)

print("\nw =")
print(w)