import math
total = 3000
X = 640
Y = 480
nombre = raw_input("Nombre del archivo: ")
nombre = nombre + ".dat"
archivo = open(nombre, "w")
archivo.write('#r0\tr1\tlyap\n')
r = [0., 0.]
for i in range(1, X, 1):
    print(('%d' % i))
    for j in range(1, Y, 1):
        r[0] = 0.6 * (i / 640.) + 2.6
        r[1] = 0.4 * (j / 480.) + 3.6
        x = 0.1354
        suma = 0.
        for n in range(0, total, 1):
            x = r[n % 2] * x * (1 - x)
            if (r[n % 2] - 2 * x * r[n % 2]) == 0:
                archivo.write('%.3f\t%.3f\t%.3f\tbreak\n' % (r[0], r[1], -5))
                break
            else:
                suma = suma + math.log(math.fabs(r[n % 2] - 2 * x * r[n % 2])) / math.log(2)
        lyap = suma / total
        archivo.write('%.3f\t%.3f\t%.3f\n' % (r[0], r[1], lyap))