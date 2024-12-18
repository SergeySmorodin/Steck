class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Возвращает True, если стек пуст, иначе False
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Добавляет новый элемент на вершину стека
        """
        self.items.append(item)

    def pop(self):
        """
        Удаляет верхний элемент стека и
        возвращает его
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Возвращает верхний элемент стека, не удаляя его
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """
        Возвращает количество элементов в стеке
        """
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())  # True
    stack.push(1)
    stack.push(2)
    print(stack.peek())  # 2
    print(stack.size())  # 2
    print(stack.pop())  # 2
    print(stack.size())  # 1
    print(stack.is_empty())  # False
