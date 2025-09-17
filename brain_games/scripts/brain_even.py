from brain_games.game_engine import launch_game
from brain_games.games.even_game import game


def main():
    RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
    launch_game(RULES, game)


if __name__ == "__main__":
    main()