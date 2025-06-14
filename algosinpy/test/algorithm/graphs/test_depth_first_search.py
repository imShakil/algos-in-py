import unittest
from algosinpy.algorithm.graphs import depth_first_search


class DepthFirstSearchTestCase(unittest.TestCase):
    def test_dfs(self):
        graph = depth_first_search.Graph()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        graph.add_edge(2, 3)
        self.assertEqual(graph.dfs(2), [2, 0, 1, 3])


if __name__ == "__main__":
    unittest.main()
