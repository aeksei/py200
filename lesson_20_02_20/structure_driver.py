# Шаблон проектирования "Стратегия"

import json
import pickle
from abc import abstractmethod


class IStructureDriver:
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, d):
        pass


class JSONFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, encoding='UTF-8') as f:
            return json.load(f)

    def write(self, d):
        with open(self.__filename, 'w', encoding='UTF-8') as f:
            json.dump(d, f, ensure_ascii=False)


class JSONStringDriver(IStructureDriver):
    def __init__(self, s='{}'):
        self.__s = s

    def get_string(self):
        return self.__s

    def read(self):
        return json.loads(self.__s)

    def write(self, d):
        self.__s = json.dumps(d, ensure_ascii=False)


class PickleDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'rb') as f:
            return pickle.load(f)

    def write(self, d):
        with open(self.__filename, 'wb') as f:
            pickle.dump(d, f)


if __name__ == "__main__":
    class SDWorker:
        def __init__(self, structure_driver=None):
            self.__structure_driver = structure_driver
            self.__d = {}

        def set_structure_driver(self, structure_driver):
            self.__structure_driver = structure_driver

        def save(self):
            self.__structure_driver.write(self.__d)

        def load(self):
            self.__d = self.__structure_driver.read()



