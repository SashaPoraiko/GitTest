from functools import reduce

from Hw_11.person1 import Person


class Teacher(Person):
    _instances = []

    def __init__(self, full_name, birth_date, faculty, posada, rank, payments, courses_count, date_format='%d-%m-%Y'):
        super(Teacher, self).__init__(full_name, birth_date, date_format)
        self.faculty = faculty
        self.rank = rank
        self.posada = posada
        self.courses_count = courses_count
        self.payments = payments
        self._instances.append(self)

    @classmethod
    def get_teachers_by_faculty(cls, faculty):
        return filter(lambda x: x.faculty == faculty, cls._instances)

    @classmethod
    def listed_teachers(cls, faculty):
        return list(cls.get_teachers_by_faculty(faculty))

    @classmethod
    def calculate_courses_count_by_faculty(cls, faculty):
        return reduce(lambda x, item: x + item.courses_count, cls.get_teachers_by_faculty(faculty), 0)

    @classmethod
    def calculate_avg_years(cls, faculty):
        total_years = 0
        count = 0
        for teacher in cls.get_teachers_by_faculty(faculty):
            total_years += teacher.calculate_years()
            count += 1
        return total_years / count


if __name__ == '__main__':
    zhorik = Teacher('Geoginelli George Georovuch', '13.02.1956', 'Economy', 'profesor', 'magistr', 13000, 3,
                     '%d.%m.%Y')
    dodik = Teacher('Geoginelli Dodik Ivanovuch', '13.02.1889', 'Economy', 'profesor', 'magistr', 13000, 3, '%d.%m.%Y')
    afonik = Teacher('Geoginelli Afoniy Petrovuch', '13.02.1760', 'Economy', 'profesor', 'magistr', 13000, 3,
                     '%d.%m.%Y')

    print(Teacher.calculate_avg_years('Economy'))
    print(Teacher.calculate_courses_count_by_faculty('Economy'))
