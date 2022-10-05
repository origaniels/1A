from sys import argv
def main():
    """Ouvre le fichier 'file' pris en entrée
    """
    with open(file, 'r') as f :
        l = f.readlines()
        print(l)
        for x in l:
            print(x)

if __name__ == "__main__":
    file = argv[1]
    main()

