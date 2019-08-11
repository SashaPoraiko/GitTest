from Drafts.Hw_11.person1 import Person


class Tourist(Person):
    _instances = []
    file = 'tourists.csv'
    columns = ['full_name', 'birth_date', 'travel_country', 'travel_days_count', 'travel_worth', 'items_count',
               'baggage_weight' 'date_format']

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

