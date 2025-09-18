from brain_games.game_engine import launch_game
from brain_games.games.gcd_game import game


def main():
    RULES = "Find the greatest common divisor of given numbers."
    launch_game(RULES, game)
    


if __name__ == "__main__":
    main()