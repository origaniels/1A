from random import randint
from math import sin, cos
from svg import Point


def triangle_aleatoire(p1, p2):
    """genere un triangle aléatoire sous la forme d'un tableau de points
    """
    triangle = []
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    for _ in range(3):
        x = randint(x1, x2)
        y = randint(y1, y2)
        triangle.append(Point(x, y))
    if triangle[0] != triangle[1] and triangle[2] != triangle[1]:
        return triangle
    else:
        return triangle_aleatoire(p1, p2)
    
def tourne_triangle_autour(triangle, centre, angle):
    """Tourne un triangle d'un angle angle autour d'un point centre
    """
    xc = centre.x
    yc = centre.y
    for i, point in enumerate(triangle):
        
        newpoint = Point((point.x - xc) * cos(angle) - (point.y - yc) * sin(angle) + xc, (point.x - xc) * sin(angle) + (point.y - yc) * cos(angle) + yc)
        triangle[i] = newpoint
    return triangle

