import numpy as np
import matplotlib.pyplot as plt

n = 10 # Number of species
trees = np.array([1012, 501, 486, 276, 150, 784, 382, 843, 373, 193])
relative_trees = trees/(np.sum(trees))

# Naive similarity matrix
Z1 = np.eye(10)

# Alternate similarity matrix
Z2 = np.zeros((10, 10))

# Edit similarity coefficents
for i in range(n):
    for j in range(n):
        if i == j:
            Z2[i, j] = 1
        elif (i <= 4 and j <= 4 and i != j):
            Z2[i, j] = 0.75
        elif (i <= 4 and j >= 4 and i != j):
            Z2[i, j] = 0.25
        elif (i >= 4 and j <= 4 and i != j):
            Z2[i, j] = 0.75
        elif (i >= 4 and j >= 4 and i != j):
            Z2[i, j] = 0.25
        
        
# Function to calculate the Hill number of order q for a similarity matrix Z
# p should be a numpy array
def Hill_Number_Similarity(q, Z, p):
    Zp = np.matmul(Z, p)
    
    if q == 0:
        return np.sum(p/Zp)
    elif q == 1:
        return np.prod(Zp**(-p))   
    else:
        c = 1/(1-q)
        return np.sum(p*(Zp**(q-1)))**c

qs = np.linspace(0, 10, 10000) # q range
D1 = []
D2 = []
# calculate Hill numbers for different q
for q in qs:
    D1.append(Hill_Number_Similarity(q, Z2, relative_trees))
    D2.append(Hill_Number_Similarity(q, Z1, relative_trees))

D1 = np.round(np.array(D1), 4)
D2 = np.round(np.array(D2), 4)

# label plots
plt.plot(qs, D1, label="Similarity")
plt.plot(qs, D2, label="No similarity")
plt.xlabel(r"$q$")
plt.ylabel(r"$D^Z_q(\mathbf{p})$")
plt.grid()
plt.legend()
plt.show()
    
