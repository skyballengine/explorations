from inheritance import Rectangle

class Carpet:
    def __init__(self, rect_obj, cost_sq_ft):
        self._size = rect_obj
        self._cost_per_sq_foot = cost_sq_ft

    def get_size(self):
        return self._size

    def get_cost_per_sq_foot(self):
        return self._cost_per_sq_foot

    def cost(self):
        return self._cost_per_sq_foot * self._size.area()

    