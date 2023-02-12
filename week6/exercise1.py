def summer(ls):
    if len(ls) == 0:
        return 0
    else:
        curr = ls[len(ls) - 1]
        return summer(ls[:len(ls) - 1]) + curr


ls_1 = [1, 2, 3, 4, 5]
print(summer(ls_1))
