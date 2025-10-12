import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, Structure, c_double, c_int, POINTER

# Load shared library (after compiling)
lib = CDLL("./formula.so")

# Define Vec2 struct in Python
class Vec2(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# Function prototypes
lib.compute_P_points.argtypes = [c_double, c_double, POINTER(Vec2), POINTER(Vec2)]
lib.tangent_normal_at.argtypes = [c_double, c_double, Vec2, POINTER(Vec2)]
lib.foot_from_origin_to_line.argtypes = [Vec2, c_double, POINTER(Vec2)]
lib.area_triangle.argtypes = [Vec2, Vec2, Vec2]
lib.area_triangle.restype = c_double
lib.tangent_line_points.argtypes = [Vec2, Vec2, c_double, c_int,
                                   POINTER(c_double), POINTER(c_double)]

# Parameters
a, b = 3.0, 2.0
npts = 200
span = 6.0

# Create needed structs
P_plus, P_minus = Vec2(), Vec2()
lib.compute_P_points(a, b, P_plus, P_minus)

# Tangent normals
n1, n2 = Vec2(), Vec2()
lib.tangent_normal_at(a, b, P_plus, n1)
lib.tangent_normal_at(a, b, P_minus, n2)

# Feet from origin
N1, N2 = Vec2(), Vec2()
lib.foot_from_origin_to_line(n1, 1.0, N1)
lib.foot_from_origin_to_line(n2, 1.0, N2)

# Area check (optional)
O = Vec2(0.0, 0.0)
area1 = lib.area_triangle(P_plus, O, N1)
area2 = lib.area_triangle(P_minus, O, N2)

# Tangent line points
x1 = (c_double * npts)()
y1 = (c_double * npts)()
x2 = (c_double * npts)()
y2 = (c_double * npts)()
lib.tangent_line_points(n1, N1, span, npts, x1, y1)
lib.tangent_line_points(n2, N2, span, npts, x2, y2)

# Convert arrays to NumPy
tx1, ty1 = np.array(x1), np.array(y1)
tx2, ty2 = np.array(x2), np.array(y2)

# Ellipse points
theta = np.linspace(0, 2*np.pi, 600)
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)

# ---------- Plot ----------
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x_ellipse, y_ellipse, label='Ellipse', linewidth=2)
ax.scatter([O.x], [O.y], color='k', s=40, label='O (origin)')
ax.scatter([P_plus.x, P_minus.x], [P_plus.y, P_minus.y], color='tab:blue', s=80, label='P (optimal)')
ax.scatter([N1.x, N2.x], [N1.y, N2.y], marker='x', s=90, color='tab:orange', label='N (foot)')
ax.plot(tx1, ty1, '--', linewidth=1.2, label='Tangent at P')
ax.plot(tx2, ty2, '--', linewidth=1.2)

# Triangles
ax.fill([O.x, P_plus.x, N1.x], [O.y, P_plus.y, N1.y], alpha=0.25)
ax.fill([O.x, P_minus.x, N2.x], [O.y, P_minus.y, N2.y], alpha=0.25)

# Labels
ax.text(O.x+0.1, O.y+0.1, f"O({O.x:.2f},{O.y:.2f})", fontsize=11)
ax.text(P_plus.x+0.1, P_plus.y+0.1, f"P₁({P_plus.x:.2f},{P_plus.y:.2f})", fontsize=11)
ax.text(P_minus.x+0.1, P_minus.y+0.1, f"P₂({P_minus.x:.2f},{P_minus.y:.2f})", fontsize=11)
ax.text(N1.x+0.1, N1.y+0.1, f"N₁({N1.x:.2f},{N1.y:.2f})", fontsize=11)
ax.text(N2.x+0.1, N2.y+0.1, f"N₂({N2.x:.2f},{N2.y:.2f})", fontsize=11)

ax.set_aspect('equal', 'box')
ax.set_xlim(-2*a, 2*a)
ax.set_ylim(-2*b, 2*b)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Ellipse and triangles PON (from C via .so)')
ax.grid(True)
ax.legend(loc='upper left')

plt.show()
