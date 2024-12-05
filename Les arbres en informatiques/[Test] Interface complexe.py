import unittest
from MAIN import Arbre

class TestArbreComplex(unittest.TestCase):

    def setUp(self):

        self.arbre = Arbre(1)
        current = self.arbre
        for i in range(2, 11):
            current.inserer(i)
            current = current.gauche

    def test_taille(self):
        self.assertEqual(self.arbre.taille(), 10)

    def test_profondeur(self):
        self.assertEqual(self.arbre.profondeur(), 10)

    def test_inserer(self):
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