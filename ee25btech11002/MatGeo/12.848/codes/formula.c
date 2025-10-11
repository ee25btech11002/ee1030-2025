#include <stdio.h>
#include <math.h>

// Function to compute Z values for the surface: z = 9 - x^2 - y^2
void compute_surface(int n, double *x, double *y, double **Z) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Z[i][j] = 9.0 - x[i]*x[i] - y[j]*y[j];
        }
    }
}

// Function to compute Z values for the tangent plane: z = 14 - 2x - 4y
void compute_plane(int n, double *x, double *y, double **Z) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Z[i][j] = 14.0 - 2.0*x[i] - 4.0*y[j];
        }
    }
}