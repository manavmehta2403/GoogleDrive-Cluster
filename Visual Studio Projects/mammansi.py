import matplotlib.pyplot as plt
import numpy as np
import math
PZqC_in=0.75
Z=0.035
conc = [0, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000] 
a=math.exp(-Z)
current = []
I = 0
for i in range (0,len(conc)):
    I=PZqC_in*Z*(1-conc[i]*a)/(1-a)
    current.append(I)
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-5,5,100)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(conc,current, '-r', label='y=2x+1')
##plt.plot(current, Z,'-.g', label='y=2x-1')
##plt.plot(current, Z,':b', label='y=2x+3')
##plt.plot(current, Z,'--m', label='y=2x-3')
plt.legend(loc='upper left')
plt.show()
