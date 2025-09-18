def is_even(number):
    return number % 2 == 0


def getGreatestCommonDivisor(firstNumber, secondNumber):
    if (secondNumber == 0):
        return firstNumber
    return getGreatestCommonDivisor(secondNumber, firstNumber % secondNumber)
