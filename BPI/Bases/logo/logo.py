from svg import *
from math import cos, sin, pi


def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    """
    x_f = abscisse + distance * cos(pi * direction / 180)
    y_f = ordonnee + distance * sin(pi * direction / 180)

    if crayon_en_bas :
        print(genere_segment(Point(abscisse, ordonnee), Point(x_f, y_f)))

    
    return Point(x_f, y_f)


def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    direction += -angle
    return direction


def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return direction + angle

