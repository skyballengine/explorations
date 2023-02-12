def summer(ls, pos=0, sum_list=0):
    if pos == len(ls):
        return sum_list
    else:
        temp = ls[pos] + sum_list
        return summer(ls, pos + 1, temp)


ls_1 = [i for i in range(10)]
print(summer(ls_1))
