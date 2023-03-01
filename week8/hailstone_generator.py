def hailstone(n):
    """
    Generator for hailstone sequence beginning with n
    :param num:
    :return:
    """

    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        yield int(n)


sequence = hailstone(10)
for i in sequence:
    print(i)

sequence = hailstone(280)
for i in range(10):
    print(next(sequence))
    