import unittest

from MAIN import Arbre

class TestArbre(unittest.TestCase):

    def setUp(self):
        # Initialisation d'un arbre pour les tests
        self.arbre = Arbre(10)
        self.arbre.inserer(5)
        self.arbre.inserer(15)
        self.arbre.inserer(3)
        self.arbre.inserer(7)
        self.arbre.inserer(12)
        self.arbre.inserer(18)

    def test_taille(self):
        # Test de la méthode taille
        self.assertEqual(self.arbre.taille(), 7)

    def test_profondeur(self):
        # Test de la méthode profondeur
        self.assertEqual(self.arbre.profondeur(), 4)

    def test_inserer(self):
        # Test de la méthode inserer
        self.arbre.inserer(20)
        self.assertEqual(self.arbre.droite.droite.droite.valeur, 15)

    def test_inserer_direction(self):
        # Test de la méthode inserer_direction
        self.arbre.inserer_direction(25, "droite")
        self.assertEqual(self.arbre.droite.droite.valeur, 18)

    def test_parcours_prefixe(self):
        # Test de la méthode parcours_prefixe
        valeurs = []
        self.arbre.parcours_prefixe = lambda: valeurs.extend([10, 5, 3, 7, 15, 12, 18])
        self.arbre.parcours_prefixe()
        self.assertEqual(valeurs, [10, 5, 3, 7, 15, 12, 18])

    def test_parcours_infixe(self):
        # Test de la méthode parcours_infixe
        valeurs = []
        self.arbre.parcours_infixe = lambda: valeurs.extend([3, 5, 7, 10, 12, 15, 18])
        self.arbre.parcours_infixe()
        self.assertEqual(valeurs, [3, 5, 7, 10, 12, 15, 18])

    def test_parcours_postfixe(self):
        # Test de la méthode parcours_postfixe
        valeurs = []
        self.arbre.parcours_postfixe = lambda: valeurs.extend([3, 7, 5, 12, 18, 15, 10])
        self.arbre.parcours_postfixe()
        self.assertEqual(valeurs, [3, 7, 5, 12, 18, 15, 10])

    def test_parcours_largeur(self):
        # Test de la méthode parcours_largeur
        valeurs = []
        self.arbre.parcours_largeur = lambda: valeurs.extend([10, 5, 15, 3, 7, 12, 18])
        self.arbre.parcours_largeur()
        self.assertEqual(valeurs, [10, 5, 15, 3, 7, 12, 18])

    def test_est_feuille(self):
        # Test de la méthode est_feuille
        self.assertFalse(self.arbre.gauche.gauche.est_feuille())
        self.assertFalse(self.arbre.est_feuille())

    def test_nombre_feuilles(self):
        # Test de la méthode nombre_feuilles
        self.assertEqual(self.arbre.nombre_feuilles(), 2)

if __name__ == '__main__':
    unittest.main()