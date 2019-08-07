from Drafts.Hw_11.person1 import Person
import csv


class Patient(Person):
    _instances = []
    file = 'Patients.csv'
    columns = ['full_name', 'birth_date', 'sex', 'height', 'weight', 'diagnosis', 'date_format']

    def __init__(self, full_name, birth_date, sex, height, weight, diagnosis, date_format='%d-%m-%Y'):
        super(Patient, self).__init__(full_name, birth_date, date_format)
        self.sex = sex
        self.height = height
        self.weight = weight
        self.diagnosis = diagnosis
        self._instances.append(self)

    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'sex': self.sex,
            'height': self.height,
            'weight': self.weight,
            'diagnosis': self.diagnosis,
            'date_format': self.date_format,

        }

    @classmethod
    def save_all(cls):
        with open(cls.file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cls.columns)
            writer.writeheader()
            writer.writerows(cls._get_dicted_patients())

    @classmethod
    def set_patients_from_csv(cls):
        with open(cls.file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            cls._instances = [Patient(**row) for row in reader]

    @classmethod
    def show_patients(cls):
        with open(cls.file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)

    def add_patient(self):
        with open(self.file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.columns)
            writer.writerow(self.dict)

    @classmethod
    def get_patients(cls):
        return cls._instances

    @classmethod
    def get_males(cls):
        return filter(lambda x: x.sex == 'male', cls._instances)

    @classmethod
    def avg_height_male(cls):
        total_height = 0
        counter = 0
        for dude in cls.get_males():
            total_height += dude.height
            counter += 1
        return total_height / counter

    @classmethod
    def lowest_weight_patient(cls):
        lowest_weight = None
        lowest_weight_patient = None
        for patient in cls._instances:
            if lowest_weight is None or patient.height < lowest_weight:
                lowest_weight = patient.height
                lowest_weight_patient = patient
        return lowest_weight_patient

    @classmethod
    def _get_dicted_patients(cls):
        return map(lambda x: x.dict, cls._instances)

    @classmethod
    def get_dicted_patients(cls):
        return list(cls._get_dicted_patients())


if __name__ == '__main__':
    p1 = Patient('some some some', '29-09-1984', 'male', 1.78, 78, 'vse ploho')
    p2 = Patient('some1 some1 some1', '23-03-1984', 'female', 1.67, 55, 'vse horosho')
    p3 = Patient('some2 some2 some2', '14-09-1984', 'male', 1.75, 88, 'vse norm')
    Patient.save_all()

    # print(Patient.get_dicted_patients())
    # print(Patient._get_dicted_patients())

    print(Patient.lowest_weight_patient())
    print(Patient.avg_height_male())
