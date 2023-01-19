import math

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

    def __repr__(self):
        return "Rectangle(" + repr(self._length) + ", " + repr(self._width) + ")"

    def __str__(self):
        return "A rectangle with a length of " + str(self._length) + " and a width of " + str(self._width)

    def __eq__(self, other):
        return math.isclose(self._length, other._length) and math.isclose(self._width, other._width)



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def main():
    rect_1 = Rectangle(5, 8)
    rect_2 = Rectangle(5, 8)
    rect_3 = Rectangle(5, 8.000000001)
    sq_1 = Square(5)
    print(f"\nRectangle 1 Length = {rect_1.get_length()}\
            \nRectangle 1 Width = {rect_1.get_width()}")
    print(f"\nSquare 1 Length = {sq_1.get_length()}\
            \nSquare 1 Width = {sq_1.get_width()}\n")
    repr(rect_1)
    if rect_1 == rect_2:
        print("Equal")
    else:
        print("Not equal")

    if rect_2 == rect_3:
        print("Equal")
    else:
        print("Not equal")



if __name__ == "__main__":
    main()
