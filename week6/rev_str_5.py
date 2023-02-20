def rec_reverse_str(st, pos):
    """
    Returns a new string that is the reverse of st
    When first called, the pos parameter must be zero
    """
    if pos == len(st):
        return ""

    return rec_reverse_str(st, pos+1) + st[pos]

def reverse_str(st):
    """
    Calls recursive reverse_str function with zero for the second parameter
    """
    return rec_reverse_str(st, 0)