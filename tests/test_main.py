import unittest
from main import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        """Создание нового стека для каждого теста"""
        self.stack = Stack()

    def test_is_empty(self):
        """Проверка, что новый стек пуст"""
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        """Проверка добавления элемента в стек"""
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)

    def test_pop(self):
        """Проверка удаления элемента из стека"""
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertTrue(self.stack.is_empty())

    def test_pop_empty_stack(self):
        """Проверка, что возникает ошибка при попытке удалить элемент из пустого стека"""
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        """Проверка верхнего элемента стека"""
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertFalse(self.stack.is_empty())

    def test_peek_empty_stack(self):
        """Проверка, что возникает ошибка при попытке посмотреть верхний элемент пустого стека"""
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_size(self):
        """Проверка размера стека"""
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
