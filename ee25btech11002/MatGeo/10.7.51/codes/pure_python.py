import numpy as np
import matplotlib.pyplot as plt

# ---------- Parameters ----------
a = 3.0   # change as needed
b = 2.0

# Ellipse matrix V and J
V = np.array([[1.0/a**2, 0.0],
              [0.0,       1.0/b**2]])
J = np.array([[0.0, 1.0],
              [-1.0, 0.0]])

# ---------- Optimal points P (derived) ----------
lam = 1.0 / np.sqrt(a**2 + b**2)
P_plus = lam * np.array([a**2, b**2])
P_minus = -P_plus

def tangent_normal_at(P):
    n = V @ P
    return n

def foot_from_origin_to_line(n, c=1.0):
    denom = n.dot(n)
    return (c / denom) * n

def tangent_line_points(n, center_point, span=5.0, npts=200):
    t = J @ n
    s = np.linspace(-span, span, npts)
    pts = center_point.reshape(2,1) + np.outer(t, s)
    return pts[0,:], pts[1,:]

def area_triangle(P, O, N):
    cross = P[0]*N[1] - P[1]*N[0]
    return 0.5 * abs(cross)

# Origin
O = np.array([0.0, 0.0])

# Compute normals and feet
n1 = tangent_normal_at(P_plus)
N1 = foot_from_origin_to_line(n1, c=1.0)

n2 = tangent_normal_at(P_minus)
N2 = foot_from_origin_to_line(n2, c=1.0)

# Areas
area1 = area_triangle(P_plus, O, N1)
area2 = area_triangle(P_minus, O, N2)

# ---------- Ellipse points for plotting ----------
theta = np.linspace(0, 2*np.pi, 600)
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)

# ---------- Plotting ----------
fig, ax = plt.subplots(figsize=(8,8))

# Ellipse
ax.plot(x_ellipse, y_ellipse, label='Ellipse', linewidth=2)

# Points O, P, N
ax.scatter([O[0]], [O[1]], color='k', s=40, label='O (origin)')
ax.scatter([P_plus[0]], [P_plus[1]], color='tab:blue', s=80, label='P (optimal)')
ax.scatter([P_minus[0]], [P_minus[1]], color='tab:blue', s=80)
ax.scatter([N1[0]], [N1[1]], marker='x', s=90, color='tab:orange', label='N (foot)')
ax.scatter([N2[0]], [N2[1]], marker='x', s=90, color='tab:orange')

# Tangent lines
tx1, ty1 = tangent_line_points(n1, N1, span=6.0)
ax.plot(tx1, ty1, linestyle='--', linewidth=1.2, label='Tangent at P')
tx2, ty2 = tangent_line_points(n2, N2, span=6.0)
ax.plot(tx2, ty2, linestyle='--', linewidth=1.2)

# Triangles P-O-N (filled lightly)
ax.fill([O[0], P_plus[0], N1[0]],
        [O[1], P_plus[1], N1[1]],
        alpha=0.25, edgecolor='none')
ax.fill([O[0], P_minus[0], N2[0]],
        [O[1], P_minus[1], N2[1]],
        alpha=0.25, edgecolor='none')

# ✅ Add coordinate labels (rounded to 2 decimals)
ax.text(O[0] + 0.1, O[1] + 0.1, f"O ({O[0]:.2f}, {O[1]:.2f})", fontsize=11)
ax.text(P_plus[0] + 0.1, P_plus[1] + 0.1, f"P₁ ({P_plus[0]:.2f}, {P_plus[1]:.2f})", fontsize=11)
ax.text(P_minus[0] + 0.1, P_minus[1] + 0.1, f"P₂ ({P_minus[0]:.2f}, {P_minus[1]:.2f})", fontsize=11)
ax.text(N1[0] + 0.1, N1[1] + 0.1, f"N₁ ({N1[0]:.2f}, {N1[1]:.2f})", fontsize=11)
ax.text(N2[0] + 0.1, N2[1] + 0.1, f"N₂ ({N2[0]:.2f}, {N2[1]:.2f})", fontsize=11)

# Styling (keep same as before)
ax.set_aspect('equal', 'box')

# ✅ Increase viewing window so ellipse appears large
scale_factor = 2.0
ax.set_xlim(-scale_factor * a, scale_factor * a)
ax.set_ylim(-scale_factor * b, scale_factor * b)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Ellipse and triangles PON where a=3,b=2')
ax.grid(True)
ax.legend(loc='upper left')

plt.show()
