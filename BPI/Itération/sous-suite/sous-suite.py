from sys import argv

def main():
    """Ouvre le fichier 'file' pris en entrée
    """
    with open(file, 'r') as f :
        l = f.readlines()
        liste_nb = []
        for x in l:
            s = x.strip('\n').split(' ')
            for y in s:
                liste_nb.append(y)
        liste_ss_suite = []
        ss_suite = [liste_nb[0]]
        if liste_nb[0] >= liste_nb[1]:
            type_suite = 0
        else:
            type_suite = 1
        for i in range(1, len(liste_nb)):
            x = liste_nb[i]
            traitement = traite_nombre(liste_nb[:i], type_suite, x)
            if traitement[0]:
                ss_suite.append(x)
            else:
                liste_ss_suite.append(ss_suite.copy())
                ss_suite = [ss_suite[-1], x]
                type_suite = traitement[1]
        i_max = 0
        print(liste_ss_suite)
        print(liste_nb)
        for i, liste in enumerate(liste_ss_suite):
            if len(liste_ss_suite[i_max]) < len(liste):
                i_max = i
        for x in liste_ss_suite[i_max]:
            print(x)



def traite_nombre(suite, type_suite, nombre):
    """Traite le nombre donné vis à vis de la suite donnée.
    Type_suite = 1 si suite croissante, 0 sinon
    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite a changé
    de sens.
    """
    u_n = suite[len(suite) - 1]
    if type_suite == 1 and u_n <= nombre:
        return (True, 1)
    elif type_suite == 0 and u_n >= nombre:
        return (True, 0)
    else:
        return (False, 1 - type_suite)

if __name__ == "__main__":
    file = argv[1]
    main()
