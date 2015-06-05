import numpy as np
import matplotlib.pyplot as plt

#plt.subplots_adjust(hspace=.4)
#t = np.arange(0.01, 20.0, 0.01)

# log x and y axis
#plt.loglog(t, 20*np.exp(-t/10.0), basex=10)
#plt.locator_params(axis='y', nbins=4)
plt.loglog([1,2,3,10,12],[.5, 5, 50, 500, 520], 'ro', basex=10)  # 'ro' can be removed for default blue line
#plt.grid(True)
plt.grid(b=True, which='major', color='b', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlabel('In-Degree (Log base 10)')
plt.ylabel('Normalized (Log base 10)')
plt.title('Citation Graph In-Degree Distribution')

plt.show()