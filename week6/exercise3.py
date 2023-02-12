"""
Write a recursive function named bin_convert that takes a non-negative integer as its parameter
and returns a string giving the binary representation of that number.
"""


def bin_convert(non_neg_int, bin_str='0'):
    one = "1"
    zero = "0"
    if non_neg_int == 0:
        return bin_str
    else:
        bin_str_list = bin_str.split()
        if bin_str[-1] == zero:
            bin_str_list[-1] = one
            bin_str = "".join(bin_str_list)
            return bin_convert(non_neg_int - 1, bin_str)

        else:
            bin_str_list = bin_str.split()
            bin_str_list[-1] = zero
            for i in range(len(bin_str) - 2, 0, -1):
                if bin_str[i] == zero:
                    bin_str_list.insert(0, one)
                    bin_str = "".join(bin_str_list)
                else:
                    break

            return bin_convert(non_neg_int - 1, bin_str)


print(bin_convert(8))
