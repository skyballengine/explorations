def insertion_desc(a_list):
    """
  Sorts a_list in ascending order
  """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] < value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value
    print(a_list)


insertion_desc(list(range(1, 10)))
