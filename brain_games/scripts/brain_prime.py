#!/usr/bin/env python3
from brain_games.engine import general_logic
from brain_games.games import prime


def main():
    general_logic(prime.RULES, prime.generate_round)


if __name__ == ('main'):
    main()
