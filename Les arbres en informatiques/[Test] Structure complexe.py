import unittest
from MAIN import Arbre

class TestArbreComplex(unittest.TestCase):
    def test_initialization(self):
        """
        Teste l'initialisation d'un objet Arbre.
        Vérifie que :
        - Les attributs 'gauche' et 'droite' de l'arbre sont initialisés à None.
        - L'attribut 'valeur' de l'arbre est correctement initialisé avec la valeur donnée.
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
        1. Crée un arbre avec une valeur initiale de 10.
        2. Ajoute 10 nœuds à gauche de l'arbre, chaque nœud ayant une valeur décroissante de 1 par rapport au nœud précédent.
        3. Vérifie que chaque nœud gauche n'est pas None.
        4. Vérifie que la valeur de chaque nœud gauche est correcte (10 - i).
        Assertions:
        - Vérifie que le nœud gauche actuel n'est pas None.
        - Vérifie que la valeur du nœud gauche actuel est correcte.
        """

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
        """
        Teste la méthode set_droite de la classe Arbre.
        Scénario de test:
        1. Crée un arbre avec une valeur initiale de 10.
        2. Ajoute successivement des nœuds à droite avec des valeurs incrémentées de 1 jusqu'à 10.
        3. Vérifie que chaque nœud à droite n'est pas None et que sa valeur est correcte.
        Explications des assertions:
        - Vérifie que le nœud droit actuel n'est pas None.
        - Vérifie que la valeur du nœud droit actuel est égale à la valeur initiale plus l'incrément.
        """

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