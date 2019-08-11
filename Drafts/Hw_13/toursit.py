from Drafts.Hw_11.person1 import Person
from Lib.csv_file_module import *


class Tourist(Person):
    _instances = []
    file = 'tourists.csv'
    columns = ['full_name', 'birth_date', 'travel_country', 'travel_days_count', 'travel_worth', 'items_count',
               'baggage_weight', 'date_format']

    def __init__(self, full_name, birth_date, travel_country, travel_days_count, travel_worth, items_count,
                 baggage_weight,
                 date_format='%d-%m-%Y'):
        super(Tourist, self).__init__(full_name, birth_date, date_format)
        self.travel_country = travel_country
        self.travel_days_count = travel_days_count
        self.travel_worth = travel_worth
        self.items_count = items_count
        self.baggage_weight = baggage_weight
        self._instances.append(self)

    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'travel_country': self.travel_country,
            'travel_days_count': self.travel_days_count,
            'travel_worth': self.travel_worth,
            'items_count': self.items_count,
            'baggage_weight': self.baggage_weight,
            'date_format': self.date_format,
        }

    @classmethod
    def __country_tourists(cls, searched_country):
        return filter(lambda x: x.travel_country == searched_country, cls._instances)

    @classmethod
    def country_tourists_count(cls, searched_country):
        return len(list(cls.__country_tourists(searched_country)))

    @classmethod
    def avg_baggage_weight(cls, searched_country):
        total_weight = 0
        for tourist in cls.__country_tourists(searched_country):
            total_weight += tourist.baggage_weight
        return total_weight / cls.country_tourists_count(searched_country)

    @classmethod
    def get_dicted_tourists(cls):
        return map(lambda x: x.dict, cls._instances)

    @classmethod
    def save_toursits(cls):
        save_all_into_csv(cls.file, cls.get_dicted_tourists(), cls.columns)

    def __add_single_tourist(self):
        add_single(self.file, self.columns, self.dict)

    def add_single_tourist(self):
        self.__add_single_tourist()

    @classmethod
    def get_tourists_form_csv(cls):
        return read_from_csv(cls.file)


if __name__ == '__main__':
    p1 = Tourist('petrov petr petrovich', '11-02-1979', 'irak', 13, 32000, 7, 12)
    p2 = Tourist('petrov fedir petrovich', '11-02-1889', 'irak', 13, 32000, 7, 32)
    p3 = Tourist('petrov ivan petrovich', '11-02-1999', 'iran', 13, 32000, 7, 12)
    Tourist.save_toursits()

    print(Tourist.country_tourists_count('iran'))
    print(Tourist.avg_baggage_weight('irak'))
    print(Tourist.get_tourists_form_csv())
