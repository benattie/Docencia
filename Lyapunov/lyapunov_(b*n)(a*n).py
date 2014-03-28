import math
total = 3000
m = 5
X = 400
Y = 400
nombre = raw_input("Nombre del archivo: ")
nombre = nombre + ".dat"
archivo = open(nombre, "w")
archivo.write('#r0\tr1\tlyap\n')

r = [0, 0]
n = 0
for j in range(1, X, 1):
    print(('%d' % j))
    for k in range(1, Y, 1):
        #print(('%d\t%d' % (j, k)))
        r[0] = 4. * (j / float(X))
        r[1] = 4. * (k / float(Y))
        x = 0.1354
        suma = 0.
        for i in range(0, total, 1):
            if (i % m) == 0:
                if n == 0:
                    n = 1
                else:
                    n = 0
            x = r[n] * x * (1 - x)
            if (r[n] - 2 * x * r[n]) == 0:
                archivo.write('%.3f\t%.3f\t%.3f\tbreak\n' % (r[0], r[1], -5))
                break
            else:
                suma = suma + math.log(math.fabs(r[n] - 2 * x * r[n])) / math.log(2)
        lyap = suma / total
        archivo.write('%.3f\t%.3f\t%.3f\n' % (r[0], r[1], lyap))
