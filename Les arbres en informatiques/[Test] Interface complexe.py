import unittest
from MAIN import Arbre

class TestArbreComplex(unittest.TestCase):

    def setUp(self):
        """
        Configuration initiale pour les tests unitaires.
        Cette méthode initialise un arbre binaire avec des valeurs de 1 à 10.
        Chaque nouvelle valeur est insérée à gauche du nœud courant.
        """

        self.arbre = Arbre(1)
        current = self.arbre
        for i in range(2, 11):
            current.inserer(i)
            current = current.gauche

    def test_taille(self):
        """
        Teste la méthode `taille` de l'arbre.
        Scénario de test:
        - On suppose que l'arbre contient 10 éléments.
        Explications des assertions:
        - Vérifie que la méthode `taille` de l'arbre retourne bien 10.
        """
        
        self.assertEqual(self.arbre.taille(), 10)

    def test_profondeur(self):
        """
        Teste la méthode profondeur de l'arbre.
        Scénario de test:
        - On suppose que l'arbre a une profondeur de 10.
        Explications des assertions:
        - Vérifie que la méthode profondeur() de l'arbre retourne bien 10.
        """

        self.assertEqual(self.arbre.profondeur(), 10)

    def test_inserer(self):
        """
        Teste la méthode 'inserer' de la classe Arbre.
        Scénario de test:
        1. Insère la valeur 11 dans l'arbre à droite de la racine.
        2. Vérifie que la valeur du nœud droit de la racine est bien 11.
        3. Insère la valeur 12 dans l'arbre à gauche de la racine.
        4. Vérifie que la valeur du nœud droit du nœud gauche de la racine est bien 12.
        Explications des assertions:
        - Vérifie que la valeur du nœud droit de la racine est 11 après l'insertion.
        - Vérifie que la valeur du nœud droit du nœud gauche de la racine est 12 après l'insertion.
        """

        self.arbre.inserer(11)
        self.assertEqual(self.arbre.droite.valeur, 11)
        self.arbre.gauche.inserer(12)
        self.assertEqual(self.arbre.gauche.droite.valeur, 12)

    def test_inserer_direction(self):
        self.arbre.inserer_direction(11, "droite")
        self.assertEqual(self.arbre.droite.valeur, 11)
        self.arbre.gauche.inserer_direction(12, "droite")
        self.assertEqual(self.arbre.gauche.droite.valeur, 12)

if __name__ == '__main__':
    unittest.main()