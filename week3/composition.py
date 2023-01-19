from inheritance import Rectangle, Square


class Cube:
    def __init__(self, side):
        self._face = Square(side)

    def get_length(self):
        return self._face.get_length()

    def get_width(self):
        return self._face.get_width()

    def get_surface_area(self):
        return self._face.area() * 6

    def volume(self):
        return self._face.area() * self._face.get_length()


def main():
    rect_1 = Rectangle(5, 8)
    sq_1 = Square(5)
    cube_1 = Cube(5)
    print(f"\n Rectangle 1 Length = {rect_1.get_length()}\
                \n Rectangle 1 Width = {rect_1.get_width()}")
    print(f"\n Square 1 Length = {sq_1.get_length()}\
                \n Square 1 Width = {sq_1.get_width()}")
    print(f"\n Rectangle 1 Length = {rect_1.get_length()}\
                \n Rectangle 1 Width = {rect_1.get_width()}")
    print(f"\n Cube 1 Length = {cube_1.get_length()}\
                \n Cube 1 Width = {cube_1.get_width()}\
            \n Cube 1 Surface Area = {cube_1.get_surface_area()}\
          \n Cube 1 Volume = {cube_1.volume()}")


if __name__ == "__main__":
    main()
