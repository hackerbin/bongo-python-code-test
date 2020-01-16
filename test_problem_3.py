# https://www.youtube.com/watch?v=6tNS--WetLI

import unittest
from io import StringIO
import sys
from problem_3 import lca, Node


class TestProblem3(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.node1 = Node(1, None)
        self.node2 = Node(2, self.node1)
        self.node3 = Node(3, self.node1)
        self.node4 = Node(4, self.node2)
        self.node5 = Node(5, self.node2)
        self.node6 = Node(6, self.node3)
        self.node7 = Node(7, self.node3)
        self.node8 = Node(8, self.node4)
        self.node9 = Node(9, self.node4)

    def tearDown(self):
        print('tearDown')

    def test_lca(self):
        """
        Test lca method
        :return:
        """
        print('test_lca:: test assertion return node')
        self.assertEqual(lca(self.node6, self.node7), self.node3)

        print('test_lca:: test assertion return value')
        self.assertEqual(lca(self.node6, self.node7).value, 3)

        print('test_lca:: test assertion console print output')
        captured_output = StringIO()
        sys.stdout = captured_output
        lca(self.node6, self.node7)
        sys.stdout = sys.__stdout__
        expected_result = "3\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

        print('test_lca:: test assertion return node')
        self.assertEqual(lca(self.node3, self.node7), self.node3)

        print('test_lca:: test assertion return value')
        self.assertEqual(lca(self.node3, self.node7).value, 3)

        print('test_lca:: test assertion console print output')
        captured_output = StringIO()
        sys.stdout = captured_output
        lca(self.node6, self.node7)
        sys.stdout = sys.__stdout__
        expected_result = "3\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

        print('test_lca:: test assertion return node for same node')
        self.assertEqual(lca(self.node7, self.node7), self.node7)

        print('test_lca:: test assertion return value for same node')
        self.assertEqual(lca(self.node7, self.node7).value, 7)

        print('test_lca:: test assertion console print output for same node')
        captured_output = StringIO()
        sys.stdout = captured_output
        lca(self.node7, self.node7)
        sys.stdout = sys.__stdout__
        expected_result = "7\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

        print('test_lca:: test type error')
        with self.assertRaises(TypeError):
            lca(self.node7)
            lca()

        print('test_lca:: test value error')
        with self.assertRaises(ValueError):
            lca(1, self.node7)
            lca(1, 2)


if __name__ == '__main__':
    unittest.main()
