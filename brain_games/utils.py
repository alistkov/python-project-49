import math
from random import randint


def is_even(number):
    return number % 2 == 0


def get_greatest_common_divisor(first_number, second_number):
    if (first_number == 0):
        return second_number
    return get_greatest_common_divisor(
        first_number,
        second_number % first_number
    )


def generate_progression(start, step, progression_length):
    progression = []

    for index in range(progression_length):
        current_element = start + index * step
        progression.append(current_element)

    return progression


def is_prime_number(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_random(start, end):
    return randint(start, end)
