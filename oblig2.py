import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (np.exp(-x/4))*np.arctan(x)

def g(x):
    return np.arctan(x) - 4/(x**2+1)

x = np.linspace(0, 5, 500)

x_topp = 1.6907
y_topp = f(x_topp)

#plotter f(x)
plt.plot(x, f(x))
plt.title("f(x)")

#plotter punkt toppunkt
plt.scatter(x_topp, y_topp)

#x og y streker 
plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.show()

# plotte den deriverte = 0
plt.plot(x, g(x))
plt.scatter(x_topp, 0)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.show()



