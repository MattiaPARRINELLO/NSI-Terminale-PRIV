from listeChainee import liste_chainee
from printFormat import print_colored
def tests():
    liste_test = liste_chainee()
    if liste_test.est_vide() == True:
        print_colored("Test est_vide() avec liste vide : OK", "green")
    else:
        print_colored("Test est_vide() avec liste vide : KO", "red")
        print_colored("Résultat attendu : True", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test.est_vide()), "yellow")
    if liste_test.tete() == None:
        print_colored("Test tete() avec liste vide : OK", "green")
    else:
        print_colored("Test tete() avec liste vide : KO", "red")
        print_colored("Résultat attendu : None", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test.tete()), "yellow")
    if liste_test.queue() == None:
        print_colored("Test queue() avec liste vide : OK", "green")
    else:
        print_colored("Test queue() avec liste vide : KO", "red")
        print_colored("Résultat attendu : None", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test.queue()), "yellow")
    if str(liste_test) == "None":
        print_colored("Test __str__() avec liste vide : OK", "green")
    else:
        print_colored("Test __str__() avec liste vide : KO", "red")
        print_colored("Résultat attendu : None", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test), "yellow")
    if len(liste_test) == 0:
        print_colored("Test __len__() avec liste vide : OK", "green")
    else:
        print_colored("Test __len__() avec liste vide : KO", "red")
        print_colored("Résultat attendu : 0", "yellow")
        print_colored("Résultat obtenu : " + str(len(liste_test)), "yellow")
    liste_test.ajouter(1)
    if liste_test.est_vide() == False:
        print_colored("Test est_vide() avec liste non vide : OK", "green")
    else:
        print_colored("Test est_vide() avec liste non vide : KO", "red")
        print_colored("Résultat attendu : False", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test.est_vide()), "yellow")
    if liste_test.tete() == 1:
        print_colored("Test tete() avec liste non vide : OK", "green")
    else:
        print_colored("Test tete() avec liste non vide : KO", "red")
        print_colored("Résultat attendu : 1", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test.tete()), "yellow")
    if liste_test.queue() == None:
        print_colored("Test queue() avec liste a un élément : OK", "green")
    else:
        print_colored("Test queue() avec liste a un élément : KO", "red")
        print_colored("Résultat attendu : None", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test.queue()), "yellow")
    if str(liste_test) == "1 -> None":
        print_colored("Test __str__() avec liste non vide : OK", "green")
    else:
        print_colored("Test __str__() avec liste non vide : KO", "red")
        print_colored("Résultat attendu : 1 -> None", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test), "yellow")
    if len(liste_test) == 1:
        print_colored("Test __len__() avec liste non vide : OK", "green")
    else:
        print_colored("Test __len__() avec liste non vide : KO", "red")
        print_colored("Résultat attendu : 1", "yellow")
        print_colored("Résultat obtenu : " + str(len(liste_test)), "yellow")
    liste_test.ajouter(2)
    if liste_test.queue() == [2]:
        print_colored("Test queue() avec 2 éléments dans la liste : OK", "green")
    else:
        print_colored("Test queue() avec 2 éléments dans la liste : KO", "red")
        print_colored("Résultat attendu : [2]", "yellow")
        print_colored("Résultat obtenu : " + str(liste_test.queue()), "yellow")
