class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return self._length * 2 + self._width * 2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

