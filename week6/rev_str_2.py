def reverse_str(st, pos=0):
    """
    Returns a new string that is the reverse of st
    When first called, the pos parameter must be zero
    """
    if pos == len(st):
        return ""

    return reverse_str(st, pos + 1) + st[pos]


print(reverse_str("recursion"))
