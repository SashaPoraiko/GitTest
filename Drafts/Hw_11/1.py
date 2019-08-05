from datetime import datetime
import file_modules


class Person:
    file = 'Humans.txt'

    def __init__(self, full_name, birth_date):
        self.full_name = full_name
        self.birth_date = birth_date

    def __repr__(self):
        return 'Full name of person is: {}, and the birth date is: {}'.format(self.full_name, self.birth_date)

    def __str__(self):
        return 'Full name of person is: {}\n\t the birth date is: {}\n'.format(self.full_name, self.birth_date)

    def save_human(self):
        file_modules.write(self.file, self)

    def get_humans(self):
        file_modules.read(self.file)

    def calculate_years(self):
        return datetime.now().year - datetime.strptime(self.birth_date, '%d-%m-%Y').year


saha = Person('Poraiko Oleksandr Viorelovuch', '28-06-1993')

petka = Person('Poroshenko Petro Batkovuch', '13-02-1775')
