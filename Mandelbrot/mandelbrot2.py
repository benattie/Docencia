import math
total = 50
XLow = -1.50
XHigh = 1.00
YLow = -1.50
YHigh = 1.50
pasox = 0.005
pasoy = 0.005
R = 100
nombre = raw_input("Nombre del archivo: ")
nombre = nombre + ".dat"
archivo = open(nombre, "w")
archivo.write('#x\ty\tL\tn\n')
i = XLow
while i <= XHigh:
    j = YLow
    while j <= YHigh:
        x = 0.0
        y = 0.0
        info = 0.0
        L = 0.0
        n = 0
        while n < total:
            n = n + 1
            x = x ** 2 - y ** 2 + i
            y = 2. * x * y + j
            r = x ** 2 + y ** 2
            if r == 0:
                n = total
                continue
            else:
                L = L + math.log(math.sqrt(0.5 * r))
            if L >= R:
                info = 1.0
                archivo.write('%.3f\t%.3f\t%.1f\t%d\n' % (i, j, info, n))
                n = total
            elif L <= -R:
                info = -1.0
                archivo.write('%.3f\t%.3f\t%.1f\t%d\n' % (i, j, info, n))
                n = total
        if L < 0:
            info = 0.5
            archivo.write('%.3f\t%.3f\t%.1f\t%d\n' % (i, j, info, n))
        elif L > 0:
            info = -0.5
            archivo.write('%.3f\t%.3f\t%.1f\t%d\n' % (i, j, info, n))
        else:
            info = 0.0
            archivo.write('%.3f\t%.3f\t%.1f\t%d\n' % (i, j, info, n))
        j = j + pasoy
    i = i + pasox
archivo.close()
nplot = "plt_mandelbrot_" + nombre
plot = open(nplot, "w")
plot.write('set view map\nset pm3d map\nunset key\n')
plot.write('set xr [%.2f:%.2f]\n' % (XLow, XHigh))
plot.write('set yr [%.2f:%.2f]\n' % (YLow, YHigh))
plot.write('set palette maxcolors 4\n')
plot.write('set palette defined (-1 "black", -0.5 "blue", 0 "red", 0.5 "green", 1 "sea-green")\n')
plot.write('set cbrange [-1:1]\n')
#plot.write('set cbrange [%d:%d]\n' % (0, R))
plot.write('splot \'%s\' u 1:2:3 w d palette\n' % nombre)
plot.close()
