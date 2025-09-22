from brain_games.game_engine import launch_game
from brain_games.games.progression_game import game


def main():
    RULES = "What number is missing in the progression?"
    launch_game(RULES, game)
    

if __name__ == "__main__":
    main()