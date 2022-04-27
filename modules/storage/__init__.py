import json

from constants import KVS_FILE_NAME, KVS_FILE_PATH


class __KeyValueStorage:
    _instance = None

    def __init__(self):
        self.store = {}
        self.__target_file = f'{KVS_FILE_PATH}{KVS_FILE_NAME}'

        try:
            with open(self.__target_file) as file_content:
                content = file_content.read()
                self.store = json.loads(content)

        except OSError:
            with open(self.__target_file, 'w+') as file_content:
                json.dump({}, file_content)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get(self, key):
        # print(f'Getting "{key}" from KVS')

        if key not in self.store:
            return False

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


def get_kvs():
    return __KeyValueStorage.instance()
