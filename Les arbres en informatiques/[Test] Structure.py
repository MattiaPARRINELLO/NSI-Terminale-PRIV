import unittest
from MAIN import Arbre

class TestArbre(unittest.TestCase):
    def test_initialization(self):
        """
        Teste l'initialisation d'un objet Arbre avec une valeur donnée.
        Scénario de test:
        - Crée un objet Arbre avec une valeur initiale de 10.
        - Vérifie que les attributs 'gauche' et 'droite' de l'arbre sont initialisés à None.
        - Vérifie que l'attribut 'valeur' de l'arbre est égal à la valeur donnée (10).
        Explications des assertions:
        - Vérifie que l'attribut 'gauche' de l'arbre est None.
        - Vérifie que l'attribut 'droite' de l'arbre est None.
        - Vérifie que l'attribut 'valeur' de l'arbre est égal à 10.
        """

        valeur = 10
        arbre = Arbre(valeur)
        self.assertIsNone(arbre.gauche)
        self.assertIsNone(arbre.droite)
        self.assertEqual(arbre.valeur, valeur)

    def test_set_gauche(self):
        """
        Teste la méthode set_gauche de la classe Arbre.
        Scénario de test:
        - Crée un arbre avec une valeur racine de 10.
        - Ajoute un sous-arbre gauche avec une valeur de 5.
        - Vérifie que le sous-arbre gauche n'est pas None.
        - Vérifie que la valeur du sous-arbre gauche est bien 5.
        Assertions:
        - Vérifie que le sous-arbre gauche a été correctement assigné et n'est pas None.
        - Vérifie que la valeur du sous-arbre gauche est bien celle attendue, c'est-à-dire 5.
        """

        valeur = 10
        arbre = Arbre(valeur)
        arbre.gauche = Arbre(5)
        self.assertIsNotNone(arbre.gauche)
        self.assertEqual(arbre.gauche.valeur, 5)

    def test_set_droite(self):
        """
        Teste la méthode set_droite de la classe Arbre.
        Scénario de test:
        1. Crée un arbre avec une valeur initiale de 10.
        2. Définit le sous-arbre droit avec une nouvelle instance d'Arbre ayant la valeur 15.
        3. Vérifie que le sous-arbre droit n'est pas None.
        4. Vérifie que la valeur du sous-arbre droit est bien 15.
        Explications des assertions:
        - Vérifie que le sous-arbre droit a été correctement assigné et n'est pas None.
        - Vérifie que la valeur du sous-arbre droit est bien celle attendue, c'est-à-dire 15.
        """

        valeur = 10
        arbre = Arbre(valeur)
        arbre.droite = Arbre(15)
        self.assertIsNotNone(arbre.droite)
        self.assertEqual(arbre.droite.valeur, 15)

if __name__ == '__main__':
    unittest.main()