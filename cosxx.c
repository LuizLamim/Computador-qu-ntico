#include <stdio.h>  // For printf
#include <math.h>   // For cos() and M_PI

int main() {
    double x, y;
    double start_x = -10.0;
    double end_x = 10.0;
    int num_points = 1000;
    double step = (end_x - start_x) / (num_points - 1);

    // Print a header (optional, but good for understanding the data)
    // printf("# x_value y_value\n");

    for (int i = 0; i < num_points; i++) {
        x = start_x + i * step;
        y = cos(x) + x;
        printf("%.6f %.6f\n", x, y); // Print x and y values, formatted to 6 decimal places
    }

    return 0;
}