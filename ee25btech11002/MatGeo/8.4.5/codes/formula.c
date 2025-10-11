#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

// Function to generate ellipse points
void generate_ellipse(double a, double b, int n, double x[], double y[]) {
    for(int i = 0; i < n; i++) {
        double theta = 2 * PI * i / n;
        x[i] = b * cos(theta);
        y[i] = a * sin(theta);
    }
}

// Function to generate circle points
void generate_circle(double cx, double cy, double r, int n, double x[], double y[]) {
    for(int i = 0; i < n; i++) {
        double theta = 2 * PI * i / n;
        x[i] = cx + r * cos(theta);
        y[i] = cy + r * sin(theta);
    }
}
