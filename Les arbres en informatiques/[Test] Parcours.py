import unittest
from MAIN import Arbre

class TestArbre(unittest.TestCase):
    
    def setUp(self):
        """
        Configuration initiale de l'arbre binaire pour les tests.
        Cette méthode crée un arbre binaire avec la structure suivante :
                1
               / \
              2   3
             / \ / \
            4  5 6  7
        L'arbre est initialisé avec la racine ayant la valeur 1. Ensuite, les valeurs
        2 et 3 sont insérées respectivement à gauche et à droite de la racine. Les
        valeurs 4 et 5 sont insérées respectivement à gauche et à droite du nœud 2.
        Les valeurs 6 et 7 sont insérées respectivement à gauche et à droite du nœud 3.
        """

        self.arbre = Arbre(1)
        self.arbre.inserer_direction(2, "gauche")
        self.arbre.inserer_direction(3, "droite")
        self.arbre.gauche.inserer_direction(4, "gauche")
        self.arbre.gauche.inserer_direction(5, "droite")
        self.arbre.droite.inserer_direction(6, "gauche")
        self.arbre.droite.inserer_direction(7, "droite")
    
    def test_parcours_prefixe(self):
        """
        Teste la méthode parcours_prefixe de l'arbre.
        Scénario de test:
        - On s'attend à ce que le parcours préfixe de l'arbre retourne les valeurs dans l'ordre [1, 2, 4, 5, 3, 6, 7].
        - On redirige la fonction print pour capturer les valeurs imprimées par la méthode parcours_prefixe.
        - On restaure la fonction print originale après l'exécution du test.
        Assertions:
        - Vérifie que la liste des valeurs capturées (result) est égale à la liste attendue (expected_output).
        """

        expected_output = [1, 2, 4, 5, 3, 6, 7]
        result = []
        def mock_print(val):
            result.append(val)
        original_print = __builtins__.print
        __builtins__.print = mock_print
        self.arbre.parcours_prefixe()
        __builtins__.print = original_print
        self.assertEqual(result, expected_output)
    
    def test_parcours_infixe(self):
        """
        Teste la méthode parcours_infixe de la classe Arbre.
        Scénario de test:
        - On crée une liste `expected_output` qui contient l'ordre attendu des valeurs après un parcours infixe de l'arbre.
        - On redéfinit temporairement la fonction `print` pour capturer les valeurs imprimées par la méthode `parcours_infixe` dans une liste `result`.
        - On appelle la méthode `parcours_infixe` de l'arbre.
        - On rétablit la fonction `print` originale.
        - On compare la liste `result` avec la liste `expected_output` pour vérifier que le parcours infixe produit les valeurs attendues.
        Assertions:
        - Vérifie que la liste des valeurs obtenues par le parcours infixe correspond à la liste des valeurs attendues.
        """

        expected_output = [4, 2, 5, 1, 6, 3, 7]
        result = []
        def mock_print(val):
            result.append(val)
        original_print = __builtins__.print
        __builtins__.print = mock_print
        self.arbre.parcours_infixe()
        __builtins__.print = original_print
        self.assertEqual(result, expected_output)
    
    def test_parcours_postfixe(self):
        """
        Teste la méthode parcours_postfixe de la classe Arbre.
        Scénario de test:
        - On redirige la fonction print vers une fonction mock_print qui ajoute les valeurs imprimées à une liste result.
        - On appelle la méthode parcours_postfixe sur l'arbre.
        - On rétablit la fonction print originale.
        - On compare la liste result avec la sortie attendue [4, 5, 2, 6, 7, 3, 1] pour vérifier que le parcours postfixe est correct.
        Assertions:
        - Vérifie que la liste result obtenue après l'exécution de parcours_postfixe correspond à la liste attendue.
        """

        expected_output = [4, 5, 2, 6, 7, 3, 1]
        result = []
        def mock_print(val):
            result.append(val)
        original_print = __builtins__.print
        __builtins__.print = mock_print
        self.arbre.parcours_postfixe()
        __builtins__.print = original_print
        self.assertEqual(result, expected_output)
    
    def test_parcours_largeur(self):
        """
        Teste la méthode parcours_largeur de la classe Arbre.
        Scénario de test:
        - On s'attend à ce que la méthode parcours_largeur affiche les valeurs des nœuds de l'arbre
          dans l'ordre d'un parcours en largeur.
        - La sortie attendue est [1, 2, 3, 4, 5, 6, 7].
        Explications des assertions:
        - La fonction mock_print est utilisée pour capturer les valeurs imprimées par la méthode
          parcours_largeur.
        - La fonction print originale est temporairement remplacée par mock_print.
        - Après l'exécution de parcours_largeur, la fonction print est restaurée à son état original.
        - On vérifie que les valeurs capturées dans result correspondent à la sortie attendue
          en utilisant.
        """

        expected_output = [1, 2, 3, 4, 5, 6, 7]
        result = []
        def mock_print(val):
            result.append(val)
        original_print = __builtins__.print
        __builtins__.print = mock_print
        self.arbre.parcours_largeur()
        __builtins__.print = original_print
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()