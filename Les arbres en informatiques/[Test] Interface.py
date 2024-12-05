import unittest
from MAIN import Arbre

class TestArbre(unittest.TestCase):

    def test_taille(self):
        """
        Teste la méthode taille() de la classe Arbre.
        Scénario de test:
        1. Crée un arbre avec une racine de valeur 1.
        2. Vérifie que la taille de l'arbre est 1.
        3. Insère un nouveau nœud avec la valeur 2.
        4. Vérifie que la taille de l'arbre est maintenant 2.
        5. Insère un autre nœud avec la valeur 3.
        6. Vérifie que la taille de l'arbre est maintenant 3.
        Explications des assertions:
        - Vérifie que la taille de l'arbre est 1 après l'initialisation.
        - Vérifie que la taille de l'arbre est 2 après l'insertion du deuxième nœud.
        - Vérifie que la taille de l'arbre est 3 après l'insertion du troisième nœud.
        """

        arbre = Arbre(1)
        self.assertEqual(arbre.taille(), 1)
        arbre.inserer(2)
        self.assertEqual(arbre.taille(), 2)
        arbre.inserer(3)
        self.assertEqual(arbre.taille(), 3)

    def test_profondeur(self):
        """
        Teste la méthode profondeur de la classe Arbre.
        Scénario de test:
        1. Crée un arbre avec une racine de valeur 1.
        2. Vérifie que la profondeur de l'arbre est 1.
        3. Insère un nœud avec la valeur 2.
        4. Vérifie que la profondeur de l'arbre est 2.
        5. Insère un nœud avec la valeur 3.
        6. Vérifie que la profondeur de l'arbre reste 2 (car il est inséré au même niveau que 2).
        7. Insère un nœud avec la valeur 4.
        8. Vérifie que la profondeur de l'arbre est 3 (car il est inséré à un niveau plus profond).
        Explications des assertions:
        - Vérifie que la profondeur initiale de l'arbre est correcte.
        - Vérifie que la profondeur initiale de l'arbre est correcte.
        - Vérifie que la profondeur initiale de l'arbre est correcte.
        - Vérifie que la profondeur augmente correctement après l'insertion de 2.
        - Vérifie que l'insertion de 3 ne change pas la profondeur car il est au même niveau que 2.
        - Vérifie que l'insertion de 4 augmente la profondeur de l'arbre.
        """
        
        
        
        arbre = Arbre(1)
        self.assertEqual(arbre.profondeur(), 1)
        arbre.inserer(2)
        self.assertEqual(arbre.profondeur(), 2)
        arbre.inserer(3)
        self.assertEqual(arbre.profondeur(), 2)
        arbre.inserer(4)
        self.assertEqual(arbre.profondeur(), 3)

    def test_inserer(self):
        """
        Teste la méthode inserer de la classe Arbre.
        Scénario de test:
        1. Crée un arbre avec une valeur racine de 1.
        2. Insère la valeur 2 dans l'arbre.
        3. Vérifie que la valeur du nœud gauche de la racine est 2.
        4. Insère la valeur 3 dans l'arbre.
        5. Vérifie que la valeur du nœud droit de la racine est 3.
        6. Insère la valeur 4 dans le nœud gauche de la racine.
        7. Vérifie que la valeur du nœud gauche du nœud gauche de la racine est 4.
        Explications des assertions:
        - Vérifie que la valeur du nœud gauche de la racine est bien 2 après l'insertion.
        - Vérifie que la valeur du nœud droit de la racine est bien 3 après l'insertion.
        - Vérifie que la valeur du nœud gauche du nœud gauche de la racine est bien 4 après l'insertion.
        """

        arbre = Arbre(1)
        arbre.inserer(2)
        self.assertEqual(arbre.gauche.valeur, 2)
        arbre.inserer(3)
        self.assertEqual(arbre.droite.valeur, 3)
        arbre.gauche.inserer(4)
        self.assertEqual(arbre.gauche.gauche.valeur, 4)

    def test_inserer_direction(self):
        """
        Teste la méthode inserer_direction de la classe Arbre.
        Scénario de test:
        1. Crée un arbre avec une valeur racine de 1.
        2. Insère la valeur 2 à gauche de la racine.
        3. Vérifie que la valeur du nœud gauche est bien 2.
        4. Insère la valeur 3 à droite de la racine.
        5. Vérifie que la valeur du nœud droit est bien 3.
        Explications des assertions:
        - Vérifie que la valeur du nœud gauche de l'arbre est 2 après l'insertion.
        - Vérifie que la valeur du nœud droit de l'arbre est 3 après l'insertion.
        """

        arbre = Arbre(1)
        arbre.inserer_direction(2, "gauche")
        self.assertEqual(arbre.gauche.valeur, 2)
        arbre.inserer_direction(3, "droite")
        self.assertEqual(arbre.droite.valeur, 3)

if __name__ == '__main__':
    unittest.main()