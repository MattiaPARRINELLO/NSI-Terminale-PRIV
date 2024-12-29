import unittest
from v2 import dijkstra, TEMPS_TRAJET

class TestDijkstra(unittest.TestCase):
    def test_dijkstra_from_A(self):
        expected = {'A': 0, 'B': 10, 'C': 15, 'D': 20, 'LYCEE': 30}
        result = dijkstra(TEMPS_TRAJET, 'A')
        self.assertEqual(result, expected)

    def test_dijkstra_from_B(self):
        expected = {'A': 10, 'B': 0, 'C': 8, 'D': 12, 'LYCEE': 25}
        result = dijkstra(TEMPS_TRAJET, 'B')
        self.assertEqual(result, expected)

    def test_dijkstra_from_C(self):
        expected = {'A': 15, 'B': 8, 'C': 0, 'D': 7, 'LYCEE': 20}
        result = dijkstra(TEMPS_TRAJET, 'C')
        self.assertEqual(result, expected)

    def test_dijkstra_from_D(self):
        expected = {'A': 20, 'B': 12, 'C': 7, 'D': 0, 'LYCEE': 15}
        result = dijkstra(TEMPS_TRAJET, 'D')
        self.assertEqual(result, expected)

    def test_dijkstra_from_LYCEE(self):
        expected = {'A': 30, 'B': 25, 'C': 20, 'D': 15, 'LYCEE': 0}
        result = dijkstra(TEMPS_TRAJET, 'LYCEE')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()