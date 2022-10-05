import svg

P1 = svg.Point(50,70)
P2 = svg.Point(40,60)
P3 = svg.Point(40,80)

from math import cos
x = cos(2)
with open('test.svg', 'w') as f:
    image_d = svg.genere_balise_debut_image(100, 100)
    image_f = svg.genere_balise_fin_image()
    groupe_d = svg.genere_balise_debut_groupe('black', 'red', 2)
    groupe_f = svg.genere_balise_fin_groupe()
    c1 = svg.genere_cercle(P1, 10)
    c2 = svg.genere_cercle(P2, 10)
    c3 = svg.genere_cercle(P3, 10)
    space1 = '     '
    space2 = '         '
    print(image_d, file=f)
    print(space1+groupe_d, file=f) 
    print(space2+c1, file=f)
    print(space2+c2, file=f)
    print(space2+c3, file=f)
    print(space1+groupe_f, file=f)
    print(image_f, file=f)
    print(image_d)