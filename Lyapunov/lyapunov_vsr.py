import math
descartar = 1000
total = 10000.
nombre = raw_input("Nombre del archivo: ")
nombre = nombre + ".dat"
bif = open("bifurcacion.dat", "w")
r = 0.01
archivo = open(nombre, "w")
archivo.write('#r\tlyap\n')
while r < 3.5:
    bif.write('%.3f\t' % r)
    n = 0
    x = 0.1354
    suma = 0
    while n < total:
        x = r * x * (1 - x)
        if n > descartar:
            bif.write('%.3f\t' % x)
        suma = suma + math.log(math.fabs(r - 2 * x * r)) / math.log(2)
        n = n + 1
    lyap = suma / total
    archivo.write('%.2f\t' % r)
    archivo.write('%.2f\n' % lyap)
    bif.write("\n")
    r = r + 0.01
while r < 4:
    bif.write('%.3f\t' % r)
    n = 0
    x = 0.1354
    suma = 0
    while n < total:
        x = r * x * (1 - x)
        if n > descartar:
            bif.write('%.3f\t' % x)
        suma = suma + math.log(math.fabs(r - 2 * x * r)) / math.log(2)
        n = n + 1
    lyap = suma / total
    archivo.write('%.2f\t' % r)
    archivo.write('%.2f\n' % lyap)
    bif.write("\n")
    r = r + 0.001
