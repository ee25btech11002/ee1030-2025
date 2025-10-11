#include <stdio.h>
#include <math.h>
#ifndef pi
#define pi acos(-1.0)
#endif

// Compute the center components
void compute_center(double u[2], double C[2]) {
    C[0] = -u[0];
    C[1] = -u[1];
}

// Compute the radius
double compute_radius(double u[2], double f) {
    return sqrt(u[0]*u[0] + u[1]*u[1] - f);
}

// Compute circle coordinates (x and y arrays)
void generate_circle_points(double C[2], double r, double *x, double *y, int n) {
    double theta;
    for (int i = 0; i < n; i++) {
        double theta = 2.0 * pi * i / n;
        x[i] = C[0] + r * cos(theta);
        y[i] = C[1] + r * sin(theta);
    }
}

// Compute edge point in direction of P
void compute_edge_point(double C[2], double P[2], double r, double edge[2]) {
    double dir[2];
    double mag = sqrt(pow(P[0]-C[0], 2) + pow(P[1]-C[1], 2));
    dir[0] = (P[0]-C[0]) / mag;
    dir[1] = (P[1]-C[1]) / mag;
    edge[0] = C[0] + r * dir[0];
    edge[1] = C[1] + r * dir[1];
}
