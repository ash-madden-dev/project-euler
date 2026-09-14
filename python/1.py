# Solution to Problem 1 on Project Euler
def sum_of_multiples(multiple_of: list[int], highest_number: int):
    sum = 0
    for number in range(highest_number):
        for item in multiple_of:
            if number % item == 0:
                sum += number
                break
    return sum


print(sum_of_multiples([3, 5], 1000))
