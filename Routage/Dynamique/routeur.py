class Routeur:
    def __init__(self, nom):
        """
        Initialise un routeur avec un nom, une table de routage vide et une liste de voisins.
        """
        self.nom = nom
        self.table_routage = {}  # Clé : destination, Valeur : (next_hop, distance)
        self.voisins = []
        self.panne = False

    def ajouter_voisin(self, routeur):
        """
        Ajoute un voisin et met à jour la table de routage avec une distance de 1.
        """
        self.voisins.append(routeur)
        self.table_routage[routeur.nom] = (routeur.nom, 1)
    
    def afficher_table(self):
        """
        Affiche la table de routage du routeur.
        """
        print(f"Table de routage de {self.nom}:")
        for destination, (next_hop, distance) in self.table_routage.items():
            print(f"Vers {destination} via {next_hop} : distance {distance}")
        print("-" * 40)

    def mise_a_jour_rip(self):
        """
        Met à jour la table de routage selon l'algorithme RIP.
        """
        changement = False

        if self.panne:
            return False
        
        for voisin in self.voisins:
            for destination, (next_hop, distance) in voisin.table_routage.items():
                if destination != self.nom:  # Ignore les routes vers soi-même
                    nouvelle_distance = distance + 1
                    if nouvelle_distance <= 15:
                        if destination not in self.table_routage or self.table_routage[destination][1] > nouvelle_distance:
                            self.table_routage[destination] = (voisin.nom, nouvelle_distance)
                            changement = True
        
        return changement
    
    def simuler_panne(self):
        """
        Simule la panne du routeur en supprimant toutes ses routes et en le déconnectant de ses voisins.
        """
        print(f"\n*** Panne du routeur {self.nom} ***")
        self.table_routage.clear()
        for voisin in self.voisins:
            if self.nom in voisin.table_routage:
                del voisin.table_routage[self.nom]
        self.voisins.clear()
        self.panne = True