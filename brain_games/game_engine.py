import prompt

from brain_games.cli import welcome_user


def launch_game(rules, game):
    ROUNDS = 3
    name = welcome_user()
    print(rules)

    for _ in range(ROUNDS):
        game_data = game()
        question = game_data.get("question")
        answer = game_data.get("answer")

        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if (user_answer != answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")

    print(f"Congratulations, {name}!")      
        
