from datetime import datetime
import file_modules


class Person:
    file = 'Humans.txt'

    def __init__(self, full_name, birth_date, date_format='%d-%m-%Y'):
        self.full_name = full_name
        self.birth_date = datetime.strptime(birth_date, date_format)
        self.date_format = date_format

    def __repr__(self):
        return 'Full name of person is: {}, and the birth date is: {}'.format(
            self.full_name,
            datetime.strftime(self.birth_date, self.date_format)
        )

    def __str__(self):
        return 'Full name of person is: {}\n\t the birth date is: {}'.format(
            self.full_name,
            datetime.strftime(self.birth_date, self.date_format)
        )

    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': datetime.strftime(self.birth_date, self.date_format),
            'date_format': self.date_format
        }

    def save_human(self):
        file_modules.write(self.file, self)

    @classmethod
    def get_humans(cls):
        return file_modules.read(cls.file)

    def calculate_years(self):
        today = datetime.now()
        try:
            birthday = self.birth_date.replace(year=today.year)
            # raised when birth date is February 29
            # and the current year is not a leap year
        except ValueError:
            birthday = self.birth_date.replace(year=today.year,
                                               month=self.birth_date.month + 1, day=1)
        if birthday > today:
            return today.year - self.birth_date.year - 1
        return today.year - self.birth_date.year


if __name__ == '__main__':
    saha = Person('Poraiko Oleksandr Viorelovuch', '28-06-1993')
    saha.save_human()
    petka = Person('Poroshenko Petro Batkovuch', '13-02-1775')
    petka.save_human()
    dashka = Person('Ivanova Dasha Ivanovna', '20.02.1992', '%d.%m.%Y')
    dashka.save_human()
    print(Person.get_humans())
    print(saha.calculate_years())
    print(petka.calculate_years())
    print(dashka.calculate_years())
