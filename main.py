from cls_stack import Stack


def equalization(string: str) -> str:

    """
    Данная функция проверяет строчку из скобочек на баланс.
    Возвращает True или False
    """

    stack = Stack()
    status = True

    for element in string:

        if element in r"([{":
            stack.push(object=element)

        else:

            if stack.peek() == "(" and element == ")":
                stack.pop()
                continue

            if stack.peek() == "[" and element == "]":
                stack.pop()
                continue
            
            if stack.peek() == "{" and element == "}":
                stack.pop()
                continue
            
            status = False
            break

    if status and stack.size() == 0:
        return "Сбалансировано"
    else:
        return "Несбалансировано"


if __name__ == "__main__":

    """
    Точка входа
    """

    list_strings = [
        r"(((([{}]))))",
        r"[([])((([[[]]])))]{()}",
        r"{{[()]}}",
        r"}{}",
        r"{{[(])]}}",
        r"[[{())}]"
    ]

    for string in list_strings:
        print(f"Строка: {string}. Статус: {equalization(string)}")



