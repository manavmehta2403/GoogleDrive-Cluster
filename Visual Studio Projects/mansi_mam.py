import matplotlib.pyplot as plt
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


plt.plot(current[0],Z,"--y*")
#plt.plot(current,"c+:")
#plt.xlim(-200, 200)
#plt.ylim(-10,6)
plt.show()

print(current)
print(conc)
