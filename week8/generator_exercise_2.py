# def all_primes():
#     counter = 2
#     divisors = 0
#     while True:
#         counter += 1
#         for num in range(counter - 1, 1, -1):
#             divisors = 0
#             if counter % num == 0:
#                 divisors += 1
#                 continue
#         if divisors == 0:
#             yield counter

# correct method
def all_primes():
    """Generates all prime numbers"""
    num = 2
    while num:
        if is_prime(num):
            yield num
        num += 1

def is_prime(n):
    if n == 2 or n == 3:
        return True

    if not n % 2:
        return False

    for i in range(3, int(n ** .5) + 1, 2):
        if not n % i:
            return False
    return True


primes = all_primes()
prime_list = [next(primes) for i in range(10)]
print(prime_list)
