choix = input("Votre choix (t, e, c ou q): ")

if choix == "t":
    motUn = input("Mot1:")
else:
    motUn = input("Mot1:")
    motDeux = input("Mot2:")


# Fonction qui compte le nombre de caractères
def compterLesCaracteres(phrase):
    i = 0
    for f in phrase:
        i += 1
    return i


if choix == "t":
    LongueurMot = compterLesCaracteres(motUn)
    i = 0
    mot = ""
    while i != LongueurMot:
        mot = mot + motUn[i]
        i = i + 1
    print(mot)
