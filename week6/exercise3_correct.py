def bin_convert(num):
    """Converts a decimal number to a string giving its binary rpresentation"""
    print(num)
    if num == 0:
        return ''

    next_digit = str(num % 2)
    return bin_convert(num // 2) + next_digit


print(bin_convert(35))
