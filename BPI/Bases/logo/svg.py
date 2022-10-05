from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple("Point", "x y")

# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaîne de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
    bas.
    """

    s = f"<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='{largeur}' style='background: white' height='{hauteur}'>"
    
    return s
 

# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_image():
    """
    Retourne la chaîne de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l'image, juste avant la fin du fichier.
    """
    return '</svg>'


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    s = f"<g stroke='{couleur_ligne}' fill='{couleur_remplissage}' stroke-width='{epaisseur_ligne}' opacity='1'>"
    return s

def genere_balise_fin_groupe():
    """genere la balise de fin de groupe
    """
    return "</g>"

def genere_balise_debut_groupe_transp(niveau_opacite):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrant un
    groupe d'éléments qui, dans son ensemble, sera partiellement transparent.
    Les éléments qui composent le groupe se masquent les uns les autres dans
    l'ordre d'apparition (ils ne sont pas transparents entre eux).
    `niveau_opacite` doit être un nombre entre 0 et 1. Ce groupe doit être
    refermé de la même manière que les groupes définissant un style.
    """
    s = f"<g opacity='{niveau_opacite}'>"
    return s

def genere_balise_fin_groupe_transp():
    """ genere la balise de fin de groupe transparent
    """
    return '</g>'

# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre, rayon):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    x = centre.x
    y = centre.y

    s =f"<circle cx='{x}' cy='{y}' r='{rayon}'/>"
    return s

def genere_segment(debut, fin):
    """Genere le debut d'un segment
    """
    x_d = debut.x
    y_d = debut.y
    x_f = fin.x
    y_f = fin.y
    s=f"<line x1='{x_d}' x2='{x_f}' y1='{y_d}' y2='{y_f}' />"
    return s

def genere_polygone(points, couleur):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG
    représentant un polygone. `points` est un tableaux de points.
    """
    pts = f"{points[0].x}, {points[0].y}"
    for i in range(1, len(points)):
        x = points[i].x
        y = points[i].y
        pts += " " + f"{x}" + "," + f"{y}"
        
    s = f'<polygon points="{pts}" style="fill:{couleur}; stroke:{couleur};stroke-width:1" />'
    return s

def dessine_case(point1, point2):
    """renvoit les lignes d'un carré
    """
    x1 = point1.x
    x2 = point2.x
    y1 = point1.y
    y2 = point2.y
    largeur = abs(x1 - x2)
    droit = f'<line x1="{x1 + largeur}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" />'
    gauche = f'<line x1="{x1}" y1="{y1}" x2="{x2 -largeur}" y2="{y2}" stroke="black" />'
    haut = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2 - largeur}" stroke="black" />'
    bas = f'<line x1="{x1}" y1="{y1 + largeur}" x2="{x2}" y2="{y2}" stroke="black" />'
    return haut + "\n" + bas + "\n" + droit + "\n" + gauche

def ecrit(point, texte):
    """ecrit un texte donné en entrée aux coordonnées du point
    """
    
    s = f'<text x="{point.x}" y="{point.y}" class="small">{texte}</text>'
    return s

