import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100, dtype=np.float64) 


fig, ax = plt.subplots()
ax.plot(x *  np.sin(0.2 * x), x * np.cos(0.2 * x))

ax.set_title('graphs')
ax.set_xlabel('the x axis')
ax.set_ylabel('the y axis')

# set limits via tuple
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))


fig.savefig('out.png')

# plt.show()
