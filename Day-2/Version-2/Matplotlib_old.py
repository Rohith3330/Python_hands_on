import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
plt.hist(data)
plt.title("Histogram without density (older version)")
# plt.show()
plt.savefig("Matplotlib_old.png")