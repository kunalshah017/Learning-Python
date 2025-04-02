from matplotlib import pyplot as plt
import numpy as np

marks = np.random.randint(50, 100, 30)

plt.hist(marks, bins= 5)

plt.show()