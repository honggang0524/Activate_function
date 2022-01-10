import numpy as np
import matplotlib.pyplot as plt

def Hard_wish(x):
    beta = 10
    return (x * (1.0 / np.exp(-beta * x)))

Hard_wish_input = np.arange(-10, 10, 0.1)
Hard_wish_ouput = Hard_wish(Hard_wish_input)

plt.plot(Hard_wish_input, Hard_wish_ouput)
plt.xlabel("Hard_wish_input")
plt.ylabel("Hard_wish_output")
plt.show()