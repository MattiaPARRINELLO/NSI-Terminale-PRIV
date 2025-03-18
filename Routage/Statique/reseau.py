import networkx as nx
import matplotlib.pyplot as plt

class Reseau:
    def __init__(self, nom):
        """
        Initialise un nouveau réseau
        
        Paramètres :
            nom (str) : Le nom du réseau (ex: "Entreprise_A")
        """
        self.nom = nom
        self.routeurs = {}  # Dictionnaire des routeurs {nom: objet Routeur}
        self.connexions = []  # Liste des connexions [(R1, I1, R2, I2)]

    def ajouter_routeur(self, routeur):
        """
        Ajoute un routeur au réseau
        
        Paramètres :
            routeur (Routeur) : Objet routeur à ajouter
        """
        if routeur.nom in self.routeurs:
            print(f"⚠ Le routeur {routeur.nom} existe déjà dans le réseau.")
        else:
            self.routeurs[routeur.nom] = routeur

    def connecter_routeurs(self, routeur1_nom, interface1, routeur2_nom, interface2):
        """
        Établit une connexion entre deux routeurs
        
        Paramètres :
            routeur1_nom (str) : Nom du premier routeur
            interface1 (str) : Interface utilisée sur le premier routeur
            routeur2_nom (str) : Nom du second routeur
            interface2 (str) : Interface utilisée sur le second routeur
        """
        if routeur1_nom not in self.routeurs or routeur2_nom not in self.routeurs:
            raise ValueError("Un des routeurs spécifiés n'existe pas dans le réseau.")

        # Vérifier que les interfaces ne sont pas déjà utilisées
        for r1, i1, r2, i2 in self.connexions:
            if (r1 == routeur1_nom and i1 == interface1) or (r2 == routeur2_nom and i2 == interface2):
                raise ValueError("Une des interfaces est déjà utilisée dans une autre connexion.")

        self.connexions.append((routeur1_nom, interface1, routeur2_nom, interface2))

    def __str__(self):
        """Représentation textuelle du réseau"""
        res = f"🌐 Réseau {self.nom} :\n"
        res += f"Routeurs : {', '.join(self.routeurs.keys())}\n"
        res += "Connexions :\n"
        for r1, i1, r2, i2 in self.connexions:
            res += f"  - {r1} ({i1}) <--> {r2} ({i2})\n"
        return res

    def generer_graphe(self):
        """
        Génère une représentation visuelle du réseau avec NetworkX
        """
        G = nx.Graph()
        
        # Ajout des routeurs comme nœuds
        for routeur in self.routeurs.values():
            G.add_node(routeur.nom)
        
        # Ajout des connexions comme arêtes
        for r1, i1, r2, i2 in self.connexions:
            G.add_edge(r1, r2, label=f"{i1} - {i2}")
        
        # Configuration de l'affichage
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 8))
        
        # Dessin des nœuds et arêtes
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=1500, font_size=10, font_weight='bold')
        
        # Ajout des labels sur les arêtes
        edge_labels = {(r1, r2): f"{i1} - {i2}" for r1, i1, r2, i2 in self.connexions}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.title(f"Topologie du réseau {self.nom}")
        plt.show()

    def simuler_transmission_pas_a_pas(self, source_ip, destination_ip, start_routeur_nom):
        """
        Simule la transmission d'un paquet dans le réseau en mode pas à pas
        
        Paramètres :
            source_ip (str) : L'adresse IP source
            destination_ip (str) : L'adresse IP destination
            start_routeur_nom (str) : Le routeur d'origine
        
        Retourne :
            list ou None : Liste des routeurs traversés ou None en cas d'échec
        """
        if start_routeur_nom not in self.routeurs:
            print(f"❌ Routeur {start_routeur_nom} introuvable dans le réseau.")
            return None

        visites = set()  # Pour éviter les boucles
        chemin = []
        routeur_courant = start_routeur_nom

        while routeur_courant:
            visites.add(routeur_courant)
            chemin.append(routeur_courant)
            print(f"📡 Transmission depuis {routeur_courant}...")

            routeur = self.routeurs[routeur_courant]
            meilleure_route = routeur.trouver_route(destination_ip)

            if not meilleure_route:
                print(f"🚫 Aucun chemin trouvé depuis {routeur_courant} vers {destination_ip}.")
                return None

            if meilleure_route.next_hop == "-":
                print(f"✅ Paquet livré à {destination_ip} via {routeur_courant} !")
                return chemin

            prochain_routeur = None
            for r1, i1, r2, i2 in self.connexions:
                if (r1 == routeur_courant and i1 == meilleure_route.interface):
                    prochain_routeur = r2
                elif (r2 == routeur_courant and i2 == meilleure_route.interface):
                    prochain_routeur = r1

            if not prochain_routeur:
                print(f"❌ Pas de connexion physique pour {meilleure_route.next_hop}.")
                return None

            if prochain_routeur in visites:
                print("🔄 Détection de boucle ! Transmission arrêtée.")
                return None

            routeur_courant = prochain_routeur
            input("➡️ Appuyez sur Entrée pour continuer...")

        return None
