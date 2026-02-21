import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# a) Dice roll simulation
dice = np.random.randint(1, 7, 100)

# b) Poisson distribution
poisson = np.random.poisson(3, 1000)

# c) Histogram
plt.figure()

plt.hist(dice, bins=6)
plt.title("Dice Roll Distribution")
plt.show()

plt.figure()

plt.hist(poisson, bins=20)
plt.title("Poisson Distribution")
plt.show()