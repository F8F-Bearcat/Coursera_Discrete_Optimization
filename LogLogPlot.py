import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

x = np.linspace(1, 4, 1000)

y = x**3

fig, ax = plt.subplots()

ax.loglog(x,y, basex=np.e, basey=np.e)

def ticks(y, pos):
    return r'$e^{:.0f}$'.format(np.log(y))

ax.xaxis.set_major_formatter(mtick.FuncFormatter(ticks))
ax.yaxis.set_major_formatter(mtick.FuncFormatter(ticks))

plt.show()