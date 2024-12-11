import unittest
from Dictionnaire import DicoABR

class TestDicoABR(unittest.TestCase):

    def setUp(self):
        # Configuration d'un arbre simple
        self.arbre_simple = DicoABR("chat", "animal domestique")
        self.arbre_simple.inserer("chien", "animal domestique")
        self.arbre_simple.inserer("oiseau", "animal volant")

        # Configuration d'un arbre complexe
        self.arbre_complexe = DicoABR("m", "milieu")
        mots_definitions = [
            ("a", "première lettre"),
            ("z", "dernière lettre"),
            ("e", "voyelle"),
            ("r", "consonne"),
            ("t", "consonne"),
            ("y", "consonne"),
            ("u", "voyelle"),
            ("i", "voyelle"),
            ("o", "voyelle"),
            ("p", "consonne"),
            ("q", "consonne"),
            ("s", "consonne"),
            ("d", "consonne"),
            ("f", "consonne"),
            ("g", "consonne"),
            ("h", "consonne"),
            ("j", "consonne"),
            ("k", "consonne"),
            ("l", "consonne"),
            ("n", "consonne"),
            ("b", "consonne"),
            ("v", "consonne"),
            ("c", "consonne"),
            ("x", "consonne"),
            ("w", "consonne")
        ]
        for mot, definition in mots_definitions:
            self.arbre_complexe.inserer(mot, definition)

    def test_inserer_simple(self):
        # Test de l'insertion dans un arbre simple
        self.arbre_simple.inserer("poisson", "animal aquatique")
        self.assertEqual(self.arbre_simple.rechercher("poisson"), "animal aquatique")

    def test_inserer_complexe(self):
        # Test de l'insertion dans un arbre complexe
        self.arbre_complexe.inserer("aa", "double a")
        self.assertEqual(self.arbre_complexe.rechercher("aa"), "double a")

    def test_rechercher_simple(self):
        # Test de la recherche dans un arbre simple
        self.assertEqual(self.arbre_simple.rechercher("chat"), "animal domestique")
        self.assertEqual(self.arbre_simple.rechercher("chien"), "animal domestique")
        self.assertEqual(self.arbre_simple.rechercher("oiseau"), "animal volant")
        self.assertIsNone(self.arbre_simple.rechercher("poisson"))

    def test_rechercher_complexe(self):
        # Test de la recherche dans un arbre complexe
        self.assertEqual(self.arbre_complexe.rechercher("a"), "première lettre")
        self.assertEqual(self.arbre_complexe.rechercher("z"), "dernière lettre")
        self.assertEqual(self.arbre_complexe.rechercher("e"), "voyelle")
        self.assertIsNone(self.arbre_complexe.rechercher("poisson"))

    def test_supprimer_simple(self):
        # Test de la suppression dans un arbre simple
        self.arbre_simple.supprimer("chien")
        self.assertIsNone(self.arbre_simple.rechercher("chien"))

    def test_supprimer_complexe(self):
        # Test de la suppression dans un arbre complexe
        self.arbre_complexe.supprimer("a")
        self.assertIsNone(self.arbre_complexe.rechercher("a"))
        self.arbre_complexe.supprimer("z")
        self.assertIsNone(self.arbre_complexe.rechercher("z"))

    def test_afficher_simple(self):
        # Test de l'affichage dans un arbre simple
        self.arbre_simple.afficher()

    def test_afficher_complexe(self):
        # Test de l'affichage dans un arbre complexe
        self.arbre_complexe.afficher()

    def test_len_simple(self):
        # Test de la longueur dans un arbre simple
        self.assertEqual(len(self.arbre_simple), 3)

    def test_len_complexe(self):
        # Test de la longueur dans un arbre complexe
        self.assertEqual(len(self.arbre_complexe), 26)

if __name__ == '__main__':
    unittest.main()