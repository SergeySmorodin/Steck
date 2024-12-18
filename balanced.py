from main import Stack


def is_balanced(_string):
    stack = Stack()
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in _string:
        if char in brackets.values():  # Если открывающая скобка
            stack.push(char)
        elif char in brackets.keys():  # Если закрывающая скобка
            if stack.is_empty() or stack.pop() != brackets[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == "__main__":
    input_string = input("Введите последовательность скобок: ")
    result = is_balanced(input_string)
    print(result)
