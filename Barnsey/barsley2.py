#import math
import numpy
import random
total = 1000000
nombre = raw_input("Nombre del archivo: ")
nombre = nombre + ".dat"
archivo = open(nombre, "w")
archivo.write('#x\ty\n')
v = numpy.array([0.5, 0.5])
p = [0.84, 0.91, 0.98, 1.00]
A1 = numpy.array([[0.85, 0.02], [-0.02, 0.83]])
A2 = numpy.array([[0.09, -0.28], [0.30, 0.11]])
A3 = numpy.array([[-0.09, 0.28], [0.30, 0.09]])
A4 = numpy.array([[0., 0.], [0., 0.25]])
b1 = numpy.array([0., 1.00])
b2 = numpy.array([0., 0.60])
b3 = numpy.array([0., 0.70])
b4 = numpy.array([0., -0.14])
random.seed(1.0)
for i in range(1, total, 1):
    aux = random.random()
    if aux < p[0]:
        v = numpy.dot(A1, v) + b1
    elif aux < p[1]:
        v = numpy.dot(A2, v) + b2
    elif aux < p[2]:
        v = numpy.dot(A3, v) + b3
    elif aux < p[3]:
        v = numpy.dot(A4, v) + b4
    if i > 100:
        archivo.write('%.3f\t%.3f\n' % (v[0], v[1]))
