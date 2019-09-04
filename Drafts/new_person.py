from datetime import datetime
import file_modules
import sqlite3

DATE_FORMAT = '%d-%m-%Y'
con = sqlite3.connect('sqlDb_1.sqlite')
cur = con.cursor()


class Person:
    file = 'Humans.txt'

    def __init__(self, full_name, birth_date):
        self.full_name = full_name
        self.birth_date = datetime.strptime(birth_date, DATE_FORMAT)
        self.id = None

    def __repr__(self):
        return 'Full name of person is: {}, and the birth date is: {}'.format(
            self.full_name,
            datetime.strftime(self.birth_date)
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
            datetime.strftime(self.birth_date)
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


if __name__ == '__main__':
    petka = Person('Poroshenko Petro Batkovuch', '13-02-1775')
    dashka = Person('Ivanova Dasha Ivanovna', '20-02-1992')

    query_create_person = """
       create table `person`(
       `id` integer primary key autoincrement not null,
       `full_name` varchar(256) not null,
       `birth_date` datetime not null
       );
       """
    # cur.execute(query_create_person)
    # con.commit()
    #
    petka.insert()
    dashka.insert()
    #
    # con.close()
    dashka.full_name = 'abrakadabra'
    dashka.birth_date = '1999-01-01'
    dashka.update()

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
