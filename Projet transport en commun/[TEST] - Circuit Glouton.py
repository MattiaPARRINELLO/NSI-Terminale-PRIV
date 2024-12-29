import unittest
from v2 import trouver_circuit_glouton, TEMPS_TRAJET

class TestTrouverCircuitGlouton(unittest.TestCase):
    def test_circuit_glouton(self):
        expected_circuit = ['A', 'B', 'C', 'D', 'LYCEE']
        result = trouver_circuit_glouton(TEMPS_TRAJET, 'A')
        self.assertEqual(result, expected_circuit)

    def test_circuit_glouton_start_B(self):
        expected_circuit = ['B', 'C', 'D', 'LYCEE', 'A']
        result = trouver_circuit_glouton(TEMPS_TRAJET, 'B')
        self.assertEqual(result, expected_circuit)

    def test_circuit_glouton_start_C(self):
        expected_circuit = ['C', 'D', 'B', 'A', 'LYCEE']
        result = trouver_circuit_glouton(TEMPS_TRAJET, 'C')
        self.assertEqual(result, expected_circuit)

    def test_circuit_glouton_start_D(self):
        expected_circuit = ['D', 'C', 'B', 'A', 'LYCEE']
        result = trouver_circuit_glouton(TEMPS_TRAJET, 'D')
        self.assertEqual(result, expected_circuit)

if __name__ == '__main__':
    unittest.main()