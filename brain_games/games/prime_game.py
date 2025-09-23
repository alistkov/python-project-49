from brain_games.utils import generate_random, is_prime_number


def game():
    question = generate_random(3, 100)
    correct_answer = "yes" if is_prime_number(question) else "no"

    return {
        "question": question,
        "answer": correct_answer
    }