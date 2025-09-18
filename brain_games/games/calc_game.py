from random import choice, randint

OPERATIONS = ["+", "-", "*"]


def game():
    first = randint(1, 25)
    second = randint(1, 25)
    operation = choice(OPERATIONS)

    question = f"{first} {operation} {second}"

    correct_answer = 0

    match operation:
        case "+":
            correct_answer = first + second
        case "-":
            correct_answer = first - second
        case "*":
            correct_answer = first * second
        
    return {
        "question": question,
        "answer": f"{correct_answer}"
    }
