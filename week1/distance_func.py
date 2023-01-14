from math import sqrt

def distance(x_first, y_first, x_second, y_second):
    x_distance = x_first - x_second
    y_distance = y_first - y_second
    c_distance = (x_distance ** 2) + (y_distance ** 2)
    return sqrt(c_distance)

def main():
    d1 = distance(3, 5, -1, 2)
    d2 = distance(0, 0, 0, 0)
    print(d1)
    print(d2)

if __name__ == "__main__":
    main()
