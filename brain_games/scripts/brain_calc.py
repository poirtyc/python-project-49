#!/usr/bin/env python3
from brain_games.engine import general_logic
from brain_games.games import calc


def main():
    general_logic(calc.RULES, calc.generate_round)


if __name__ == '__main__':
    main()
