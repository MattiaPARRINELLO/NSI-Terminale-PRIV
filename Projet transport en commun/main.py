import matplotlib.pyplot as plt



##Contexte 

# Une commune souhaite optimiser son réseau de transport scolaire. Elle dispose d'une liste d'arrêts 
# de bus et doit déterminer le meilleur itinéraire possible pour ramasser tous les élèves en minimisant 
# le temps de trajet total.


##Données fournies

#Un dictionnaire des arrêts avec leurs coordonnées (x, y) et le nombre d'élèves à chaques arrets
ARRETS = {
'A': {'coords': (0, 0), 'nb_eleves': 5},
'B': {'coords': (1, 2), 'nb_eleves': 3},
'C': {'coords': (3, 1), 'nb_eleves': 4},
'D': {'coords': (2, 3), 'nb_eleves': 6},
'LYCEE': {'coords': (5, 5), 'nb_eleves': 0}
}

# Une matrice des temps de trajet entre chaque paire d'arrêts
TEMPS_TRAJET = {
'A': {'B': 10, 'C': 15, 'D': 20, 'LYCEE': 30},
'B': {'A': 10, 'C': 8, 'D': 12, 'LYCEE': 25},
'C': {'A': 15, 'B': 8, 'D': 7, 'LYCEE': 20},
'D': {'A': 20, 'B': 12, 'C': 7, 'LYCEE': 15},
'LYCEE': {'A': 30, 'B': 25, 'C': 20, 'D': 15}
}


class Arret:
    def __init__(self, nom: str, coordonees: tuple, nb_eleves: int) -> None:
        self.nom = nom
        self.cord = coordonees
        self.nb_eleves = nb_eleves

class Graphe:
    def __init__(self, arrets: dict, temps_trajet: dict) -> None:
        self.graphe = {arret: {} for arret in arrets}
        for arret in arrets:
            for voisin in temps_trajet[arret]:
                self.graphe[arret][voisin] = temps_trajet[arret][voisin]

    def __repr__(self) -> str:
        return str(self.graphe)







# Ajouter des méthodes pour calculer le temps total d'un trajet
# et pour afficher le trajet sous forme de texte
class Trajet:
    def __init__(self, graphe: dict, arrets: dict, depart: str) -> None:
        self.graphe = graphe
        self.arrets = arrets
        self.trajet = [depart]
        self.temps_total = 0

    def ajouter_arret(self, arret: str) -> None:
        self.trajet.append(arret)
        self.temps_total += self.graphe[self.trajet[-2]][arret]

    def liste_arrets(self) -> dict:
        return {arret: self.arrets[arret] for arret in self.trajet} 
    
    def nb_eleves(self, arret: str) -> int:
        return self.arrets[arret]['nb_eleves']

    def temps_trajet(self) -> int:
        return self.temps_total

    def afficher(self) -> None:
        print('Trajet:')
        for i in range(len(self.trajet) - 1):
            print(f'{self.trajet[i]} -> {self.trajet[i + 1]}: {self.graphe[self.trajet[i]][self.trajet[i + 1]]} min')
        print(f'Temps total: {self.temps_total} min')


# Trajet1 = Trajet(Graphe(ARRETS, TEMPS_TRAJET).graphe, ARRETS, 'A')
# Trajet1.ajouter_arret('B')
# Trajet1.ajouter_arret('C')
# Trajet1.ajouter_arret('D')
# Trajet1.ajouter_arret('LYCEE')
# Trajet1.afficher()
# print(Trajet1.liste_arrets())



# Créer une fonction utilisant matplotlib pour visualiser :
#   Les arrêts (points)
#   Le nombre d'élèves (taille des points)
#   Les connexions possibles entre les arrêts
#   Le lycée (point en forme d'étoile)


def visualiser(trajets: Trajet) -> None:
    arrets = trajets.liste_arrets()
    for arret in arrets:
        if arret != 'LYCEE':
            plt.scatter(*arrets[arret]['coords'], s=arrets[arret]['nb_eleves'] * 30, label=arret.upper())

    for i in range(len(trajets.trajet) - 1):
        plt.plot([arrets[trajets.trajet[i]]['coords'][0], arrets[trajets.trajet[i + 1]]['coords'][0]], 
                 [arrets[trajets.trajet[i]]['coords'][1], arrets[trajets.trajet[i + 1]]['coords'][1]], 'k-')
    plt.scatter(*arrets['LYCEE']['coords'], marker='*', s=100, label='LYCEE')
    plt.legend()
    plt.show()








# 2.1 Plus court chemin
# Implémenter l'algorithme de Dijkstra pour trouver le plus court chemin entre deux arrêts
# Calculer le meilleur trajet direct entre chaque arrêt et le lycée
# 2.2 Optimisation de circuit
# Implémenter un algorithme glouton pour créer un circuit passant par tous les arrêts
# Améliorer le circuit en utilisant l'algorithme 2-opt (échange de segments)
# Comparer différentes stratégies de construction de circuit initial


def dijkstra(graphe: dict, depart: str, arrivee: str) -> list:
    non_visites = {noeud: float('inf') for noeud in graphe}
    non_visites[depart] = 0
    chemin = {}

    while non_visites:
        noeud_courant = min(non_visites, key=non_visites.get)
        cout_courant = non_visites[noeud_courant]
        if noeud_courant in graphe:
            for voisin, cout in graphe[noeud_courant].items():
                if cout + cout_courant < non_visites.get(voisin, float('inf')):
                    non_visites[voisin] = cout + cout_courant
                    chemin[voisin] = noeud_courant
        del non_visites[noeud_courant]

    noeud_courant = arrivee
    chemin_complet = []
    while noeud_courant != depart:
        chemin_complet.insert(0, noeud_courant)
        noeud_courant = chemin[noeud_courant]
    chemin_complet.insert(0, depart)
    return chemin_complet

test = dijkstra(Graphe(ARRETS, TEMPS_TRAJET).graphe, 'A', 'LYCEE')