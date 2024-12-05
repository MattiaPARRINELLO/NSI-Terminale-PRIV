import unittest
from MAIN import Arbre

class TestArbreComplex(unittest.TestCase):
    def test_initialization(self):
        valeur = 10
        arbre = Arbre(valeur)
        self.assertIsNone(arbre.gauche)
        self.assertIsNone(arbre.droite)
        self.assertEqual(arbre.valeur, valeur)

    def test_set_gauche(self):
        valeur = 10
        arbre = Arbre(valeur)
        current = arbre
        for i in range(1, 11):
            current.gauche = Arbre(valeur - i)
            current = current.gauche
        current = arbre
        for i in range(1, 11):
            self.assertIsNotNone(current.gauche)
            self.assertEqual(current.gauche.valeur, valeur - i)
            current = current.gauche

    def test_set_droite(self):
        valeur = 10
        arbre = Arbre(valeur)
        current = arbre
        for i in range(1, 11):
            current.droite = Arbre(valeur + i)
            current = current.droite
        current = arbre
        for i in range(1, 11):
            self.assertIsNotNone(current.droite)
            self.assertEqual(current.droite.valeur, valeur + i)
            current = current.droite

if __name__ == '__main__':
    unittest.main()