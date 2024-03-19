import matplotlib.pyplot as plt
import numpy as np

populations = np.array([[0.25, 0.25, 0.25, 0.25],
					[0.50, 0.30, 0.20, 0.10],
					[1, 0, 0, 0]])


start = populations[0]
label = [0.5, 1, 1.5, 2]

diff = (populations[1]-populations[0])/25

for i in range(24):
    # Mention x and y limits to define their range
    
	
    plt.xlim(0, 3)
    plt.ylim(0, 1)
    
    # Plotting graph
    plt.bar(label, start, width=0.45)
    start += diff
    plt.savefig(f'anim/foo{i}.png')

plt.show()
   


plt.savefig('foo.png')