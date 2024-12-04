import unittest

from Parcours import Arbre

class TestArbre(unittest.TestCase):
    
    def setUp(self):
        self.arbre = Arbre(1)
        self.arbre.inserer_direction(2, "gauche")
        self.arbre.inserer_direction(3, "droite")
        self.arbre.gauche.inserer_direction(4, "gauche")
        self.arbre.gauche.inserer_direction(5, "droite")
        self.arbre.droite.inserer_direction(6, "gauche")
        self.arbre.droite.inserer_direction(7, "droite")
    
    def test_parcours_prefixe(self):
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