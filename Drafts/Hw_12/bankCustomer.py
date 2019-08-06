from functools import reduce

from Drafts.Hw_11.person1 import Person


class BankCustomer(Person):
    _instances = []

    def __init__(self, full_name, birth_date, passport_id, sex, credit_sum, phone_number, date_format='%d-%m-%Y'):
        super(BankCustomer, self).__init__(full_name, birth_date, date_format)
        self.passport_id = passport_id
        self.sex = sex
        self.credit_sum = credit_sum
        self.phone_number = phone_number
        self._instances.append(self)

    @classmethod
    def total_credit_sum(cls):
        return reduce(lambda x, item: x + item.credit_sum, cls._instances, 0)

    @classmethod
    def avg_male_clients_age(cls):
        total_age = 0
        count = 0
        for customer in filter(lambda x: x.sex == 'male', cls._instances):
            total_age += customer.calculate_years()
            count += 1
        return total_age / count


ivan = BankCustomer('Ivanov Ivan Ivanovuch', '20-02-1996', 'ktl123ig', 'male', 23000, '0999876273')
olia = BankCustomer('Ivanova Olia Ivanovna', '20-02-1998', 'qtw123ig', 'female', 13500, '0990887265')
masha = BankCustomer('Petrova Masha Ostapivna', '20-06-1992', 'ktjh73ig', 'female', 43897, '0998753785')
bogdan = BankCustomer('Ivanov Bogdan Bogdanovuch', '13-03-1991', 'kt9uk3ig', 'male', 4289, '0667224564')

print(BankCustomer.avg_male_clients_age())
print(BankCustomer.total_credit_sum())
