# class A:
#     pi = 3.14
#
#     def __init__(self):
#         self.__pi = 3.14
#
#     @property
#     def pi(self):
#         return self.__pi
#
#     @property
#     @staticmethod
#     def get_pi():
#         return 3.14
#
#     @property
#     @classmethod
#     def get_pi(cls):
#         return cls.pi

#

class A:
    class_public_attr_a = "public_attr_a"
    _class_protected_attr_a = "protected_attr_a"
    __class_private_attr_a = "private_attr_a"


if __name__ == "__main__":
    a = A()
    print()

