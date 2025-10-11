import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes

# Load the shared library
lib = ctypes.CDLL('./formula.so')

# Array size
n = 100
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# Create empty Z arrays
Z_surface = np.zeros((n, n), dtype=np.float64)
Z_plane = np.zeros((n, n), dtype=np.float64)

# Convert to C pointers
X_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
Y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
Z_surface_ptr = Z_surface.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
Z_plane_ptr = Z_plane.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Define the functions argument types
lib.compute_surface.argtypes = [ctypes.c_int,
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.POINTER(ctypes.c_double))]
lib.compute_plane.argtypes = [ctypes.c_int,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.POINTER(ctypes.c_double))]

# Allocate row pointers for C 2D array
Z_surface_c = (ctypes.POINTER(ctypes.c_double) * n)()
Z_plane_c = (ctypes.POINTER(ctypes.c_double) * n)()
for i in range(n):
    Z_surface_c[i] = Z_surface[i].ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    Z_plane_c[i] = Z_plane[i].ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call C functions
lib.compute_surface(n, X_ptr, Y_ptr, Z_surface_c)
lib.compute_plane(n, X_ptr, Y_ptr, Z_plane_c)

# Point of contact
px, py, pz = 1, 2, 4

# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, Z_surface, alpha=0.5)
ax.plot_surface(X, Y, Z_plane, alpha=0.5)
ax.scatter(px, py, pz, s=60)

ax.text2D(0.85, 0.90,
          "Surface (blue):  $x^2 + y^2 + z = 9$\n"
          "Tangent Plane (orange):  $2x + 4y + z = 14$",
          transform=ax.transAxes,
          fontsize=10,
          bbox=dict(boxstyle="round", alpha=0.5))

ax.text(px, py, pz + 1, "Point (1,2,4)", fontsize=10)
ax.set_xlabel('X - axis')
ax.set_ylabel('Y - axis')
ax.set_zlabel('Z - axis')
ax.set_title('Surface $x^2 + y^2 + z = 9$ and Tangent Plane $2x + 4y + z = 14$')
plt.show()