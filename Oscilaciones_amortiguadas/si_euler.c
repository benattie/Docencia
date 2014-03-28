#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "array_alloc.h"

typedef double (*fun_ptr) (double x, double * params);

double F_MAS(double x, double * params)
{
    double omega2 = pow(params[0], 2);
    double a = - omega2 * x;
    return a;
}

//definir funcion para el movimiento amortiguado
//definir funcion para el movimiento amortiguado forzado

int si_euler_iteration(double * x, double * v, double t, double step, fun_ptr g, double * params)
{
    v[1] = v[0] + g(x[0], params) * step;
    x[1] = x[0] + v[1] * step;
    return 0;
}

int main(int argc, char **argv)
{   
    FILE *fp = fopen("t_x_v.dat", "w");
    double * x = vector_double_alloc(2); 
    double * v = vector_double_alloc(2);
    double * omega = vector_double_alloc(1);
    fun_ptr ac;
    ac = &g;
    int iter = 0, max_iter;
    //double step = 0.001;
    double step = atof(argv[1]);
    max_iter = atoi(argv[2]);
    printf("Escriba el valor de omega:\n");
    scanf("%lf", omega);
    printf("Escriba el valor inicial de x:\n");
    scanf("%lf", &x[0]);
    printf("Escriba el valor inicial de v:\n");
    scanf("%lf", &v[0]);
    //x[0] = 1.0;
    //v[0] = 0.0;
    fprintf(fp, "#t\tx\tv\n");

    while(iter < max_iter)
    {
        if(si_euler_iteration(x, v, iter * step, step, ac, omega))
        {
            printf("Error durante la iteración\n");
            break;
        }
        fprintf(fp, "%.3lf\t%.3lf\t%.3lf\n", step * iter, x[1], v[1]);
        x[0] = x[1];
        v[0] = v[1];
        iter++;
    }
    return 0;
}
