import prompt
from brain_games.cli import welcome_user


def general_logic(RULES, generate_round):

    player_name = welcome_user()
    print(RULES)

    diversity_rounds = 4
    
    for _ in range(diversity_rounds):
        question, answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != answer:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {answer}.")
            print(f"Let's try again, {player_name}!")
            return
        print("Correct!")

    print(f'Congratulations, {player_name}!')
