import sys
from math import pi, sin, cos

def rad(d):  return (d/360.0) * 2 * pi

def calc(p0,l0):
    
    # standard calcs
    P0 = rad(p0)   
    L0 = rad(l0)
    radius = 1.0

    p1,p2 = 29.5, 45.5
    print('p1', p1)
    print('p2', p2)
    P1,P2 = rad(p1),rad(p2)
        
    S1 = sin(P1)
    S2 = sin(P2)
    C1 = cos(P1)
    C2 = cos(P2)
    
    n = (S1 + S2)*1.0/2
    print('n', n)
        
    C = C1**2 + 2 * n * S1
    print('C', C)
    
    def rho(P):
        part = (C - 2*n*sin(P))**0.5
        return (radius/n) * part
         
    R0 = rho(P0)
    print('R0', R0)
    
    # specific calcs
    def f(p,l):
        P = rad(p)
        R = rho(P)
        
        print('R', R)
        
        theta = n * (l - l0)
        print('t', theta)
        T = rad(theta)
        
        x = R * sin(T)
        y = R0 - R * cos(T)
        return x,y
    return f

p0 = 23
l0 = -96
g = calc(p0,l0)

p = 35
l = -75
x,y = g(p,l)
print('x', x)
print('y', y)
