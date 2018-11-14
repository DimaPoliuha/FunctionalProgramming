import pylab
from matplotlib import mlab
from math import pi, sin, cos


def func_r(fi, a):
    return a / fi


def func_x(r, fi):
    return r * cos(fi)


def func_y(r, fi):
    fi += delta
    return r * sin(fi)


delta = pi / 50
fimin = 1.0
fimax = 25.0

a = -1.0

filist = mlab.frange(fimin, fimax, delta)

rlist = [func_r(fi, a) for fi in filist]

xlist = [func_x(r, fi) for r, fi in zip(rlist, filist)]

ylist = [func_y(r, fi) for r, fi in zip(rlist, filist)]

pylab.plot(xlist, ylist)

pylab.show()
