import numpy as np
import matplotlib.pyplot as plt

def Sigmoid(x):
    return x * (1.0 / (1 + np.exp(-x)))

sigmoid_input = np.arange(-10, 10, 0.1)
sigmoid_output = Sigmoid(sigmoid_input)
plt.plot(sigmoid_input, sigmoid_output)
plt.xlabel("sigmoid_input")
plt.ylabel("sigmoid_output")
plt.show()