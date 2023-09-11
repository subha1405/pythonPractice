import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3])
y=np.array([3,8,5])

a=np.array([0,4,5])
b=np.array([6,5,3])
plt.title("sample")
plt.xlabel("x")
plt.ylabel("y")
# plt.plot(x,y)

# o for rings
# plt.plot(x,y,'o')

# * for stars
# plt.plot(x,y,'*')

# :for dotted lines marker/line/colour
# plt.plot(x,y,'o-.r')
# plt.plot(a,b,'*--g')

# Subplot
# plt.subplot(2,1,1)
# plt.title("a")
# plt.plot(x,y)
# plt.subplot(2,1,2)
# plt.title("b")
# plt.plot(x,y,'o')

# Scatter plot
plt.scatter(x,y)
plt.scatter(a,b)
plt.colorbar()
plt.bar(x,y)
plt.show()
