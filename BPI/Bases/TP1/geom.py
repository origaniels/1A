from collections import namedtuple

Point = namedtuple("Point","x y")
Triangle = namedtuple("Triangle","p1 p2 p3")

def affiche_triangle(triangle):
    print(triangle.p1)
    print(triangle.p2)
    print(triangle.p3)

a = Point(2,3)
b = Point(4,5)
c = Point(6,2)

t1 = Triangle(a,b,c)

affiche_triangle(t1)
