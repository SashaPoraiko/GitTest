from datetime import datetime
import file_modules


class Person:
    file = 'Humans.txt'

    def __init__(self, full_name, birth_date, date_format='%d-%m-%Y'):
        self.full_name = full_name
        self.birth_date = birth_date
        self.date_format = date_format

    def __repr__(self):
        return 'Full name of person is: {}, and the birth date is: {}'.format(self.full_name, self.birth_date)

    def __str__(self):
        return 'Full name of person is: {}\n\t the birth date is: {}\n'.format(self.full_name, self.birth_date)

    def save_human(self):
        file_modules.write(self.file, self)

    def get_humans(self):
        return file_modules.read(self.file)

    def calculate_years(self):
        return datetime.now().year - datetime.strptime(self.birth_date, self.date_format).year


saha = Person('Poraiko Oleksandr Viorelovuch', '28-06-1993')
saha.save_human()
petka = Person('Poroshenko Petro Batkovuch', '13-02-1775')
petka.save_human()
dashka = Person('Ivanova Dasha Ivanovna', '20.02.1992', '%d.%m.%Y')
dashka.save_human()
dashka.calculate_years()
print(petka.get_humans())
print(saha.calculate_years())
print(petka.calculate_years())
print(dashka.calculate_years())