from brain_games.engine import general_logic
from brain_games.games import progression


def main():
    general_logic(progression.rules, progression.generate_round)


if __name__ == ('__main__'):
    main()
