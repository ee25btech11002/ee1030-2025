import numpy as np
import matplotlib.pyplot as plt

# Define lines as functions: y = f(x)
def line_L1(x):
    return (2*x - 5)/3  # from 2x - 3y = 5 → y = (2x - 5)/3

def line_L2(x):
    return (8 - 3*x)/2  # from 3x + 2y = 8 → y = (8 - 3x)/2

def line_L3(x):
    return (4*x - 5)/6  # from 4x - 6y = 5 → y = (4x - 5)/6

def line_L4(x):
    return (6*x - 6)/9  # from 6x - 9y = 6 → y = (6x - 6)/9

# x values for plotting
x = np.linspace(-5, 5, 400)

# Plot each line
plt.plot(x, line_L1(x), label='L1: 2x - 3y = 5', color='blue')
plt.plot(x, line_L2(x), label='L2: 3x + 2y = 8', color='red')
plt.plot(x, line_L3(x), label='L3: 4x - 6y = 5', color='green')
plt.plot(x, line_L4(x), label='L4: 6x - 9y = 6', color='orange')

# Highlight parallel and perpendicular
plt.text(1, line_L1(1)+0.5, 'L1 || L3', color='green')
plt.text(2, line_L2(1.7)+0, 'L2 $\perp$ L4', color='red')

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
