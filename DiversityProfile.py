import numpy as np
import matplotlib.pyplot as plt

abundances = np.array([1/3, 1/3, 1/3, 0])
relative_abundance = abundances/np.sum(abundances)

def Hill_Number(q, p):
    support_p = p[p != 0]
    if q == 0:
        return len(support_p)
    elif q == 1:
        return np.prod(support_p**(-1*support_p))   
    else:
        c = 1/(1-q)
        return np.sum(support_p**q)**c

qs = np.linspace(0, 10, 1000) # q range
D = []
for q in qs:
    D.append(Hill_Number(q, relative_abundance))

D = np.round(np.array(D), 4)

plt.plot(qs, D)
plt.xlabel(r"$q$")
plt.ylabel(r"$D_q(\mathbf{p})$")
plt.grid()
plt.show()
    
