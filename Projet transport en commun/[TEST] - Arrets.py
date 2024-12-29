import unittest
from v2 import Arret

class TestArret(unittest.TestCase):
    def test_arret_initialization(self):
        arret = Arret("A", (0, 0), 5)
        self.assertEqual(arret.nom, "A")
        self.assertEqual(arret.coordonnees, (0, 0))
        self.assertEqual(arret.nb_eleves, 5)

    def test_arret_repr(self):
        arret = Arret("A", (0, 0), 5)
        self.assertEqual(repr(arret), "Arret(A, (0, 0), 5 élèves)")

if __name__ == '__main__':
    unittest.main()