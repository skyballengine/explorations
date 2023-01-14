class Box:
    """Represents a box"""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        return self._length * self._width * self._height

    def surface_area(self):
        x_area = (self._length * self._width) * 2
        y_area = (self._height * self._width) * 4
        return x_area + y_area

tesseract = Box(8, 8, 8)
print(tesseract.volume())
print(tesseract.surface_area())