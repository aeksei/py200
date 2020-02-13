class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, *args):
        if len(args) == 3:
            print(args)
            self.__year = args[0]
            self.__month = args[1]
            self.__day = [2]
        else:
            print(args)

    def __str__(self):
        return f"{self.__year}-{self.__month}-{self.__day}"

    def __repr__(self):
        return f"Date({self.year}...)"

    @staticmethod
    def is_leap_year(year):
        return False  #

    @classmethod
    def get_max_day(cls, year, month):
        pass

    @property
    def date(self):
        return self.__str__

    @classmethod
    def __is_valid_date(cls, *args):
        pass

    @date.setter
    def date(self, value):
        pass

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def add_day(self, day):
        pass

    def add_month(self, month):
        pass

    def add_year(self, year):
        pass

    @staticmethod
    def date2_date1(date2, date1):
        pass

    def date_to_days(self):
        return self.__year * 365 + self.__month * 30 + self.__day

    def __eq__(self, other):
        # self == other
        if (self.day == other.day) and \
            (self.month == other.month) and \
            (self.year == other.year):
            return True
        else:
            return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                elif self.day >= other.day:
                    return False

    # def __add__(self, other):
    #     if not isinstance(other, int):
    #         raise ValueError
    #     else:
    #         self.__day += other

    def __radd__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            self.__day += other

d1 =   Date(2020, 2, 7)
d1_1 = Date("2020-2-7")
d2 = Date(2020, 2, 6)

# print(d1.date_to_days() - d2.date_to_days())