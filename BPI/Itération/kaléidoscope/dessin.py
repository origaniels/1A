from random import randint
from svg import *

def couleur_aleatoire():
    """genere le code d'une couleur aléatoirement
    """
    couleur = "#"
    liste_hexa = [f"{i}" for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(6):
        valeur = liste_hexa[randint(0, 14)]
        couleur += valeur
    return couleur

def affiche_triangle(triangle, couleur):
    """Affiche le triangle dans la couleur donnée
    """
    print(genere_balise_debut_groupe(couleur, couleur, 1))
    print(genere_polygone(triangle, couleur))
    print(genere_balise_fin_groupe())



