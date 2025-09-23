from brain_games.utils import generate_random, is_even


def game():
    question = generate_random(1, 100)
    correct_answer = "yes" if is_even(question) else "no"
    return {
        "question": question,
        "answer": correct_answer
    }
