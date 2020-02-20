# Наблюдатель
class Observer:
    def update(self):
        pass


class Subject:
    def __init__(self):
        self.__o = set()

    def add_observer(self, o: Observer):
        self.__o.add(o)

    def remove_observer(self, o: Observer):
        self.__o.remove(o)

    def notify(self):
        for o in self.__o:
            o.update()


class Data(Subject):
    def __init__(self, data):
        super().__init__()  # нужно ли вызывать super?
        self._data = data  # подумать как сделать так, чтобы при первой записи тоже уведомлялся observer

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if self._data != data:
            self._data = data
            self.notify()
