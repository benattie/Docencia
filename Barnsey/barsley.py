#import math
import numpy
import random
total = 1000000
nombre = raw_input("Nombre del archivo: ")
nombre = nombre + ".dat"
archivo = open(nombre, "w")
archivo.write('#x\ty\n')
v = numpy.array([0.5, 0.5])
p = [0.85, 0.92, 0.99, 1.00]
A1 = numpy.array([[0.85, 0.04], [-0.04, 0.85]])
A2 = numpy.array([[0.20, -0.26], [0.23, 0.22]])
A3 = numpy.array([[-0.15, 0.28], [0.26, 0.24]])
A4 = numpy.array([[0., 0.], [0., 0.16]])
b1 = numpy.array([0., 1.60])
b2 = numpy.array([0., 1.60])
b3 = numpy.array([0., 0.44])
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
        v = numpy.dot(A4, v)
#    if i > 100:
    archivo.write('%.3f\t%.3f\n' % (v[0], v[1]))
