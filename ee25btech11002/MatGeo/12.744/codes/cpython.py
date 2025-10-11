import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double

# Load shared library
lib = CDLL("./formula.so")

# Define Python wrappers for C functions
lib.line_L1.restype = c_double
lib.line_L1.argtypes = [c_double]

lib.line_L2.restype = c_double
lib.line_L2.argtypes = [c_double]

lib.line_L3.restype = c_double
lib.line_L3.argtypes = [c_double]

lib.line_L4.restype = c_double
lib.line_L4.argtypes = [c_double]

# x values for plotting
x = np.linspace(-5, 5, 400)

# Compute y values by calling C functions
y1 = np.array([lib.line_L1(xi) for xi in x])
y2 = np.array([lib.line_L2(xi) for xi in x])
y3 = np.array([lib.line_L3(xi) for xi in x])
y4 = np.array([lib.line_L4(xi) for xi in x])

# Plot each line
plt.plot(x, y1, label='L1: 2x - 3y = 5', color='blue')
plt.plot(x, y2, label='L2: 3x + 2y = 8', color='red')
plt.plot(x, y3, label='L3: 4x - 6y = 5', color='green')
plt.plot(x, y4, label='L4: 6x - 9y = 6', color='orange')

# Highlight parallel and perpendicular
plt.text(1, y1[240]+0.5, 'L1 || L3', color='green')
plt.text(2, y2[260], 'L2 $\perp$ L4', color='red')

# Axes and grid
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.grid(True)
plt.legend()
plt.title("Visualization of Lines L1, L2, L3, L4")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
