from os.path import exists
import json


class Profile:
    def __init__(self, name, username, total_games):
        self.name = name
        self.username = username
        self.total_games = total_games


class Repository:
    def save_profile_data(self, profile_data):
        user = {'name': profile_data.name, 'username': profile_data.username, 'total_games': profile_data.total_games}
        json_object = json.dumps(user, indent=4)
        with open("profile.json", "w") as outfile:
            outfile.write(json_object)

    def load_profile_data(self):
        file = open('profile.json')
        data = json.load(file)
        profile = Profile(data['name'], data['username'], data['total_games'])
        return profile

    def is_profile_exist(self):
        file_exists = exists('profile.json')
        return file_exists
