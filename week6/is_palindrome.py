def is_palindrome(word):
    if word == "":
        return True

    else:
        first_and_last = word[0] == word[-1]
        return is_palindrome(word[1:-1]) and first_and_last


print(is_palindrome("tornado"))
print(is_palindrome("tuopmmpout"))
