from os.path import exists
import json


class Profile:
    def __init__(self, name, username, total_games):
        self.name = name
        self.username = username
        self.total_games = total_games


class Repository:

    def load_profiles(self):
        if not exists('profiles.json'):
            return []
        file = open('profiles.json')
        data = json.load(file)
        profiles = []
        for profile_data in data:
            profile = Profile(profile_data['name'], profile_data['username'], profile_data['total_games'])
            profiles.append(profile)
        return profiles

    def save_profiles(self, profiles):
        profiles_data = []
        for profile in profiles:
            profile_data = {'name': profile.name, 'username': profile.username, 'total_games': profile.total_games}
            profiles_data.append(profile_data)
        json_object = json.dumps(profiles_data, indent=4)
        with open("profiles.json", "w") as outfile:
            outfile.write(json_object)

