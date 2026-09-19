import math


def is_prime(a: int) -> bool:
    if a <= 0:
        return False
    elif a == 1:
        return False
    elif a == 2:
        return True
    elif a % 2 == 0:
        return False
    else:
        root = int(math.sqrt(a))
        for i in range(3, root + 1, 2):
            if a % i == 0:
                return False
        return True


def smallest_multiple(a: int, b: int) -> int:
    prime_numbers_up_to_b: list[int] = []
    least_common_multiple = 1
    for i in range(a, b):
        if is_prime(i):
            prime_numbers_up_to_b.append(i)
    for prime_number in prime_numbers_up_to_b:
        exponent = 1
        while prime_number**exponent <= b:
            exponent += 1
        least_common_multiple *= prime_number ** (exponent - 1)
    return least_common_multiple


print(smallest_multiple(1, 20))
