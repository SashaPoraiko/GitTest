# select avg(salary) from programmer
# where firm_name = 'firma'

# select current_project from programmer
# where salary=(select min(salary) from programmer)

# select firm_name, max(salary) from programmer group by firm_name

#
# select firm_name,count(id) from programmer
# where spec='arrays'
# GROUP by firm_name

# FOREIGN key (person_id) REFERENCES person(id)

# insert into programmer(firm_name,spec,post,salary,current_project,person_id)
# select firm_name,spec,post,salary,current_project,person_id from programmer_old