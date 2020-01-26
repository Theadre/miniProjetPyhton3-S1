import random


# define functions **************************************************************************************************

# 1 Supprimer une lettre d'un mot saisi
def deleteLettreByIndex(word, i):
    new_word = word[:i] + '' + word[i + 1:]
    return new_word


# 2 Remplacer la lettre d'un mot
def replaceLettreByIndex(word, i, new_lettre):
    new_word = word[:i] + new_lettre + word[i + 1:]
    return new_word


# 3 ----------
def mainApplication(message_welcome):
    print(message_welcome)

    while True:
        user_choice = input("Votre choix (t, e, c ou q): ")
        typed_word = ''

        # choix de la lettre "t"
        if user_choice == 't':
            typed_word = input("Votre mot:")
            length = len(typed_word)
            list_of_words = []

            # création d'une liste de mots
            for index in range(length):
                updated_word = deleteLettreByIndex(typed_word, index)
                list_of_words.append(updated_word)

            print(list_of_words)

            print("Jérémy dit : ça marche ! ")

        # choix de la lettre "e"
        elif user_choice == 'e':
            typed_word = input("Mot1:")
            length = len(typed_word)

            random_index = random.randrange(0, length)

            updated_word = deleteLettreByIndex(typed_word, random_index)

            print("Mot2:" + updated_word)

            print("Jérémy dit : ça marche ! ")

        # choix de la lettre "c" :
        elif user_choice == 'c':
            typed_word = input("Mot1:")
            list_of_lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

            length_of_typed_word = len(typed_word)
            length_of_list_of_lettres = len(list_of_lettres)

            random_index_of_typed_word = random.randrange(0, length_of_typed_word)
            random_index_of_letter = random.randrange(0, length_of_list_of_lettres)

            random_letter = list_of_lettres[random_index_of_letter]

            updated_word = replaceLettreByIndex(typed_word, random_index_of_typed_word, random_letter)

            print("Mot2:" + updated_word)
            print("TASWIN AL KASID Jérémy dit : ca marche ! ")
        else:
            break

    exit()


# launch the application *********************************************************

message_welcome = """
        Bienvenue dans le programme de TASWIN AL KASID Jérémy
        afficher la liste de [t]ous les mots qu'on peut obtenir en enlevant un seul caractère d'un mot
        afficher si 'mot2' peut être obtenu en [e]nlevant un seul caractère de 'mot1'
        afficher si 'mot2' peut être obtenu en [c]hangeant un seul caractère de 'mot1'
        [q]uitter
    """

mainApplication(message_welcome)
