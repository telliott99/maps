import sys
from math import pi, sin, cos

def rad(d):  return (d/360.0) * 2 * pi

def calc(p0,l0):
    
    # standard calcs
    P0 = rad(p0)   
    L0 = rad(l0)
    radius = 1.0
    print('R:  %.2f' % radius)

    p1,p2 = 29.5, 45.5
    print('p1: %.1f' % p1)
    print('p2: %.1f' % p2)
    P1,P2 = rad(p1),rad(p2)
        
    S1 = sin(P1)
    S2 = sin(P2)
    C1 = cos(P1)
    C2 = cos(P2)
    
    n = (S1 + S2)*1.0/2
    print('n:  %.7f' % n)
        
    C = C1**2 + 2 * n * S1
    print('C:  %.7f' % C)
    
    def rho(P):
        part = (C - 2*n*sin(P))**0.5
        return (radius/n) * part
         
    R0 = rho(P0)
    print('R0: %.7f' % R0)
    
    # specific calcs
    def f(p,l):
        P = rad(p)
        R = rho(P)
        
        print('R:  %.7f' % R)
        
        theta = n * (l - l0)
        print('t:  %.7f' % theta)
        T = rad(theta)
        
        x = R * sin(T)
        y = R0 - R * cos(T)
        return x,y
    return f

p0 = 23
l0 = -96
print('p0: %.1f' % p0)
print('l0:%.1f' % l0)

g = calc(p0,l0)

if __name__ == "__main__":

    p = 35
    l = -75
    print('p:  %.1f' % p)
    print('l: %.1f' % l)
    
    x,y = g(p,l)
    print('x:  %.7f' % x)
    print('y:  %.7f' % y)
