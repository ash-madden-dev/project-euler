# Project Euler problem 2
def even_fibonacci_numbers(number_1: int, number_2: int, current_sum: int) -> int:
    current_term = number_1 + number_2
    current_term_is_even_number = current_term % 2 == 0

    if current_term < 4_000_000 and current_term_is_even_number:
        new_sum = current_sum + current_term
        return even_fibonacci_numbers(number_2, current_term, new_sum)
    elif current_term < 4_000_000 and current_term_is_even_number is not True:
        return even_fibonacci_numbers(number_2, current_term, current_sum)
    else:
        return current_sum


print(even_fibonacci_numbers(1, 2, 2))
