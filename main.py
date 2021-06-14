import matplotlib.pyplot as plt
import numpy as np

xaxis = np.array([2, 8])
yaxis = np.array([2, 8])

plt.plot(xaxis, yaxis)
plt.show()

xaxis = np.array([2, 12, 3, 9])

plt.plot(xaxis, marker="o", linestyle="--")  # - = single line

plt.show()

x = [2, 3, 7, 29, 8, 5, 13, 11, 22, 33]

y = [4, 7, 55, 43, 2, 4, 11, 22, 33, 44]

plt.scatter(x, y)

plt.show()
