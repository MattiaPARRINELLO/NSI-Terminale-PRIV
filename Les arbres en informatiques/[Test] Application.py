import unittest

from Application import Arbre

class TestArbre(unittest.TestCase):

    def test_est_feuille(self):
        # Test with a single node 
        arbre = Arbre(10)
        self.assertTrue(arbre.est_feuille())
        
        # Test with a tree with one child
        arbre.inserer(5)
        self.assertFalse(arbre.est_feuille())

        # Test with a tree with two children
        arbre.inserer(15)
        self.assertFalse(arbre.est_feuille())

        # Test leaf nodes
        self.assertTrue(arbre.gauche.est_feuille())
        self.assertTrue(arbre.droite.est_feuille())

    def test_nombre_feuilles(self):
        # Test with a single node tree
        arbre = Arbre(10)
        self.assertEqual(arbre.nombre_feuilles(), 1)

        # Test with a tree with one child
        arbre.inserer(5)
        self.assertEqual(arbre.nombre_feuilles(), 1)

        # Test with a tree with two children
        arbre.inserer(15)
        self.assertEqual(arbre.nombre_feuilles(), 2)

        # Test with a larger tree
        arbre.gauche.inserer(3)
        arbre.droite.inserer(20)
        self.assertEqual(arbre.nombre_feuilles(), 2)
        arbre.droite.inserer(30)
        self.assertEqual(arbre.nombre_feuilles(), 3)

if __name__ == '__main__':
    unittest.main()