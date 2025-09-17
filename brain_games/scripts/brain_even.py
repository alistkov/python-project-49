import prompt
from random import randint
from brain_games.utils import is_even


def main():
    steps = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while steps > 0:
        number = randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        correct_answer = "yes" if is_even(number) else "no"

        if (user_answer.lower() != correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
        steps -= 1

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()