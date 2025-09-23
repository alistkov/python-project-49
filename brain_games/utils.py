import math
from random import randint


def is_even(number):
    return number % 2 == 0


def get_greatest_common_divisor(firstNumber, secondNumber):
    if (secondNumber == 0):
        return firstNumber
    return get_greatest_common_divisor(secondNumber, firstNumber % secondNumber)


def generate_progression(start, step, progression_length):
    progression = []

    for index in range(progression_length):
        currentElement = start + index * step
        progression.append(currentElement)

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
