import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double, c_int, POINTER

# Load the shared library
formula = CDLL('./formula.so')

# Number of points
n = 400
arr_type = c_double * n

# Prepare arrays
x_ellipse = arr_type()
y_ellipse = arr_type()
x_circle1 = arr_type()
y_circle1 = arr_type()
x_circle2 = arr_type()
y_circle2 = arr_type()

# Call C functions
formula.generate_ellipse(c_double(2), c_double(1), c_int(n), x_ellipse, y_ellipse)
formula.generate_circle(c_double(0), c_double(2), c_double(2), c_int(n), x_circle1, y_circle1)
formula.generate_circle(c_double(1), c_double(0), c_double(1), c_int(n), x_circle2, y_circle2)

# Convert to numpy arrays
x_ellipse = np.array(x_ellipse)
y_ellipse = np.array(y_ellipse)
x_circle1 = np.array(x_circle1)
y_circle1 = np.array(y_circle1)
x_circle2 = np.array(x_circle2)
y_circle2 = np.array(y_circle2)

# Plotting
plt.figure(figsize=(10,10))
plt.plot(x_ellipse, y_ellipse, 'g', linewidth=2, label=r'Ellipse: $4x^2 + y^2 = 4$')
plt.plot(x_circle1, y_circle1, 'b', linewidth=2, label=r'Circle: $C_1$ (0,2), r=2')
plt.plot(x_circle2, y_circle2, 'r', linewidth=2, label=r'Circle: $C_2$ (1,0), r=1')

# Mark centers
plt.plot(0, 2, 'bo')
plt.text(0.1, 2.1, '$C_1$(0,2)', color='blue', fontsize=12)
plt.plot(1, 0, 'ro')
plt.text(1.1, 0.1, '$C_2$(1,0)', color='red', fontsize=12)

# Axes and formatting
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Ellipse and Circles with Centers')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
