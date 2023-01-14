# raise NameError
import math


class ImaginaryNumberException(Exception):
    # print("Number less than 0")
    pass


# def main():
num = int(input("Enter a number:"))
# if num >= 0:
#     result = math.sqrt(num)
# else:
#     raise ImaginaryNumberException

try:
    result = 10/num
    print(result)
except ImaginaryNumberException:
    print("No good")
except ZeroDivisionError:
    print("You entered 0")
finally:
    print("We're done here")



#if __name__ == "__main__":
#    main()
