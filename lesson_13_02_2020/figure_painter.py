import os
#
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\PySide2\\plugins\\platforms'

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint

sys.path.append(os.path.abspath(os.getcwd()))
import figures

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


class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []

    def set_figures(self, figures):
        self.__figures = figures

    def paintEvent(self, event):
        painter = QPainter(self)
        reset_brush = painter.brush()
        for figure in self.__figures:
            if not isinstance(figure, Figure):
                raise TypeError

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x, figure.y,
                                 figure.width, figure.height)
                continue

			# if isinstance(figure, Ellipse):
			# 	painter.setBrush(QBrush(Qt.green))
			# 	painter.drawEllipse(figure.x(), figure.y(), figure.width(), figure.height())
			# 	continue
			#
			# if isinstance(figure, CloseFigure):
			# 	painter.setBrush(QBrush(Qt.blue))
			#
			# 	points = []
			# 	for point in figure:
			# 		points.append(QPoint(point['x'], point['y']))
			# 	painter.drawPolygon(points)
			# 	continue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # Создайте список фигур
    figures = [Rectangle(0, 0, 100, 100)]

    figure_widget.set_figures(figures)

    figure_widget.show()
    sys.exit(app.exec_())
