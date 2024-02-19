import numpy as np 
import cmath

n = int(input("Unesite nenegativan cijeli broj: "))
b = []
for i in range(3):
    temp = complex(input(f"Unesite vrijednost broja b_{i}: "))
    b.append(temp)
c = []
for i in range(3):
    temp = complex(input(f"Unesite vrijednost broja c_{i}: "))
    c.append(temp)

# mogli smo i inverz pa dot product ili eventualno Cramer x = ((de - bf) / (ad - bc)), y = ((af - ce) / (ad - bc))
A = np.array([[b[1], b[0]], [c[1], c[0]]])
B = np.array([b[2], c[2]])
lambdas = np.linalg.solve(A, B)

# nakon ovoga mozemo zadatak rjesiti iterativno preko rekurzivne funkcije, ali to nije prikladno za velike n-ove
# ovako smo u konstantnom vremenu 

#sada rjesavam kvadratnu jednadzbu oblika x^2 - lambda[0]x - lambda[1] = 0 kako bi dobili nultocke pripadajuceg polinoma
disc = (lambdas[0]**2) + (4 * lambdas[1])
x1 = complex(((lambdas[0]-cmath.sqrt(disc))/(2)))
x2 = complex((lambdas[0]+cmath.sqrt(disc))/(2))

# sada jos moramo izracunati koeficijente mi1, mi2 uz n.t. 
if(x1 == x2):
    x = x1
    # u ovom slucaju jednadzba izgleda bn = mi[0]x^n + mi[1]*n*x^n -> rjesavamo sustav iz uvjeta
        # 1 mi1 + 0 mi2 = b[0]
        # mi1 * x1 + mi2 * x2 * n = b[1]
    mi1 = b[0]
    mi2 = (b[1] - mi1 * x) / (x * n)
    rez = (mi1 * (x**n)) + (mi2 * n * (x**n))
else: 
    # u ovom slucaju jednadzba izgleda bn = mi[0] * x^n + mi[1] * x^n -> rjesavamo sustav iz uvjeta
        # 1 mi1 + 1 mi2 = b[0]
        # mi1 * x1 + mi2 * x2 = b[1]
    mi1 = (b[1] - b[0] * x2) / (x1 - x2) #cista supstitucija
    mi2 = b[0] - mi1
    rez = (mi1 * (x1**n)) + (mi2 * (x2**n))

if(rez.imag != 0):
        print("Vrijednost broja b_n: ", round(rez.real, 2) + round(rez.imag, 2) * 1j)
else: 
        print("Vrijednost broja b_n: ", round(rez.real, 2))







