from math import pi
from boid import *
import numpy as np
import matplotlib.pyplot as plt
from wall import *


# Variables du prog
B1 = boid(40,69,1,(120 * pi /180))
Mur = Wall(101,101)

B1_x = []
B1_y = []
mur_x = []
mur_y = []

i = 0

# Création du mur :
for i in range(101):

    # Mur gauche
    p = Point(0,i)
    Mur.wallAdd(p)
    mur_x.append(p.get_x())
    mur_y.append(p.get_y())

    # Mur droite
    p = Point(100,i)
    Mur.wallAdd(p)
    mur_x.append(p.get_x())
    mur_y.append(p.get_y())

    # Mur bas
    p = Point(i,0)
    Mur.wallAdd(p)
    mur_x.append(p.get_x())
    mur_y.append(p.get_y())

    # Mur gauche
    p = Point(i,100)
    Mur.wallAdd(p)
    mur_x.append(p.get_x())
    mur_y.append(p.get_y())

for i in range (6):
    p = Point(i*20,i*20)
    Mur.wallAdd(p)
    mur_x.append(p.get_x())
    mur_y.append(p.get_y())

for i in range(31):
    p = Point(31,45+i)
    Mur.wallAdd(p)
    mur_x.append(p.get_x())
    mur_y.append(p.get_y())

for i in range(18):
    p = Point(100-i,45+i)
    Mur.wallAdd(p)
    mur_x.append(p.get_x())
    mur_y.append(p.get_y())

# Exécution du script
while(i<10000):
    B1.boidBehave(Mur)
    B1_x.append(B1.get_x())
    B1_y.append(B1.get_y())
    i = i+1

plt.plot(B1_x,B1_y)
plt.grid()

plt.scatter(mur_x,mur_y,c='red')
plt.show()
