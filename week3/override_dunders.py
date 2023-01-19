from inheritance import Rectangle, Square
from composition import Cube


def main():
    rect_1 = Rectangle(5, 8)
    repr(rect_1._length)
    str(rect_1._length)
    repr(rect_1)
    str(rect_1)
    cube_1 = Cube(7)
    repr(cube_1._face)
    print(repr(cube_1))
    print(str(cube_1))
    print(cube_1)
    cube_1.__repr__()
    rect_1.__repr__()



if __name__ == "__main__":
    main()
