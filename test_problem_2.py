# https://www.youtube.com/watch?v=6tNS--WetLI

import unittest
from io import StringIO
import sys
from problem_2 import print_depth, recursive_print_depth, Person


class TestProblem2(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.person_a = Person("a", "b", None)
        self.person_b = Person("a", "b", self.person_a)
        self.data = {"key1": 1, "key2": {"key3": 1, "key4": {"key5": 4, "user": self.person_b}}}
        self.data1 = self.person_a

    def tearDown(self):
        del self.data
        del self.data1
        del self.person_a
        del self.person_b
        print('tearDown')

    def test_print_depth(self):
        """
        Test print depth method
        :return:
        """
        print('test_print_depth:: test assertion')
        captured_output = StringIO()
        sys.stdout = captured_output
        print_depth(self.data)
        sys.stdout = sys.__stdout__
        expected_result = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser: 3\nfirst_name: 4\nlast_name: 4\nfather: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

        print('test_print_depth:: test assertion for Person object only')
        captured_output = StringIO()
        sys.stdout = captured_output
        print_depth(self.data1)
        sys.stdout = sys.__stdout__
        expected_result = "first_name: 1\nlast_name: 1\nfather: 1\n"

        self.assertEqual(captured_output.getvalue(), expected_result)

        print('test_print_depth:: test type error')
        with self.assertRaises(TypeError):
            print_depth()

        print('test_print_depth:: test value error')
        with self.assertRaises(ValueError):
            print_depth(1)

    def test_recursive_print_depth(self):
        """
        Test recursive print depth method
        :return:
        """
        print('test_recursive_print_depth:: test assertion')
        captured_output = StringIO()
        sys.stdout = captured_output
        recursive_print_depth(self.data, depth=1)
        sys.stdout = sys.__stdout__
        expected_result = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser: 3\nfirst_name: 4\nlast_name: 4\nfather: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\n"

        self.assertEqual(captured_output.getvalue(), expected_result)

        print('test_recursive_print_depth:: test type error')
        with self.assertRaises(TypeError):
            recursive_print_depth(self.data)

        print('test_recursive_print_depth:: test value error')
        with self.assertRaises(ValueError):
            recursive_print_depth(self.data, '1')


if __name__ == '__main__':
    unittest.main()
