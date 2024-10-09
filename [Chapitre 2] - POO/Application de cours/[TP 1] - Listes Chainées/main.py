from printFormat import print_colored
from tests import tests
from listeChainee import liste_chainee
from art import tprint
from random import randint
from tqdm import tqdm
import webbrowser


def clearTerminal():
    print("\033[H\033[J")

def main():
    clearTerminal()
    tprint(" Listes\nChainees", font="beer-pub")
    print_colored("Bienvenue dans le programme de test des listes chainées", "blue")
    print("------------------------------------------------------------------------")
    print_colored("1 - Realiser les tests", "cyan")
    print_colored("2 - Manipulation d'une liste chainée a travers un menu", "cyan")
    print("------------------------------------------------------------------------")
    choix = input("Que voulez vous faire ? ")
    if choix == "1":
        clearTerminal()
        tprint("Tests", font="beer-pub")
        tests()
    elif choix == "2":
        clearTerminal()
        menu()


def menu():
    liste = liste_chainee()
    input_user = ""
    last_return = None
    while True:
        clearTerminal()
        tprint(" Menu", font="beer-pub")
        print_colored("--------------------", "orange")
        print_colored("1 - Afficher la liste", "blue")
        print_colored("2 - Ajouter un élément", "green")
        print_colored("3 - Ajouter de manière aléatoire", "green")
        print_colored("4 - Retirer un élément à partir de son index", "yellow")
        print_colored("5 - Retirer un élément à partir de sa valeur", "yellow")
        print_colored("6 - Vider la liste", "red")
        print_colored("7 - Afficher la longueur de la liste", "blue")
        print_colored("8 - Afficher la tête de la liste", "blue")
        print_colored("9 - Afficher la queue de la liste", "blue")
        print_colored("10 - Quitter", "purple")
        print_colored("--------------------", "orange")
        if len(liste) > 70:
            print_colored("Liste : " + str(liste.tete()) + " -> ... -> " + str(liste.fin()), "cyan")
        else:
            print_colored("Liste : " + str(liste), "cyan")
        print_colored("Dernier retour : " + str(last_return), "green")
        print_colored("--------------------", "orange")
        input_user = input("Que voulez vous faire ? ") 

        if input_user == "1":
            print(liste)

        elif input_user == "2":
            valeur = input("Quelle valeur voulez vous ajouter ? ")
            liste.ajouter(valeur)

        elif input_user == "3":
            nb = input("Combien de valeurs voulez vous ajouter ? ")
            for _ in tqdm(range(int(nb))):
                liste.ajouter(randint(0, 10000000))

        elif input_user == "4":
            valeur = input("Quelle index voulez vous retirer ? ")
            liste.retirer_index(valeur)

        elif input_user == "5":
            valeur = input("Quelle valeur voulez vous retirer ? ")
            liste.retirer_valeur(valeur)

        elif input_user == "6":
            liste.vider()

        elif input_user == "7":
            last_return = len(liste)

        elif input_user == "8":
            last_return = liste.tete()

        elif input_user == "9":
            last_return = liste.queue()

        elif input_user == "10":
            print_colored("Au revoir !", "blue")
            break


        else:
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')




if __name__ == "__main__":
    main()






