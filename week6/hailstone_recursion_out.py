def hailstone(num):
    if num == 1:
        return 0

    if num % 2 == 0:
        return hailstone(num / 2) + 1

    else:
        return hailstone(num * 3 + 1) + 1


print(hailstone(20))
