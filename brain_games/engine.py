import prompt
from brain_games.cli import welcome_user


def general_logic(rules, generate_round):

    player_name = welcome_user()
    print(rules)
    rounds_count = 3

    while rounds_count > 0:
        question, answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {answer}.")
            print(f"Let's try again, {player_name}!")
            return
        rounds_count -= 1
    print(f'Congratulations, {player_name}!')
