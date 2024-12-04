import unittest

from Interface import Arbre

class TestArbre(unittest.TestCase):

    def test_taille(self):
        arbre = Arbre(1)
        self.assertEqual(arbre.taille(), 1)
        arbre.inserer(2)
        self.assertEqual(arbre.taille(), 2)
        arbre.inserer(3)
        self.assertEqual(arbre.taille(), 3)

    def test_profondeur(self):
        arbre = Arbre(1)
        self.assertEqual(arbre.profondeur(), 1)
        arbre.inserer(2)
        self.assertEqual(arbre.profondeur(), 2)
        arbre.inserer(3)
        self.assertEqual(arbre.profondeur(), 2)
        arbre.inserer(4)
        self.assertEqual(arbre.profondeur(), 3)

    def test_inserer(self):
        arbre = Arbre(1)
        arbre.inserer(2)
        self.assertEqual(arbre.gauche.valeur, 2)
        arbre.inserer(3)
        self.assertEqual(arbre.droite.valeur, 3)
        arbre.gauche.inserer(4)
        self.assertEqual(arbre.gauche.gauche.valeur, 4)

    def test_inserer_direction(self):
        arbre = Arbre(1)
        arbre.inserer_direction(2, "gauche")
        self.assertEqual(arbre.gauche.valeur, 2)
        arbre.inserer_direction(3, "droite")
        self.assertEqual(arbre.droite.valeur, 3)

if __name__ == '__main__':
    unittest.main()