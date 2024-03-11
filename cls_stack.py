class Stack():

    """
    Стек — абстрактный тип данных, представляющий список элементов,
    организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
    """

    def __init__(self) -> None:
        self.__stack__ = []

    def is_empty(self) -> None:

        """Проверка стека на пустоту. Метод возвращает True или False."""

        if bool(self.__stack__):
            return False
        else:
            return True

    def push(self, object: any) -> None:

        """Добавляет новый элемент на вершину стека. Метод ничего не возвращает."""

        self.__stack__.append(object)

    def pop(self) -> None:

        """Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека."""

        try:
            result = self.__stack__.pop()
        except IndexError:
            return "Stack is empty"
        else:
            return result

    def peek(self) -> None:

        """Возвращает верхний элемент стека, но не удаляет его. Стек не меняется."""

        try:
            result = self.__stack__[-1]
        except IndexError:
            return "Stack is empty"
        else:
            return result

    def size(self) -> None:

        """Возвращает количество элементов в стеке."""

        return len(self.__stack__)


if __name__ == "__main__":
    print("Чтобы использовать данный код - импортируйте в свой файл данный класс")