#!/usr/bin/env python3
from brain_games.engine import general_logic
from brain_games.games import even


def main():
    general_logic(even.RULES, even.generate_round)


if __name__ == '__main__':
    main()
