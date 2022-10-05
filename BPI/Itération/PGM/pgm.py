import random
from collections import namedtuple

Cercle = namedtuple("Cercle", "x, y, r")
Point = namedtuple("Point", "x, y")

def est_dans_image(cercle, largeur, hauteur):
    """Vérifie si le cercle est bien inscrit dans l'image
    """
    x = cercle.x
    y = cercle.y
    rayon = cercle.r
    if x - rayon <= 0 or x + rayon >= largeur :
        return False
    elif y - rayon <= 0 or y + rayon >= hauteur :
        return False
    else : 
        return True

def genere_cercle_aleatoire(largeur, hauteur):
    """genere un cercle aléatoire valide
    """
    x = random.randint(0, largeur)
    y = random.randint(0, hauteur)
    r = random.randint(0, min(hauteur, largeur))
    cercle = Cercle(x, y, r)
    if est_dans_image(cercle, largeur, hauteur):
        return cercle
    else :
        return genere_cercle_aleatoire(largeur, hauteur)

def distance(p1, p2):
    """Renvoit la distance entre deux points
    """
    x1 = p1.x
    y1 = p1.y
    x2 = p2.x
    y2 = p2.y

    return (x2 - x1)**2 + (y2-y1)**2

def est_dans_cercle(p):
    """Vérifie si un point donné est dans un disque ou non
    """
    centre1 = Point(cercle1.x, cercle1.y)
    centre2 = Point(cercle2.x, cercle2.y)
    rayon1 = cercle1.r
    rayon2 = cercle2.r
    if distance(p, centre1) <= rayon1 :
        return True
    elif distance(p, centre2) <= rayon2 :
        return True
    else : 
        return False

def genere_entete(hauteur, largeur):
    """Genere l'en-tête du fichier pgm
    """
    print('P2')
    print(str(largeur) + ' ' + str(hauteur))
    print(255)

def ecrit_ligne(position, largeur, hauteur):
    """Ecrit une ligne donnée
    """
    p = Point(position, 0)
    s = ""
    for i in range(largeur):
        if est_dans_cercle(p):
            s += " " + str(random.randint(0,255))
        else :
            s += " " + str(0)
        p = Point(position, i)
    print(s)


largeur = int(input())
hauteur = int(input())
cercle1 = genere_cercle_aleatoire(largeur, hauteur)
cercle2 = genere_cercle_aleatoire(largeur, hauteur)
genere_entete(hauteur, largeur)
for j in range(hauteur):
    position = hauteur - j
    ecrit_ligne(position, largeur, hauteur)

