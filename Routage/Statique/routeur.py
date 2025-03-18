from route import Route

class Routeur:
    def __init__(self, nom):
        """
        Initialise un nouveau routeur
        """
        self.nom = nom
        self.routes = []
    
    def ajouter_route(self, route):
        """
        Ajoute une route à la table de routage
        """
        self.routes.append(route)
    
    def afficher_table(self):
        """
        Affiche la table de routage complète
        """
        print(f"Table de routage du routeur {self.nom}:")
        print("-" * 40)
        for route in self.routes:
            print(route)
        print("-" * 40)
    
    def trouver_route(self, adresse):
        """
        Trouve la meilleure route pour une adresse IP donnée
        """
        meilleures_routes = [route for route in self.routes if route.correspond(adresse)]
        if meilleures_routes:
            return max(meilleures_routes, key=lambda r: sum(map(int, r.masque.split('.'))))
        return next((route for route in self.routes if route.destination == "0.0.0.0"), None)
    
    def acheminer_paquet(self, adresse_source, adresse_dest):
        """
        Simule l'acheminement d'un paquet
        """
        route = self.trouver_route(adresse_dest)
        if route:
            print(f"Paquet de {adresse_source} à {adresse_dest} acheminé via {route}")
            return True
        print(f"Aucune route trouvée pour {adresse_dest}. Acheminement impossible.")
        return False


if __name__ == "__main__":
    # Création des routeurs
    routeur1 = Routeur("R1")
    routeur2 = Routeur("R2")

    # Ajout de routes aux routeurs
    routeur1.ajouter_route(Route("192.168.1.0", "255.255.255.0", "-", "eth0"))
    routeur1.ajouter_route(Route("192.168.2.0", "255.255.255.0", "192.168.1.254", "eth0"))
    routeur1.ajouter_route(Route("0.0.0.0", "0.0.0.0", "192.168.1.1", "eth0"))

    routeur2.ajouter_route(Route("192.168.2.0", "255.255.255.0", "-", "eth1"))

    # Affichage des tables de routage
    routeur1.afficher_table()
    routeur2.afficher_table()

    # Simulation d'acheminement
    test1 = routeur1.acheminer_paquet("192.168.1.10", "192.168.2.5")
    test2 = routeur1.acheminer_paquet("192.168.1.10", "8.8.8.8")
