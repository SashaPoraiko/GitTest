from Drafts.Hw_11.person1 import Person
from Lib import csv_file_module as csv_f


class Footballer(Person):
    _instances = []
    file = 'footballers.csv'
    columns = ['full_name', 'birth_date', 'country', 'club', 'matches_count', 'goals_count',
               'goal_passes', 'date_format']

    def __init__(self, full_name, birth_date, country, club, matches_count, goals_count, goal_passes,
                 date_format='%d-%m-%Y'):
        super(Footballer, self).__init__(full_name, birth_date, date_format)
        self.country = country
        self.club = club
        self.matches_count = matches_count
        self.goals_count = goals_count
        self.goal_passes = goal_passes
        self._instances.append(self)

    @property
    def dict(self):
        data = super(Footballer, self).dict
        data.update({
            'country': self.country,
            'club': self.club,
            'matches_count': self.matches_count,
            'goals_count': self.goals_count,
            'goal_passes': self.goal_passes
        })
        return data

    @classmethod
    def get_dicted_footballers(cls):
        return map(lambda x: x.dict, cls._instances)

    @classmethod
    def country_team(cls, searched_country):
        return list(filter(lambda player: player.country == searched_country, cls._instances))

    @classmethod
    def best_avg_results_player(cls, searched_country):
        best_avg = None
        best_player = ''
        for player in cls.country_team(searched_country):
            if best_avg is None or best_avg < player.matches_count / player.goals_count:
                best_avg = player.matches_count / player.goals_count
                best_player = player
        return best_player

    @classmethod
    def save_footballers(cls):
        csv_f.save_all_into_csv(cls.file, cls.get_dicted_footballers(), cls.columns)

    def __add_single_footballer(self):
        csv_f.add_single(self.file, self.columns, self.dict)

    def add_single_footballer(self):
        self.__add_single_footballer()

    @classmethod
    def get_footballers_form_csv(cls):
        cls._instances = [Footballer(**row) for row in csv_f.read_from_csv(cls.file)]


if __name__ == '__main__':
    p1 = Footballer('abra cadabra cabra', '27-07-1876', 'argentina', 'club1', 193, 26, 13)

    p2 = Footballer('abra asdqqe terte', '27-07-1899', 'argentina', 'club2', 123, 9, 8)

    p3 = Footballer('abra qweqxxx caqweertqbra', '27-07-1876', 'italy', 'club3', 93, 16, 4)

    Footballer.save_footballers()
    Footballer.get_footballers_form_csv()
    print(Footballer._instances)
