import matplotlib.pyplot as plt
import heapq
import streamlit as st


class Arret:
    def __init__(self, nom, coordonnees, nb_eleves):
        self.nom = nom
        self.coordonnees = coordonnees
        self.nb_eleves = nb_eleves

    def __repr__(self):
        return f"Arret({self.nom}, {self.coordonnees}, {self.nb_eleves} élèves)"
    


# Données des arrêts
ARRETS = {
    'A': {'coords': (0, 0), 'nb_eleves': 5},
    'B': {'coords': (1, 2), 'nb_eleves': 3},
    'C': {'coords': (3, 1), 'nb_eleves': 4},
    'D': {'coords': (2, 3), 'nb_eleves': 6},
    'LYCEE': {'coords': (5, 5), 'nb_eleves': 0}
}

# Matrice des temps de trajet
TEMPS_TRAJET = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'LYCEE': 30},
    'B': {'A': 10, 'C': 8, 'D': 12, 'LYCEE': 25},
    'C': {'A': 15, 'B': 8, 'D': 7, 'LYCEE': 20},
    'D': {'A': 20, 'B': 12, 'C': 7, 'LYCEE': 15},
    'LYCEE': {'A': 30, 'B': 25, 'C': 20, 'D': 15}
}


arrets = {nom: Arret(nom, data['coords'], data['nb_eleves']) for nom, data in ARRETS.items()}



def visualiser_arrets(arrets, temps_trajet):
    plt.figure(figsize=(10, 8))
    
    # Affichage des arrêts
    for nom, arret in arrets.items():
        x, y = arret.coordonnees
        plt.scatter(x, y, s=arret.nb_eleves * 50, label=nom)
        plt.text(x + 0.1, y + 0.1, nom, fontsize=9)
    
    # Connexions
    for depart, destinations in temps_trajet.items():
        for arrivee, _ in destinations.items():
            x1, y1 = arrets[depart].coordonnees
            x2, y2 = arrets[arrivee].coordonnees
            plt.plot([x1, x2], [y1, y2], 'gray', linestyle='--', linewidth=0.5)
    
    # Mise en forme
    plt.scatter([arrets['LYCEE'].coordonnees[0]], [arrets['LYCEE'].coordonnees[1]], 
                s=200, c='red', label='Lycée')
    plt.legend()
    plt.title("Visualisation des arrêts et connexions")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()




def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances




def trouver_circuit_glouton(temps_trajet, start):
    visite = {start}
    circuit = [start]
    current = start
    
    while len(visite) < len(temps_trajet):
        next_stop = min(
            (stop for stop in temps_trajet[current] if stop not in visite),
            key=lambda stop, current=current: temps_trajet[current][stop]
        )
        circuit.append(next_stop)
        visite.add(next_stop)
        current = next_stop
    return circuit



def planifier_circuits(arrets, temps_trajet, capacite_max):
    circuits = []
    non_visites = set(arrets.keys())
    non_visites.remove('LYCEE')
    
    while non_visites:
        capacite_actuelle = 0
        circuit = []
        current = 'LYCEE'
        
        while non_visites:
            next_stop = min(
                (stop for stop in non_visites),
                key=lambda stop: temps_trajet[current][stop]
            )
            
            if capacite_actuelle + arrets[next_stop].nb_eleves <= capacite_max:
                circuit.append(next_stop)
                capacite_actuelle += arrets[next_stop].nb_eleves
                non_visites.remove(next_stop)
                current = next_stop
            else:
                # If the bus cannot take all students in one go, it will take as many as it can
                remaining_eleves = capacite_max - capacite_actuelle
                arrets[next_stop].nb_eleves -= remaining_eleves
                capacite_actuelle += remaining_eleves
                circuit.append(next_stop)
                current = next_stop
                break
        
        circuit.append('LYCEE')
        circuits.append(circuit)
    
    return circuits

# Test avec une capacité maximale de 10








