from brain_games.game_engine import launch_game
from brain_games.games.calc_game import game


def main():
    RULES = "What is the result of the expression?"
    launch_game(RULES, game)


if __name__ == "__main__":
    main()