import unittest
from MAIN import Arbre

class TestArbreComplex(unittest.TestCase):

    def test_est_feuille_complex(self):
        """
        Scénario de test :
        1. Crée un arbre avec une racine de valeur 10.
        2. Insère 100000 valeurs décroissantes dans le sous-arbre gauche.
        3. Vérifie que le dernier nœud inséré est une feuille.
        4. Vérifie que les 10 premiers nœuds ne sont pas des feuilles.
        5. Vérifie que la racine n'est pas une feuille.
        """
        
        arbre = Arbre(10)
        current = arbre
        for i in range(100000):
            current.inserer(i)
            current = current.gauche

        self.assertTrue(current.est_feuille())

        current = arbre
        for i in range(9):
            self.assertFalse(current.est_feuille())
            current = current.gauche

        self.assertFalse(arbre.est_feuille())

if __name__ == '__main__':
    unittest.main()