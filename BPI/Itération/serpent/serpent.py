import sys
from svg import *

def nb_cases_hauteur(hauteur):
    """Renvoit le nombre de cases à placer en hauteur
    """
    if hauteur >= 40 : 
        nombre_cases = 1
        taille = 40
        while taille <= hauteur :
            taille += 80
            nombre_cases += 2
        return nombre_cases
    else :
        return "dimensions trop petites"

def nb_cases_largeur(largeur):
    """Renvoit le nombre de cases à placer en largeur"""
    return largeur // 40

def total_cases(largeur, hauteur):
    """renvoit le nombre de cases total
    """
    return((nb_cases_largeur(largeur) + 1) * nb_cases_hauteur(hauteur) // 2)

def main():
    """enregistre le plateau de jeu
    """
    hauteur = int(sys.argv[1])
    largeur = int(sys.argv[2])
    nb_h = nb_cases_hauteur(hauteur)
    nb_l = nb_cases_largeur(largeur)
    numero_case = 0
    print(genere_balise_debut_image(largeur, hauteur))
    print('<style> \n .small {\n  font: italic 13px sans-serif;\n}')
    print('</style>')
    y = 0
    print(genere_balise_debut_groupe("white",  "white", 1))
    print(genere_polygone([Point(0, 0), Point(0, hauteur), Point(largeur, hauteur), Point(largeur, 0)], "white"))
    print(genere_balise_fin_groupe())
    x = 0 
    if y + 40 <= hauteur:
        for j in range(nb_l):
            numero_case += 1
            print(dessine_case(Point(x, y), Point(x + 40, y + 40)))
            print(ecrit(Point(x + 5, y + 20), numero_case))
            x += 40
        y += 40
    while y + 80 <= hauteur:
        if y + 80 <= hauteur:
            numero_case += 1
            print(dessine_case(Point(x - 40, y), Point(x, y + 40)))
            print(ecrit(Point(x - 35, y + 20), numero_case))
            y += 40
            for j in range(nb_l):
                numero_case += 1
                print(dessine_case(Point(x - 40, y), Point(x, y + 40)))
                print(ecrit(Point(x - 35, y + 20), numero_case))
                x -= 40
        y += 40
        
        if y + 80 <= hauteur:
            numero_case += 1
            print(dessine_case(Point(x, y), Point(x + 40, y + 40)))
            print(ecrit(Point(x + 5, y + 20), numero_case))
            y += 40
            for j in range(nb_l):
                numero_case += 1
                print(dessine_case(Point(x, y), Point(x + 40, y + 40)))
                print(ecrit(Point(x + 5, y + 20), numero_case))
                x += 40
        y += 40
        
    print(genere_balise_fin_image())


if __name__ == "__main__":
    main()

