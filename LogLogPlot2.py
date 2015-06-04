import numpy as np
import matplotlib.pyplot as plt

#plt.subplots_adjust(hspace=.4)
t = np.arange(0.01, 20.0, 0.01)

# log x and y axis
#plt.loglog(t, 20*np.exp(-t/10.0), basex=10)
plt.loglog([1,2,3,10,12],[.5, 5, 50, 500, 520], 'ro', basex=10)  # 'ro' can be removed for default blue line
plt.grid(True)
plt.xlabel('In-Degree')
plt.ylabel('Normalized')
plt.title('loglog base 10 on X & Y axis')

plt.show()