from routeur import Routeur
import random
def simuler_reseau(routeurs, nb_cycles):
    print("\n=== Début de la simulation ===")
    for cycle in range(nb_cycles):
        print(f"\nCycle {cycle + 1}")
        changement = False
        for routeur in routeurs:
            if routeur.mise_a_jour_rip():
                changement = True
        for routeur in routeurs:
            routeur.afficher_table()
        if not changement:
            print(f"\nConvergence atteinte en {cycle + 1} cycles!")
            break
    print("=== Fin de la simulation ===")


def simuler_reseau_panne(routeurs, nb_cycles):
    print("\n=== Début de la simulation ===")

    for cycle in range(nb_cycles):
        if cycle == 1:
            failed_router = random.choice(routeurs)
            failed_router.simuler_panne()
            print(f"\n--== Le routeur {failed_router.nom} est en panne ==--")


        print(f"\nCycle {cycle + 1}")
        changement = False
        for routeur in routeurs:
            if routeur.mise_a_jour_rip():
                changement = True
        for routeur in routeurs:
            routeur.afficher_table()
        

        if not changement:
            print(f"\nConvergence atteinte en {cycle + 1} cycles!")
            break
    print("=== Fin de la simulation ===")



if __name__ == "__main__":
    r1 = Routeur("R1")
    r2 = Routeur("R2")
    r3 = Routeur("R3")
    r4 = Routeur("R4")

    r1.ajouter_voisin(r2)
    r2.ajouter_voisin(r1)
    r2.ajouter_voisin(r3)
    r3.ajouter_voisin(r2)
    r3.ajouter_voisin(r4)
    r4.ajouter_voisin(r3)


    rp1 = Routeur("RP1")
    rp2 = Routeur("RP2")
    rp3 = Routeur("RP3")
    rp4 = Routeur("RP4")

    rp1.ajouter_voisin(rp2)
    rp2.ajouter_voisin(rp1)
    rp2.ajouter_voisin(rp3)
    rp3.ajouter_voisin(rp2)
    rp3.ajouter_voisin(rp4)
    rp4.ajouter_voisin(rp3)





    routeurs = [r1, r2, r3, r4]
    routeurs_panne = [rp1, rp2, rp3, rp4]
    simuler_reseau(routeurs, 5)
    input("Appuyez sur une touche pour continuer...")
    simuler_reseau_panne(routeurs_panne, 5)