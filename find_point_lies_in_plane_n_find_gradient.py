import sympy as sy
from sympy import *
from random import randint,uniform
#x**2+2*y**2+z**2 = 55
x, y, z = symbols('x y z ')

def find_gradient_vector(lhs,a,b,c):
    pdx = sy.diff(lhs,x)
    pdy = sy.diff(lhs,y)
    pdz = sy.diff(lhs,z)
    fx = pdx.subs(x,a)
    fy = pdy.subs(y,b)
    fz = pdz.subs(z,c)
    print("Gradient vector is %s %s %s" % (fx,fy,fz), "for the points %s %s %s" % (a,b,c),"on the plane")
    return True

def find_points_liesin_plane(lhs,rhs):
    count= 0
    while('TRUE'):
        a= randint(1,10)
        b= randint(1,10)
        c= randint(1,10)
        value = lhs.subs([(x,a),(y,b),(z,c)])
        if value==rhs:
            count+=1
            if count>10:
                break
            else:
                find_gradient_vector(lhs,a,b,c)
    return True

if __name__ == "__main__":
    lhs = x**2+2*y**2+z**2
    rhs = 55
    find_points_liesin_plane(lhs,rhs)