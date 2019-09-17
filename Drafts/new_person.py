from datetime import datetime
import file_modules
import sqlite3

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
con = sqlite3.connect('sqlDb_1.sqlite')
cur = con.cursor()


class Person:

    def __init__(self, full_name, birth_date):
        self.full_name = full_name
        self.birth_date = datetime.strptime(birth_date, DATE_FORMAT)
        self.id = None

    def __repr__(self):
        return 'Full name of person is: {}, and the birth date is: {}'.format(
            self.full_name,
            datetime.strftime(self.birth_date, DATE_FORMAT)
        )

    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'id': self.id
        }

    def __str__(self):
        return 'Full name of person is: {}\n\t the birth date is: {}'.format(
            self.full_name,
            datetime.strftime(self.birth_date, DATE_FORMAT)
        )

    def insert(self):
        sql_insert = "insert into `person` (full_name, birth_date) " \
                     "values ('{full_name}', '{birth_date}')"
        cur.execute(sql_insert.format(**self.dict))
        pk = cur.lastrowid
        self.id = pk
        return pk

    def update(self):
        sql_update = '''
                     update `person`
                     set full_name='{full_name}', birth_date='{birth_date}'
                     where id = '{id}'
                     '''
        cur.execute(sql_update.format(**self.dict))
        return con.commit()

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


class Programmer(Person):

    def __init__(self, full_name, birth_date, firm_name, spec, post, salary, current_project, id=None, person_id=None):
        super(Programmer, self).__init__(full_name, birth_date)
        self.firm_name = firm_name
        self.spec = spec
        self.post = post
        self.salary = salary
        self.current_project = current_project
        self.id = id
        self.person_id = person_id

    def __str__(self):
        person = super(Programmer, self).__str__()
        return 'Person: {person}\nSalary: {salary}'.format(
            person=person,
            **self.dict
        )

    def update(self):
        sql_person_update = '''
                     update `person`
                     set full_name='{full_name}', birth_date='{birth_date}'
                     where id = '{person_id}'
                     '''
        cur.execute(sql_person_update)
        sql_programmer_update = '''
                     update `programmer`
                     set firm_name='{firm_name}', spec='{spec}', post='{post}','salary'='{salary}',
                     'current_project'='{current_project}'
                     where id = '{id}'
                     '''
        cur.execute(sql_programmer_update)

    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'id': self.id,
            'person_id': self.person_id,
            'firm_name': self.firm_name,
            'spec': self.spec,
            'post': self.post,
            'salary': self.salary,
            'current_project': self.current_project
        }

    @classmethod
    def get_programmers_by_spec(cls, spec):
        sql_get_programmers = """
        select firm_name,count(id) from programmer
        where spec='{}'
        GROUP by firm_name
        """.format(spec)
        cur.execute(sql_get_programmers)
        programmers = cur.fetchall()
        return [{'firm': firm, 'count': count} for firm, count in programmers]

    @classmethod
    def get_avg_salary(cls, firm_name):
        sql_avg_salary = """
            select avg(salary) from programmer
            where firm_name="{}"
        """.format(firm_name)
        cur.execute(sql_avg_salary)
        return cur.fetchone()[0]

    @classmethod
    def best_salaries_per_firm(cls):
        sql_best_salaries = """
        select firm_name, max(salary) from programmer group by firm_name
        """
        cur.execute(sql_best_salaries)
        salaries = cur.fetchall()
        return [{'firm': firm, 'salary': salary} for firm, salary in salaries]

    @classmethod
    def worst_project(cls):
        sql_worst_project = """
        select current_project from programmer
         where salary=(select min(salary) from programmer)
        """
        cur.execute(sql_worst_project)
        return cur.fetchall()

    def insert(self):
        sql_person_insert = """
        insert into `person` (full_name, birth_date) 
                     values ('{full_name}', '{birth_date}')
                     """
        cur.execute(sql_person_insert.format(**self.dict))

        self.person_id = cur.lastrowid

        sql_insert = "insert into `programmer` (firm_name,spec,post,salary,current_project,person_id) " \
                     "values ('{firm_name}','{spec}','{post}'," \
                     "'{salary}','{current_project}','{person_id}')"

        cur.execute(sql_insert.format(**self.dict))

        self.id = cur.lastrowid

    def save(self):
        if self.id is None:
            self.insert()
        else:
            self.update()

        con.commit()

    @staticmethod
    def get_by_id(id):

        inc_programmer = '''
            select person.full_name,person.birth_date,
            firm_name,spec,post,salary,current_project,programmer.id,person_id
            from "programmer" 
            join "person" on person.id=programmer.person_id
            where programmer.id=={id}
        '''
        cur.execute(inc_programmer.format(id=id))
        res = cur.fetchone()
        con.commit()
        print(res)

        return Programmer(*res)


if __name__ == '__main__':
    query_create_programmer = """
       create table `programmer`(
       `id` integer primary key autoincrement not null,
       `firm_name` varchar(256) not null,
       `spec` varchar(256) null,
       `post` varchar(256) not null,
       `salary` integer not null,
       `current_project` varchar(256) null,
       'person_id' integer not null
       );
       """
    print(Programmer.get_programmers_by_spec('arrays'))

    # cur.execute(query_create_programmer)
    # con.commit()

    # vadim = Programmer('Korniychuk Vadim Batkovuch', '02-03-1996', 'firma', 'arrays', 'topDev', 32000, 'courses')
    # sasha = Programmer('Poraiko Sasha Batkovuch', '05-11-1993', 'firma', 'arrays', 'topDev', 132000, 'studying')
    # dima = Programmer('SkyGroup Dmutro Batkovuch', '12-03-1989', 'firma', 'arrays', 'topDev', 232000, 'learning')

    # vadim.insert()
    # sasha.insert()
    # dima.insert()
    # con.commit()

    con.close()

    # petka = Person('Poroshenko Petro Batkovuch', '13-02-1775')
    # dashka = Person('Ivanova Dasha Ivanovna', '20-02-1992')
    #
    # query_create_person = """
    #    create table `person`(
    #    `id` integer primary key autoincrement not null,
    #    `full_name` varchar(256) not null,
    #    `birth_date` datetime not null
    #    );
    #    """
    # vadim = Programmer('Korniychuk Vadim Batkovuch', '02-03-1996', 'firma', 'arrays', 'topDev', 32000, 'courses')
    # sasha = Programmer('Poraiko Sasha Batkovuch', '05-11-1993', 'firma', 'arrays', 'topDev', 132000, 'studying')
    # dima = Programmer('SkyGroup Dmutro Batkovuch', '12-03-1989', 'firma', 'arrays', 'topDev', 232000, 'learning')
    #
    # print(Programmer.calculate_firm_avg_salary('firma'))
    # print(Programmer.get_worst_project('firma'))
    #
    # # cur.execute(query_create_person)
    # # con.commit()
    # #
    # petka.insert()
    # dashka.insert()
    # #
    # # con.close()
    # dashka.full_name = 'abrakadabra'
    # dashka.birth_date = '1999-01-01'
    # dashka.update()

    #
    # select * from person
    # where full_name like '%po%'
    # select avg(date('now')-birth_date) from person

    # UPDATE person
    # set birth_date='2000-02-20'
    # where id=2

    # select full_name,birth_date from person
    # where id in (1) or birth_date > '2000-01-01'
    # order by birth_date
