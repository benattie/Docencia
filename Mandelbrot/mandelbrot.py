#import math
#import cmath
total = 5000
XLow = -1.41
XHigh = -1.2
YLow = -0.08
YHigh = 0.08
DX = abs(XHigh - XLow)
DY = abs(YHigh - YLow)
resX = 2000
resY = 2000
pasox = DX / resX
pasoy = DY / resY
exp = 2
R = 2.0
nombre = raw_input("Nombre del archivo: ")
nombre = nombre + ".dat"
archivo = open(nombre, "w")
archivo.write('#x\ty\tn\n')
i = XLow
while i < XHigh:
    k = YLow
    while k < YHigh:
        z = 0.0 + 0.0j
        n = 0
        flag = 0
        while n < total:
            C = i + k *(1j)
            z = z ** exp + C
            if abs(z) > R:
                archivo.write('%.3f\t%.3f\t%d\n' % (i, k, n))
                n = total
                flag = 1
            else:
                n = n + 1
        if flag == 0:
            archivo.write('%.3f\t%.3f\t%d\n' % (i, k, n))
        k = k + pasoy
    i = i + pasox
archivo.close()
nplot = "plt_mandelbrot_" + nombre
plot = open(nplot, "w")
plot.write('set view map\nset pm3d map\nunset key\n')
plot.write('set xr [%.2f:%.2f]\n' % (XLow, XHigh))
plot.write('set yr [%.2f:%.2f]\n' % (YLow, YHigh))
plot.write('set palette defined (0 "black", %d "sea-green")\n' % n)
plot.write('set cbrange [0:%d]\n' % n)
plot.write('splot \'%s\' u 1:2:3 w d palette\n' % nombre)
plot.close()
