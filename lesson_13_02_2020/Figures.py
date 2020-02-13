from abc import abstractmethod


class Figure:
    def __init__(self, x=0, y=0):
        self._x = x  # start_x
        self._y = y  # start_y

    @abstractmethod
    def perimeter(self):
        """
        Abstract method
        :return:
        """

    @abstractmethod
    def square(self):
        """
        Abstract method
        :return:
        """

    @abstractmethod
    def width(self):
        """
        Abstract method
        :return:
        """

    @abstractmethod
    def height(self):
        """
        Abstract method
        :return:
        """


class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x, y)
        # self.__x = x
        # self.__y = y
        self.w = w
        self.h = h

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError
        self._y = y

    @property
    def perimeter(self):
        return 2*(self.w+self.h)

    @property
    def square(self):
        return self.w*self.h

    @property
    def width(self):
        return self.w

    @property
    def height(self):
        return self.h


if __name__ == "__main__":
    rect = Rectangle(0, 0, 5, 10)