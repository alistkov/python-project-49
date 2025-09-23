import math


def is_even(number):
    return number % 2 == 0


def getGreatestCommonDivisor(firstNumber, secondNumber):
    if (secondNumber == 0):
        return firstNumber
    return getGreatestCommonDivisor(secondNumber, firstNumber % secondNumber)


def generateProgression(start, step, progression_length):
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
