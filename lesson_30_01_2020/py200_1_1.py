# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Первушин А.О.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами v и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume  # объем стакана
            else:
                raise ValueError
        else:
            raise TypeError

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume  # заполнненость водой
            else:
                raise ValueError
        else:
            raise TypeError


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

glass1 = Glass(200, 100)
print(glass1.capacity_volume)
print(glass1.occupied_volume)

glass2 = Glass(300, 150)
print(glass2.capacity_volume)
print(glass2.occupied_volume)


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume  # объем стакана
            else:
                raise ValueError
        else:
            raise TypeError

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume  # заполнненость водой
            else:
                raise ValueError
        else:
            raise TypeError


glass_3_1 = GlassDefaultArg(200)
glass_3_2 = GlassDefaultArg(200, 200)


# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?
  
class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)
        print(self.occupied_volume)

print("=========")
glass_4_1 = GlassDefaultListArg(200)
glass_4_2 = GlassDefaultListArg(200)


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume  # объем стакана
            else:
                raise ValueError
        else:
            raise TypeError

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume  # заполнненость водой
            else:
                raise ValueError
        else:
            raise TypeError

    def add_water(self, adding_water):
        space = self.capacity_volume - self.occupied_volume  # объем пустого места в стакане
        if adding_water <= space:
            self.occupied_volume += adding_water
            return self.occupied_volume
        else:
            self.occupied_volume = self.capacity_volume
            return adding_water - space

    def remove_water(self, removing_water):
        pass


glass_5_1 = GlassAddRemove(200, 100)
print(glass_5_1.add_water(50) == 150)

# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

print("======")

glass_6_1 = GlassAddRemove(200)


if isinstance(glass_6_1, GlassAddRemove):
    print(type(int))

GlassAddRemove(200)
# GlassAddRemove.__init__(self, capacity_volume=200, occupied_volume=0)

print(dir(glass_6_1))
print(glass_6_1.__dict__)

print(dir(GlassAddRemove))
print(GlassAddRemove.__dict__)

# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume=0):
        # print()
        self.capacity_volume = capacity_volume  # объем стакана
        # print()
        self.occupied_volume = occupied_volume  # заполнненость водой
        # print()

# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

class GlassId:
    def __init__(self, capacity_volume, occupied_volume=0):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # заполнненость водой
        print(hex(id(self)))  # адрес  в памяти объекта self

glass_8_1 = GlassId(200)
print(hex(id(glass_8_1)))

glass_8_2 = GlassId(200)
print(hex(id(glass_8_2)))

# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
	def __init__(f, a=2):
		f.a = a
		
	def print_me(p):
		print(p.a)
		
d.print_me(d())		

# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:
            return
        self.a = a;

obj_1 = A(25)
print(dir(obj_1))

obj_2 = A(100)
print(dir(obj_2))

# Объясните так реализовывать __init__ нельзя?
		
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# 

class Node:
    def __init__(self, prev=None, next_=None):
        """
        :param prev: Class Node
        :param next_: Class Node
        """
        self.__prev = prev
        self.__next = next_

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev
        
    def __str__(self):
        ...
        
    def __repr__(self):
        ...

class LinkedList:
    def __init_(self, nodes=None):
        if nodes is None:
            self.head = None
            self.tail = None
            self.__len = 0

        elif isinstance(nodes, Node):
            self.head = nodes
            self.tail = nodes
            self.__len = 1
        else:
            self.head = nodes[0]
            self.tail = nodes[-1]
            self.__len = len(nodes)

    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        # TODO index out of range

        if index == 0:
            node.set_prev(None)
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
        elif index == (self.__len - 1):
            node.set_next(None)
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.get_next()
            current_node_next = current_node.get_next()

            current_node.set_next(node)
            node.set_prev(current_node)

            node.set_next(current_node_next)
            current_node_next.set_prev(node)




        # current_node = self.head
        # for i in range(index):
        #     current_node = current_node.get_next()


        current_node.set_prev(node)
        node.set_next(self.head)


       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        pass

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...
























