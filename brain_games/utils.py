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
