from profile import Profile


class Game:

    def __init__(self, repo, **kwargs):
        self.__random_number_start = kwargs["random_number_start"]
        self.__random_number_end = kwargs["random_number_end"]
        if self.__random_number_end <= self.__random_number_start:
            raise 'Wrong random numbers range'
        self.__current_games_count = 0
        self.__current_profile = None
        self.repository = repo
        self.profiles = self.repository.load_profiles()

    def ask_variant(self, text, true_answer, false_answer):
        print(f'{text} {true_answer}/{false_answer}')
        user_answer = input().lower()
        if user_answer == true_answer:
            return True
        elif user_answer == false_answer:
            return False
        else:
            return self.ask_variant(text, true_answer, false_answer)

    def guess(self, text, true_answer):
        print(text)
        user_answer = input()
        if user_answer == true_answer:
            return True
        else:
            return False

    def login(self):
        print(f'Введите ваш юзернейм:')
        username = input()
        if len(self.profiles) == 0:
            self.signup(username)
            print(f'Привет, {self.__current_profile.name}')
            return
        for profile in self.profiles:
            if profile.username == username:
                self.__current_profile = profile
                print(f'Привет, {self.__current_profile.name}')
                break
            else:
                self.signup(username)
                print(f'Привет, {self.__current_profile.name}')
                break

    def signup(self, username):
        print(f'Введите ваше имя:')
        name = input()
        self.__current_profile = Profile(name, username, 0)
        self.profiles.append(self.__current_profile)
        self.repository.save_profiles(self.profiles)

    def start(self):
        self.login()

        while True:
            guess_number = 1  # random.randint(random_number_start, random_number_end)
            if self.guess(f'Угадайте число от {self.__random_number_start} до {self.__random_number_end}',
                          str(guess_number)):
                print('Вы угадали число: ' + str(guess_number))
                self.__current_games_count += 1
                self.__current_profile.total_games += 1
                print(f'Игр сыграно в этой сессии: {self.__current_games_count}')
                print(f'Всего игр сыграно: {self.__current_profile.total_games}')
                if not self.ask_variant('Хотите сыграть еще раз?', 'да', 'нет'):
                    break
            else:
                print('Вы не угадали число. Попробуйте еще раз')
        self.repository.save_profiles(self.profiles)
