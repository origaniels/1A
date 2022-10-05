#!/usr/bin/python3

from svg import *
from collections import namedtuple

Point = namedtuple("Point", "x, y")
file = input()
with open(file, 'r')  as f:
    liste_pts = f.readlines()
    points = []
    for i in range(len(liste_pts)//2):
        pt = Point(liste_pts[2*i], liste_pts[2*i + 1])
        points.append(pt)
    s = genere_balise_debut_image(640, 480) + "\n" + genere_balise_debut_groupe('blue', 'red', 1) + "\n"
    for pt in points:
        s += genere_cercle(pt, 4) + "\n"
    s += genere_balise_fin_groupe() + "\n" + genere_balise_fin_image()
    print(s)
    
