from wall import *
import matplotlib.pyplot as plt
import numpy as np

Mur = Wall(101,101)

mur_x = []
mur_y = []

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


plt.scatter(mur_x,mur_y)
plt.grid()
plt.show()

