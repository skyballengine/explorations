def reverse_string(str):
    if len(str) == 0:
        return ""
    else:
        return reverse_string(str[1:]) + str[0]


print(reverse_string("whateveryoudomyfriend"))
