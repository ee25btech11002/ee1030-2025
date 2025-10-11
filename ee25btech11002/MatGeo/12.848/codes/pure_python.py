import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define surface: x^2 + y^2 + z = 9  →  z = 9 - x^2 - y^2
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z_surface = 9 - X**2 - Y**2

# Define tangent plane: 2x + 4y + z = 14 → z = 14 - 2x - 4y
Z_plane = 14 - 2*X - 4*Y

# Point of contact
px, py, pz = 1, 2, 4

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
ax.plot_surface(X, Y, Z_surface, alpha=0.5)

# Plot tangent plane
ax.plot_surface(X, Y, Z_plane, alpha=0.5)

# Plot point of contact
ax.scatter(px, py, pz, s=60)


ax.text2D(
    0.85, 0.90,
    "Surface (blue):  $x^2 + y^2 + z = 9$\n"
    "Tangent Plane (orange):  $2x + 4y + z = 14$",
    transform=ax.transAxes,
    fontsize=10,
    bbox=dict(boxstyle="round", alpha=0.5)
)
#  Label for point of contact
ax.text(px, py, pz + 1, "Point (1,2,4)", fontsize=10)

# Labels
ax.set_xlabel('X - axis')
ax.set_ylabel('Y - axis')
ax.set_zlabel('Z - axis')
ax.set_title('Surface $x^2 + y^2 + z = 9$ and Tangent Plane $2x + 4y + z = 14$')
plt.legend(loc='upper right')
# Show
plt.show()