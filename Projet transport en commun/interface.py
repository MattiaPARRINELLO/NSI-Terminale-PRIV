import streamlit as st
import matplotlib.pyplot as plt

# Données des arrêts
ARRETS = {
    'A': {'coords': (0, 0), 'nb_eleves': 5},
    'B': {'coords': (1, 2), 'nb_eleves': 3},
    'C': {'coords': (3, 1), 'nb_eleves': 4},
    'D': {'coords': (2, 3), 'nb_eleves': 6},
    'LYCEE': {'coords': (5, 5), 'nb_eleves': 0}
}

TEMPS_TRAJET = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'LYCEE': 30},
    'B': {'A': 10, 'C': 8, 'D': 12, 'LYCEE': 25},
    'C': {'A': 15, 'B': 8, 'D': 7, 'LYCEE': 20},
    'D': {'A': 20, 'B': 12, 'C': 7, 'LYCEE': 15},
    'LYCEE': {'A': 30, 'B': 25, 'C': 20, 'D': 15}
}

# Classe Arret
class Arret:
    def __init__(self, nom, coordonnees, nb_eleves):
        self.nom = nom
        self.coordonnees = coordonnees
        self.nb_eleves = nb_eleves

arrets = {nom: Arret(nom, data['coords'], data['nb_eleves']) for nom, data in ARRETS.items()}

# Visualisation des arrêts
def visualiser_arrets(arrets, circuits=None):
    plt.figure(figsize=(10, 8))
    
    # Points et noms des arrêts
    for nom, arret in arrets.items():
        x, y = arret.coordonnees
        plt.scatter(x, y, s=arret.nb_eleves * 50, label=f"{nom} ({arret.nb_eleves} élèves)")
        plt.text(x + 0.1, y + 0.1, nom, fontsize=9)
    
    # Dessiner les circuits si fournis
    if circuits:
        for circuit in circuits:
            coords = [arrets[stop].coordonnees for stop in circuit]
            x, y = zip(*coords)
            plt.plot(x, y, marker='o')
    
    # Lycée en rouge
    plt.scatter([arrets['LYCEE'].coordonnees[0]], [arrets['LYCEE'].coordonnees[1]], 
                s=200, c='red', label='Lycée')
    plt.legend()
    plt.title("Visualisation des arrêts et des circuits")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    st.pyplot(plt)

# Algorithmes
def trouver_circuit_glouton(temps_trajet, start):
    visite = {start}
    circuit = [start]
    current = start
    
    while len(visite) < len(temps_trajet):
        next_stop = min(
            (stop for stop in temps_trajet[current] if stop not in visite),
            key=lambda stop: temps_trajet[current][stop]
        )
        circuit.append(next_stop)
        visite.add(next_stop)
        current = next_stop
    
    circuit.append(start)  # Retour au départ
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
                remaining_eleves = capacite_max - capacite_actuelle
                arrets[next_stop].nb_eleves -= remaining_eleves
                capacite_actuelle += remaining_eleves
                circuit.append(next_stop)
                current = next_stop
                break
        
        circuit.append('LYCEE')
        circuits.append(circuit)
    
    return circuits

# Interface Streamlit
st.title("Optimisation du réseau de transport scolaire")

# Paramètres utilisateur
st.sidebar.header("Paramètres")
capacite_max = st.sidebar.slider("Capacité maximale du bus", 1, 20, 10)
algo = st.sidebar.selectbox("Algorithme", ["Circuit Glouton", "Optimisation Capacités"])

# Choix de l'algorithme
if algo == "Circuit Glouton":
    circuit = trouver_circuit_glouton(TEMPS_TRAJET, 'LYCEE')
    circuits = [circuit]
else:
    circuits = planifier_circuits(arrets, TEMPS_TRAJET, capacite_max)

# Affichage
st.subheader("Visualisation des circuits")
visualiser_arrets(arrets, circuits)

st.subheader("Résultats des circuits")
for i, circuit in enumerate(circuits, start=1):
    st.write(f"Circuit {i}: {' -> '.join(circuit)}")
