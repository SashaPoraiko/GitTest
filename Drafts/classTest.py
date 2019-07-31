from datetime import datetime
import file_modules


class FootballClub:
    file_name = 'Footb.txt'

    def __init__(self, name, country, year, president, budget=0, trophy_count=0):
        self.name = name
        self.country = country
        self.year = year
        self.president = president
        self.budget = budget
        self.trophy_count = trophy_count

    def __repr__(self):
        return 'T: {}, {}, built in: {}\n\tOwner is: {}, with  : {},and won: {} trophies'.format(
            self.name, self.country, self.year, self.president, self.budget,
            self.trophy_count)

    def __str__(self):
        return 'The club name is: {}, {}, built in: {}\n\tOwner is: {}, with total budget: {},and won: {} trophies'.format(
            self.name, self.country, self.year, self.president, self.budget,
            self.trophy_count)

    def __add__(self, other):
        new_club = FootballClub(self.name + ' ' + other.name, self.country, datetime.now().year, self.president,
                                self.budget + other.budget, self.trophy_count + other.trophy_count)
        self.deleted = True
        other.deleted = True
        return new_club

    def __eq__(self, other):
        for att in self.__dict__:
            if getattr(self, att) != getattr(other, att, None):
                return False
        return True

    def save(self):
        file_modules.write(self.file_name, self)


madrid = FootballClub('Madrid', 'Spain', 2888, 'Peres', trophy_count=102)
chelsea = FootballClub('Chelsea', 'Italy', 1980, 'Abramovich', 12385222222, 32)
n_madrid = FootballClub('Madrid', 'Spain', 2888, 'Peres', trophy_count=102)

# print(chelsea)
# print(madrid)

chelsea.save()

