import random
from profile import *

random_number_start = 0
random_number_end = 5
games_count = 0


def ask_variant(text, true_answer, false_answer):
    print(f'{text} {true_answer}/{false_answer}')
    user_answer = input().lower()
    if user_answer == true_answer:
        return True
    elif user_answer == false_answer:
        return False
    else:
        return ask_variant(text, true_answer, false_answer)


def guess(text, true_answer):
    print(text)
    user_answer = input()
    if user_answer == true_answer:
        return True
    else:
        return False


current_user = None
repository = Repository()

if repository.is_profile_exist():
    current_user = repository.load_profile_data()
    print(f'Привет, {current_user.name}')
    print(f'Всего игр сыграно: {current_user.total_games}')
else:
    print(f'Введите ваше имя:')
    name = input()
    print(f'Введите ваш никнейм:')
    username = input()
    current_user = Profile(name, username, 0)
    repository.save_profile_data(current_user)

while True:
    guess_number = 1  # random.randint(random_number_start, random_number_end)
    if guess(f'Угадайте число от {random_number_start} до {random_number_end}', str(guess_number)):
        print('Вы угадали число: ' + str(guess_number))
        games_count += 1
        current_user.total_games += 1
        print(f'Игр сыграно в этой сессии: {games_count}')
        print(f'Всего игр сыграно: {current_user.total_games}')
        if not ask_variant('Хотите сыграть еще раз?', 'да', 'нет'):
            break
    else:
        print('Вы не угадали число. Попробуйте еще раз')
repository.save_profile_data(current_user)
