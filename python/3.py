def largest_prime_factor(n: int) -> int:
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 1
    return n


print(largest_prime_factor(600851475143))
