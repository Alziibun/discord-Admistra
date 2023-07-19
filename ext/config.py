import os
import json


class Configuration:
    def __init__(self, guild_id):
        self.guild_id = int(guild_id)
        if not os.listdir('.'):
            os.mkdir('config')

    @staticmethod
    def load_json (*args):
        with open(f'{args[0].guild_id}.json', 'r') as file:
            data = json.load(file.read())
            return args[-1](data)

    @staticmethod
    def setting(file, name):
        while (line := file.readline()) != "":



    @read
    def load_setting(self, content, setting_name):


