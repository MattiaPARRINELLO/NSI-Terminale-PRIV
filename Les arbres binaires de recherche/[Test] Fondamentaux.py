import unittest
from Fondamentaux import ABR

class TestABR(unittest.TestCase):
    
    def test_inserer_et_rechercher_simple(self):
        # Test avec un arbre simple
        arbre = ABR(10)
        arbre.inserer(5)
        arbre.inserer(15)
        
        # Vérifie que les valeurs existent dans l'arbre
        self.assertTrue(arbre.rechercher(10))
        self.assertTrue(arbre.rechercher(5))
        self.assertTrue(arbre.rechercher(15))
        
        # Vérifie que les valeurs n'existent pas dans l'arbre
        self.assertFalse(arbre.rechercher(20))
        self.assertFalse(arbre.rechercher(0))
    
    def test_inserer_et_rechercher_complexe(self):
        # Test avec un arbre plus complexe
        valeurs = [20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37]
        arbre = ABR(20)
        for valeur in valeurs[1:]:
            arbre.inserer(valeur)
        
        # Vérifie que toutes les valeurs existent dans l'arbre
        for valeur in valeurs:
            self.assertTrue(arbre.rechercher(valeur))
        
        # Vérifie que certaines valeurs n'existent pas dans l'arbre
        self.assertFalse(arbre.rechercher(0))
        self.assertFalse(arbre.rechercher(40))
        self.assertFalse(arbre.rechercher(22))
        self.assertFalse(arbre.rechercher(8))
        
    def test_inserer_et_rechercher_grand_arbre(self):
        # Test avec un grand arbre
        arbre = ABR(50000)
        for i in range(100000):
            if i != 50000:  # 50000 is already the root
                arbre.inserer(i)
        
        # Vérifie que la valeur 99999 existe dans l'arbre
        self.assertTrue(arbre.rechercher(99999))
        
        # Vérifie que certaines valeurs n'existent pas dans l'arbre
        self.assertFalse(arbre.rechercher(100000))
        self.assertFalse(arbre.rechercher(-1))
if __name__ == '__main__':
    unittest.main()
