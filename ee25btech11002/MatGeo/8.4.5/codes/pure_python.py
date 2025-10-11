import numpy as np
import matplotlib.pyplot as plt

# Ellipse: 4x^2 + y^2 = 4  ->  (x^2/1^2) + (y^2/2^2) = 1
a = 2   # semi-major axis along y
b = 1   # semi-minor axis along x

theta = np.linspace(0, 2*np.pi, 400)
x_ellipse = b * np.cos(theta)
y_ellipse = a * np.sin(theta)

# Circle 1: center (0,2), radius 2
r1 = 2
center1 = (0, 2)
x_circle1 = center1[0] + r1 * np.cos(theta)
y_circle1 = center1[1] + r1 * np.sin(theta)

# Circle 2: center (1,0), radius 1
r2 = 1
center2 = (1, 0)
x_circle2 = center2[0] + r2 * np.cos(theta)
y_circle2 = center2[1] + r2 * np.sin(theta)

# Plotting
plt.figure(figsize=(10,10))
plt.plot(x_ellipse, y_ellipse, 'g', linewidth=2, label=r'Ellipse: $4x^2 + y^2 = 4$')
plt.plot(x_circle1, y_circle1, 'b', linewidth=2, label=r'Circle: $C_1$ (0,2), r=2')
plt.plot(x_circle2, y_circle2, 'r', linewidth=2, label=r'Circle: $C_2$ (1,0), r=1')

# Mark centers
plt.plot(center1[0], center1[1], 'bo')  # blue dot for $C_1$
plt.text(center1[0]+0.1, center1[1]+0.1, '$C_1$(0,2)', color='blue', fontsize=12)

plt.plot(center2[0], center2[1], 'ro')  # red dot for $C_2$
plt.text(center2[0]+0.1, center2[1]+0.1, '$C_2$(1,0)', color='red', fontsize=12)

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
