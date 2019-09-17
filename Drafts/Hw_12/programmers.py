from Drafts.Hw_11.person1 import Person


class Programmer(Person):
    _instances = []

    def __init__(self, full_name, birth_date, firm_name, spec, post, salary, current_project, date_format='%d-%m-%Y'):
        super(Programmer, self).__init__(full_name, birth_date, date_format)
        self.firm_name = firm_name
        self.spec = spec
        self.post = post
        self.salary = salary
        self.current_project = current_project
        self._instances.append(self)

    @classmethod
    def get_programmers_by_firm(cls, firm):
        return filter(lambda x: x.firm_name == firm, cls._instances)

    @classmethod
    def calculate_firm_avg_salary(cls, firm):
        total_salary = 0
        counter = 0
        for programmer in cls.get_programmers_by_firm(firm):
            total_salary += programmer.salary
            counter += 1
        return total_salary / counter

    @classmethod
    def get_worst_project(cls, firm):
        lowest_salary = None
        worst_project = None
        for programmer in cls.get_programmers_by_firm(firm):
            if lowest_salary is None or programmer.salary < lowest_salary:
                lowest_salary = programmer.salary
                worst_project = programmer.current_project
        return worst_project, lowest_salary




vadim = Programmer('Korniychuk Vadim Batkovuch', '02-03-1996', 'firma', 'arrays', 'topDev', 32000, 'courses')
sasha = Programmer('Poraiko Sasha Batkovuch', '05-11-1993', 'firma', 'arrays', 'topDev', 132000, 'studying')
dima = Programmer('SkyGroup Dmutro Batkovuch', '12-03-1989', 'firma', 'arrays', 'topDev', 232000, 'learning')

print(Programmer.calculate_firm_avg_salary('firma'))
print(Programmer.get_worst_project('firma'))
