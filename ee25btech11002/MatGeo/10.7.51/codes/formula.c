#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// ---------- Define structure ----------
typedef struct {
    double x;
    double y;
} Vec2;

// ---------- Compute V @ P ----------
void tangent_normal_at(double a, double b, Vec2 P, Vec2 *n) {
    n->x = P.x / (a * a);
    n->y = P.y / (b * b);
}

// ---------- Foot of perpendicular from origin to line n·x = 1 ----------
void foot_from_origin_to_line(Vec2 n, double c, Vec2 *N) {
    double denom = n.x * n.x + n.y * n.y;
    N->x = (c / denom) * n.x;
    N->y = (c / denom) * n.y;
}

// ---------- Cross product area ----------
double area_triangle(Vec2 P, Vec2 O, Vec2 N) {
    double cross = P.x * N.y - P.y * N.x;
    return 0.5 * fabs(cross);
}

// ---------- Compute optimal P points ----------
void compute_P_points(double a, double b, Vec2 *P_plus, Vec2 *P_minus) {
    double lam = 1.0 / sqrt(a * a + b * b);
    P_plus->x = lam * a * a;
    P_plus->y = lam * b * b;
    P_minus->x = -P_plus->x;
    P_minus->y = -P_plus->y;
}

// ---------- Compute tangent line points (parametric) ----------
void tangent_line_points(Vec2 n, Vec2 N, double span, int npts, double *x_out, double *y_out) {
    // J @ n = (n.y, -n.x)
    double tx = n.y;
    double ty = -n.x;
    double step = (2 * span) / (npts - 1);
    for (int i = 0; i < npts; i++) {
        double s = -span + i * step;
        x_out[i] = N.x + tx * s;
        y_out[i] = N.y + ty * s;
    }
}
