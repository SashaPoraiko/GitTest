import sqlite3
import datetime
from Drafts.Hw_11.person1 import Person

if __name__ == '__main__':
    con = sqlite3.connect('dbSqlTest.sqlite')
    cur = con.cursor()
    query_create_person = """
    create table `person`(
    `id` integer primary key autoincrement not null,
    `full_name` varchar(256) not null,
    `birth_date` datetime not null
    );
    """
    human_str = 'Poraiko Oleksandr Viorelovuch, 28-06-1993'
    human_str_2 = 'Poroshenko Petro Batkovuch, 13-02-1775'
    human_str_3 = 'Ivanova Dasha Ivanovna, 20-02-1992'

    lst = []

    lst.append(human_str.split(', '))
    lst.append(human_str_2.split(', '))
    lst.append(human_str_3.split(', '))
    sql_insert = "insert into person (full_name, birth_date) " \
                 "values ('{full_name}', '{birth_date}')"
    for item in lst:
        full_name = item[0]
        birth_date = datetime.datetime.strptime(item[1], '%d-%m-%Y').strftime('%Y-%m-%d %H:%M:%S')
        print(sql_insert.format(full_name=full_name, birth_date=birth_date))
        cur.execute(sql_insert.format(full_name=full_name, birth_date=birth_date))

    con.commit()

    con.close()
