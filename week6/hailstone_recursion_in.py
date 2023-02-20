def hailstone(num, count=0):
    if num == 1:
        return 0

    if num % 2 == 0:
        count += 1
        return hailstone(num/2) + count
    else:
        count += 1
        return hailstone(num * 3 + 1) + count


print(hailstone(20))