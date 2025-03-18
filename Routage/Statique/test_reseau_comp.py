from route import Route
from routeur import Routeur
from reseau import Reseau

def test_reseau_complet():
    # 1. Créez un objet Reseau nommé "Entreprise_A"
    reseau = Reseau("Entreprise_A")

    # 2. Créez trois routeurs (R1, R2, R3)
    r1 = Routeur("R1")
    r2 = Routeur("R2")
    r3 = Routeur("R3")

    # 3. Configurez les routes sur chaque routeur
    r1.ajouter_route(Route("192.168.1.0", "255.255.255.0", "-", "eth0"))
    r1.ajouter_route(Route("192.168.2.0", "255.255.255.0", "192.168.1.254", "eth1"))
    r1.ajouter_route(Route("192.168.3.0", "255.255.255.0", "192.168.1.254", "eth1"))

    r2.ajouter_route(Route("192.168.2.0", "255.255.255.0", "-", "eth1"))
    r2.ajouter_route(Route("192.168.1.0", "255.255.255.0", "192.168.2.254", "eth0"))
    r2.ajouter_route(Route("192.168.3.0", "255.255.255.0", "192.168.3.254", "eth2"))

    r3.ajouter_route(Route("192.168.3.0", "255.255.255.0", "-", "eth2"))
    r3.ajouter_route(Route("192.168.1.0", "255.255.255.0", "192.168.3.254", "eth1"))
    r3.ajouter_route(Route("192.168.2.0", "255.255.255.0", "192.168.3.254", "eth1"))

    # 4. Ajoutez les routeurs au réseau
    reseau.ajouter_routeur(r1)
    reseau.ajouter_routeur(r2)
    reseau.ajouter_routeur(r3)

    # 5. Connectez les routeurs entre eux
    reseau.connecter_routeurs("R1", "eth1", "R2", "eth0")
    reseau.connecter_routeurs("R2", "eth2", "R3", "eth1")

    # 6. Affichez le réseau et son graphe
    print(reseau)
    reseau.generer_graphe()

    # 7. Effectuez les tests de transmission
    print("\n🔹 Test 1: Transmission locale (R1 -> R1)")
    reseau.simuler_transmission_pas_a_pas("192.168.1.10", "192.168.1.25", "R1")

    print("\n🔹 Test 2: Transmission vers réseau distant (R1 -> R2)")
    reseau.simuler_transmission_pas_a_pas("192.168.1.10", "192.168.2.25", "R1")

    print("\n🔹 Test 3: Transmission impossible (R1 -> Réseau inconnu)")
    reseau.simuler_transmission_pas_a_pas("192.168.1.10", "192.168.4.25", "R1")


if __name__ == "__main__":
    test_reseau_complet()