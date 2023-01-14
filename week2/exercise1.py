class OutOfRangeError(Exception):
    pass


def name_the_number():
    num = int(input("Please enter a number: "))
    if num == 1:
        print(1)
    elif num == 2:
        print(2)
    elif num == 3:
        print(3)
    else:
        raise OutOfRangeError

def main():
    try:
        name_the_number()
    except OutOfRangeError:
        print("That's not one of the allowed values!")


if __name__ == "__main__":
    main()
