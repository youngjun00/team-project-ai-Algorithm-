#include <math.h>
#include <stdio.h>


from sympy import *
from sympy.plotting.plot import MatplotlibBackend, _matplotlib_list
          
x, y, z, t = symbols('x y z t')
f, g, h = symbols('f, g, h', cls=Function)

init_printing()


# 라플라스 모듈 불러오기 
from sympy.integrals.transforms import laplace_transform
from sympy.integrals.transforms import inverse_laplace_transform

s = symbols('s')
a, w = symbols('a w', constant=True, positive=True)


laplace_transform( DiracDelta(t), t, s,noconds=True)##DiracDelta(t)=δ(t)  1번

laplace_transform(Heaviside(t), t, s, noconds=True)##Heaviside(t)=u(t)  2번

laplace_transform( t*exp(-a*t), t, s, noconds=True)## 7번 

laplace_transform(sin(w*t), t, s, noconds=True )## 8번

laplace_transform(cos(w*t), t, s, noconds=True )## 9번

laplace_transform( sinh(w*t), t, s, noconds=True)## 10번

#laplace_transform( cosh(w*t), t, s, noconds=True)## 11번 해결안됨.

laplace_transform(t * sin(w*t), t, s, noconds=True )## 12번

laplace_transform(t * cos(w*t), t, s, noconds=True )## 13번

laplace_transform(exp(-a*t) * sin(w*t), t, s, noconds=True) ## 14번

laplace_transform(exp(-a*t) * cos(w*t), t, s, noconds=True )## 15번

