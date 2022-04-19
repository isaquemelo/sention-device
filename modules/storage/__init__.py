import json

from constants import KVS_FILE_NAME, KVS_FILE_PATH


class KeyValueStorage:
    def __init__(self):
        self.store = {}
        self.__target_file = f'{KVS_FILE_PATH}{KVS_FILE_NAME}'

        with open(self.__target_file) as file_content:
            self.store = json.load(file_content)

    def get(self, key):
        print(f'Getting "{key}" from KVS')
        return self.store[key]

    def set(self, key, value):
        print(f'Setting "{key} = {value}" from KVS')

        self.store[key] = value

        with open(self.__target_file, 'w') as jsonfile:
            json.dump(self.store, jsonfile)

        return value

    def wipe(self):
        with open(self.__target_file, 'w') as jsonfile:
            json.dump({}, jsonfile)
            self.store = {}

    def get_store(self):
        return self.store
