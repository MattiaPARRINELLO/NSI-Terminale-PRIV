class Route:
    def __init__(self, destination, masque, next_hop, interface):
        """
        Initialise une route.
        """
        self.destination = destination
        self.masque = masque
        self.next_hop = next_hop
        self.interface = interface
    
    def __str__(self):
        """
        Retourne une représentation lisible de la route.
        """
        return f"{self.destination}/{self.masque} via {self.next_hop} sur {self.interface}"
    
    def correspond(self, adresse):
        """
        Vérifie si une adresse appartient à ce réseau en utilisant le masque réseau.
        """
        dest_octets = list(map(int, self.destination.split('.')))
        addr_octets = list(map(int, adresse.split('.')))
        mask_octets = list(map(int, self.masque.split('.')))
        
        for i in range(4):
            if mask_octets[i] == 255 and dest_octets[i] != addr_octets[i]:
                return False
        return True

if __name__ == "__main__":
    # Création des routes demandées
    route_locale = Route("192.168.1.0", "255.255.255.0", "-", "eth0")
    route_distante = Route("192.168.2.0", "255.255.255.0", "192.168.1.254", "eth0")

    # Affichage des routes
    print("Route locale :", route_locale)
    print("Route distante :", route_distante)

    # Test de correspondance
    print("192.168.1.25 appartient au réseau ?", route_locale.correspond("192.168.1.25"))
    print("192.168.2.1 appartient au réseau ?", route_locale.correspond("192.168.2.1"))
