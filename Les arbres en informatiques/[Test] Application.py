import unittest
from MAIN import Arbre

class TestArbre(unittest.TestCase):

    def test_est_feuille(self):
        """
        Scénarios testés:
        - Un arbre avec un seul nœud est une feuille.
        - Après l'insertion d'un nœud à gauche, l'arbre n'est plus une feuille.
        - Après l'insertion d'un nœud à droite, l'arbre n'est toujours pas une feuille.
        - Les nœuds gauche et droit sont des feuilles après insertion.
        Assertions:
        - L'arbre initial est une feuille.
        - L'arbre n'est plus une feuille après l'insertion d'un nœud à gauche.
        - L'arbre n'est toujours pas une feuille après l'insertion d'un nœud à droite.
        - Les nœuds gauche et droit sont des feuilles après insertion.
        """

        arbre = Arbre(10)
        self.assertTrue(arbre.est_feuille())

        arbre.inserer(5)
        self.assertFalse(arbre.est_feuille())
        
        arbre.inserer(15)
        self.assertFalse(arbre.est_feuille())
        self.assertTrue(arbre.gauche.est_feuille())
        self.assertTrue(arbre.droite.est_feuille())

    def test_nombre_feuilles(self):
        """
        Scénario de test:
        1. Crée un arbre avec une racine de valeur 10.
        2. Vérifie que le nombre de feuilles est 1.
        3. Insère un nœud avec la valeur 5.
        4. Vérifie que le nombre de feuilles est toujours 1.
        5. Insère un nœud avec la valeur 15.
        6. Vérifie que le nombre de feuilles est maintenant 2.
        7. Insère un nœud avec la valeur 3 dans le sous-arbre gauche.
        8. Insère un nœud avec la valeur 20 dans le sous-arbre droit.
        9. Vérifie que le nombre de feuilles est toujours 2.
        10. Insère un nœud avec la valeur 30 dans le sous-arbre droit.
        11. Vérifie que le nombre de feuilles est maintenant 3.
        Assertions:
        - L'arbre a une feuille
        - L'arbre a une feuille
        - L'arbre a deux feuilles
        - L'arbre a deux feuilles
        - L'arbre a trois feuilles
        """
        
        arbre = Arbre(10)
        self.assertEqual(arbre.nombre_feuilles(), 1)

        arbre.inserer(5)
        self.assertEqual(arbre.nombre_feuilles(), 1)

        arbre.inserer(15)
        self.assertEqual(arbre.nombre_feuilles(), 2)

        arbre.gauche.inserer(3)
        arbre.droite.inserer(20)
        self.assertEqual(arbre.nombre_feuilles(), 2)

        arbre.droite.inserer(30)
        self.assertEqual(arbre.nombre_feuilles(), 3)

if __name__ == '__main__':
    unittest.main()