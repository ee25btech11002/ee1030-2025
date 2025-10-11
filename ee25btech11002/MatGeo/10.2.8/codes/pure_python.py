import numpy as np
import matplotlib.pyplot as plt

# Circle parameters from the equation x^2 + y^2 - 14x - 10y - 151 = 0
u = np.array([-7, -5])    # coefficients of x and y
f = -151

# Center and radius
C = -u                    # Center (7, 5)
r = np.sqrt(u @ u - f)    # Radius = sqrt(74 - (-151)) = 15

# Given point
P = np.array([2, 7])

# Create circle points
theta = np.linspace(0, 2*np.pi, 400)
x_circ = C[0] + r * np.cos(theta)
y_circ = C[1] + r * np.sin(theta)

# Plot circle
plt.plot(x_circ, y_circ, label='Circle: $x^2+y^2-14x-10y-151=0$', color='b')

# Plot center and point
plt.scatter(*C, color='red')
plt.scatter(*P, color='green')

# Draw line from center to point
plt.plot([C[0], P[0]], [C[1], P[1]], 'k--', label='Distance $CP$ = $15 - \sqrt{29}$')

# Annotate
plt.text(C[0]+0.5, C[1]-1, 'C(7,5)', fontsize=10)
plt.text(P[0]-1.5, P[1]+0.5, 'P(2,7)', fontsize=10)
plt.text(P[0]+1.5, P[1], '$15 - \sqrt{29}$', fontsize=10)

# Plot radius line to show circle edge in same direction
vec_CP = P - C
vec_dir = vec_CP / np.linalg.norm(vec_CP)
edge_point = C + r * vec_dir
plt.plot([C[0], edge_point[0]], [C[1], edge_point[1]], 'r:', label='Radius = 15')

# Equal aspect ratio and settings
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.title('Shortest Distance from Point (2,7) to Circle')
plt.legend(loc='upper right')
plt.show()