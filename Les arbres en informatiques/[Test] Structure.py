import unittest

from Structure import Arbre

class TestArbre(unittest.TestCase):
    def test_initialization(self):
        valeur = 10
        arbre = Arbre(valeur)
        self.assertIsNone(arbre.gauche)
        self.assertIsNone(arbre.droite)
        self.assertEqual(arbre.valeur, valeur)

    def test_set_gauche(self):
        valeur = 10
        arbre = Arbre(valeur)
        arbre.gauche = Arbre(5)
        self.assertIsNotNone(arbre.gauche)
        self.assertEqual(arbre.gauche.valeur, 5)

    def test_set_droite(self):
        valeur = 10
        arbre = Arbre(valeur)
        arbre.droite = Arbre(15)
        self.assertIsNotNone(arbre.droite)
        self.assertEqual(arbre.droite.valeur, 15)

if __name__ == '__main__':
    unittest.main()