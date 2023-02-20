def list_max(ls, max_num=0):
    if len(ls) == 0:
        return max_num
    else:
        if ls[-1] > max_num:
            max_num = ls[-1]
            return list_max(ls[: len(ls) - 1], max_num)

        else:
            return list_max(ls[: len(ls) - 1], max_num)