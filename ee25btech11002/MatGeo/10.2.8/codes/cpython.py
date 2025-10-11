import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL('./formula.so')
# Declare argument and return types for each C function
lib.compute_center.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

lib.compute_radius.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double]
lib.compute_radius.restype = ctypes.c_double

lib.generate_circle_points.argtypes = [
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]

lib.compute_edge_point.argtypes = [
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double)
]

# --- Step 3: Set up input values ---
u = (ctypes.c_double * 2)(-7, -5)
f = ctypes.c_double(-151)
P = np.array([2, 7], dtype=np.float64)

# Compute center using C
C = (ctypes.c_double * 2)()
lib.compute_center(u, C)

# Compute radius using C
r = lib.compute_radius(u, f)

# Generate circle points using C
N = 400
x_arr = (ctypes.c_double * N)()
y_arr = (ctypes.c_double * N)()
lib.generate_circle_points(C, r, x_arr, y_arr, N)

# Convert circle arrays to NumPy for plotting
x_circ = np.array(list(x_arr))
y_circ = np.array(list(y_arr))

# Compute edge point using C
edge = (ctypes.c_double * 2)()
P_c = (ctypes.c_double * 2)(*P)  # Convert NumPy -> C array
lib.compute_edge_point(C, P_c, r, edge)

# --- Step 4: Plot EXACTLY like your specified plot ---
plt.plot(x_circ, y_circ, label='Circle: $x^2+y^2-14x-10y-151=0$', color='b')
plt.scatter(C[0], C[1], color='red')
plt.scatter(P[0], P[1], color='green')
plt.plot([C[0], P[0]], [C[1], P[1]], 'k--', label='Distance $CP$ = $15 - \\sqrt{29}$')
plt.text(C[0]+0.5, C[1]-1, f'C({C[0]:.0f},{C[1]:.0f})', fontsize=10)
plt.text(P[0]-1.5, P[1]+0.5, f'P({P[0]:.0f},{P[1]:.0f})', fontsize=10)
plt.text(P[0]+2.3, P[1], '$15 - \\sqrt{29}$', fontsize=10)

# Plot radius in same direction
plt.plot([C[0], edge[0]], [C[1], edge[1]], 'r:', label='Radius = 15')

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.title('Shortest Distance from Point (2,7) to Circle')
plt.legend(loc='upper right')
plt.show()