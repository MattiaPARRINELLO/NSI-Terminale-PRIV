import unittest
from v2 import planifier_circuits, Arret

class TestPlanifierCircuits(unittest.TestCase):
    def setUp(self):
        self.arrets = {
            'A': Arret('A', (0, 0), 5),
            'B': Arret('B', (1, 2), 3),
            'C': Arret('C', (3, 1), 4),
            'D': Arret('D', (2, 3), 6),
            'LYCEE': Arret('LYCEE', (5, 5), 0)
        }
        self.temps_trajet = {
            'A': {'B': 10, 'C': 15, 'D': 20, 'LYCEE': 30},
            'B': {'A': 10, 'C': 8, 'D': 12, 'LYCEE': 25},
            'C': {'A': 15, 'B': 8, 'D': 7, 'LYCEE': 20},
            'D': {'A': 20, 'B': 12, 'C': 7, 'LYCEE': 15},
            'LYCEE': {'A': 30, 'B': 25, 'C': 20, 'D': 15}
        }

    def test_planifier_circuits(self):
        expected_circuits = [['D', 'LYCEE'], ['D', 'C', 'B', 'LYCEE'], ['B', 'A', 'LYCEE'], ['A', 'LYCEE']]
        result = planifier_circuits(self.arrets, self.temps_trajet, capacite_max=5)
        self.assertEqual(result, expected_circuits)

    def test_planifier_circuits_large_capacity(self):
        expected_circuits = [['D', 'C', 'B', 'A', 'LYCEE']]
        result = planifier_circuits(self.arrets, self.temps_trajet, capacite_max=20)
        self.assertEqual(result, expected_circuits)

    def test_planifier_circuits_no_capacity(self):

        expected_circuits = [['D', 'LYCEE'], ['D', 'LYCEE'], ['D', 'LYCEE'], ['D', 'LYCEE'], ['D', 'LYCEE'], ['D', 'C', 'LYCEE'], ['C', 'LYCEE'], ['C', 'LYCEE'], ['C', 'LYCEE'], ['C', 'B', 'LYCEE'], ['B', 'LYCEE'], ['B', 'LYCEE'], ['B', 'A', 'LYCEE'], ['A', 'LYCEE'], ['A', 'LYCEE'], ['A', 'LYCEE'], ['A', 'LYCEE'], ['A', 'LYCEE']]
        result = planifier_circuits(self.arrets, self.temps_trajet, capacite_max=1)
        self.assertEqual(result, expected_circuits)

if __name__ == '__main__':
    unittest.main()