import matplotlib.pyplot as plt
import numpy as np
c=np.random.normal(170,10,300)
print(c.size)
print(c)
plt.hist(c)
plt.show()