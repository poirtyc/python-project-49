import prompt
from brain_games.cli import welcome_user


def general_logic(RULES, generate_round):

    player_name = welcome_user()
    print(RULES)

    for _ in range(3):
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

    print(f'Congratulations, {player_name}!')
