A - класс
А() - конструктор класса A (__init__)

class A:
	b_class_attr = 1
	def __init__(self):
        self.b_obj_attr = 2
        self.__b = 1
	def b_method(self)

	@property
	def b_property(self):
	    return self.__b

a_obj = A()

A.b_class_attr  # атрибут класса

a_obj.b_obj_attr  # атрибут объекта

a_obj.b_property  # свойство

get_b()

set_b()




clas







