import json
import os


def read(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def write(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)


def append(content, file_path):
    with open(file_path, 'a') as file:
        file.write(content)


class JSON:
    @staticmethod
    def read(file_path, *data_path):
        data_path = list(data_path)

        if not JSON.exists(file_path):
            JSON.write(file_path, None)

        with open(file_path, 'r') as file:
            data = json.load(file)

        if len(data_path) > 0:
            for i in data_path:
                data = data[i]

        return data

    @staticmethod
    def exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def write(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)
