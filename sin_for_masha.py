import matplotlib.pyplot as matplt
import numpy as np
import math as mt

a = -3.5*mt.pi
b = mt.pi/2

c = 2.5*mt.pi
d = 6.5*mt.pi
e = 8.5*mt.pi
f = 10.5*mt.pi

x1 = np.linspace(a, b, int(100*(b-a)))
x2 = np.linspace(b, c, int(100*(c-b)))
x3 = np.linspace(c, d, int(100*(d-c)))
x4 = np.linspace(d, e, int(100*(e-d)))
x5 = np.linspace(e, f, int(100*(f-e)))


amp1=2.5
f1 = amp1*np.sin(x1)
f2 = 3*amp1*(np.sin(x2)-1)+amp1
f3 = amp1*np.sin(x3)
f4 = 2*amp1*(np.sin(x4)-1)+amp1
f5 = amp1*np.sin(x5)

matplt.plot(x1, f1, c='k')
matplt.plot(x2, f2, c='k')
matplt.plot(x3, f3, c='k')
matplt.plot(x4, f4, c='k')
matplt.plot(x5, f5, c='k')
matplt.gca().set_aspect("equal")
# matplt.show()
matplt.savefig("figure2.png", dpi=240, bbox_inches="tight")