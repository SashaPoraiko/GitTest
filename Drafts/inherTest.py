from Hw_11.person1 import Person


class Student(Person):
    _instances = []

    def __init__(self, full_name, birth_date, faculty, group, payments, avg_mark, date_format='%d-%m-%Y'):
        super(Student, self).__init__(full_name, birth_date, date_format)
        self.faculty = faculty
        self.group = group
        self.avg_mark = avg_mark
        self.payments = payments
        self._instances.append(self)

    @classmethod
    def calculate_payments_size(cls, group):
        total_sum = 0
        for student in cls._students_by_group(group):
            total_sum += student.payments
        return total_sum

    @classmethod
    def calculate_avg_age(cls, group):
        total_age = 0
        counter = 0
        for student in cls._students_by_group(group):
            total_age += student.calculate_years()
            counter += 1
        return total_age / counter

    @classmethod
    def _students_by_group(cls, group):
        return filter(lambda x: x.group == group, cls._instances)

    @classmethod
    def students_by_group(cls, group):
        return list(cls._students_by_group(group))


if __name__ == '__main__':
    masha = Student('Kostunyk Masha Victorivna', '28-04-1995', 'Economic', 372, 117.8, 13.3, '%d-%m-%Y')
    grisha = Student('Kostunyk grisha Victorovuch', '28-04-1995', 'Economic', 372, 117.8, 13.3, '%d-%m-%Y')
    yasha = Student('Kostunyk Yasha Georgovuch', '28-04-1995', 'Economic', 372, 117.8, 13.3, '%d-%m-%Y')
    print(Student.calculate_payments_size(372))
    print(Student.calculate_avg_age(372))
