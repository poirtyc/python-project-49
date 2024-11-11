#!/usr/bin/env python3
from brain_games.engine import general_logic
from brain_games.games import culc


def main():
    general_logic(culc.rules, culc.generate_round)


if __name__ == '__main__':
    main()
