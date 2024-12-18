from balanced import is_balanced
import unittest


class TestIsBalanced(unittest.TestCase):

    def test_balanced_brackets(self):
        self.assertEqual(is_balanced("(((([{}]))))"), "Сбалансированно")
        self.assertEqual(is_balanced("[([])((([[[]]])))]{()}"), "Сбалансированно")
        self.assertEqual(is_balanced("{{[()]}}"), "Сбалансированно")

    def test_unbalanced_brackets(self):
        self.assertEqual(is_balanced("}{}"), "Несбалансированно")
        self.assertEqual(is_balanced("{{[(])]}}"), "Несбалансированно")
        self.assertEqual(is_balanced("[[{())}]"), "Несбалансированно")

    def test_empty_string(self):
        self.assertEqual(is_balanced(""), "Сбалансированно")


if __name__ == '__main__':
    unittest.main()
