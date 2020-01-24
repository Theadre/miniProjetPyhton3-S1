print("""
Bienvenue dans le programme de Valéry Michaux
afficher la liste de [t]ous les mots qu'on peut obtenir en enlevant un seul caractère d'un mot
afficher si 'mot2' peut être obtenu en [e]nlevant un seul caractère de 'mot1'
afficher si 'mot2' peut être obtenu en [c]angeant un seul caractère de 'mot1'
[q]uitter
""")

choix = input("Votre choix (t, e, c ou q): ")


def compterLesCaracteres(phrase):
    i = 0
    for f in phrase:
        i += 1
    return i


def supprCaractere(motUn):
    LongueurMot = compterLesCaracteres(motUn)

    a = 0
    listeMots = []

    while a != LongueurMot:
        mot = ""
        i = 0

        while i != LongueurMot:
            if a != i:
                mot = mot + motUn[i]
            i = i + 1
        listeMots.extend([mot])
        a = a + 1

    return (listeMots)


if choix == "t":
    motUn = input("Mot1:")
    print(supprCaractere(motUn))

if choix == "e":
    motUn = input("Mot1:")
    motDeux = input("Mot2:")
    tableMotSupp = supprCaractere(motUn)
    nbreMots = len(tableMotSupp) - 1
    print(nbreMots)
    print(tableMotSupp)

    i = 0
    while tableMotSupp[i] != tableMotSupp[nbreMots]:
        if tableMotSupp[i] == motDeux:
            print("Ca marche !")
        else:
            print("Ca ne marche pas !")
        i = i + 1

if choix == "c":
    print("Votre choix c")


if choix == "q":
    quit()
