from Drafts.Hw_11.person1 import Person
from Lib import csv_file_module as csv_f, shelve_module as sm


class Applicant(Person):
    _instances = []
    csv_file = 'applicants.csv'
    shelve_file = 'applicants'

    columns = ['full_name', 'birth_date', 'faculty', 'spec', 'avg_mark', 'date_format']

    def __init__(self, full_name, birth_date, faculty, spec, avg_mark,
                 date_format='%d-%m-%Y'):
        super(Applicant, self).__init__(full_name, birth_date, date_format)
        self.faculty = faculty
        self.spec = spec
        self.avg_mark = avg_mark
        self._instances.append(self)

    @property
    def dict(self):
        data = super(Applicant, self).dict
        data.update({
            'faculty': self.faculty,
            'spec': self.spec,
            'avg_mark': self.avg_mark,
        })
        return data

    @classmethod
    def save_into_csv_file(cls):
        csv_f.save_all_into_csv(cls.file, cls.get_dicted_applicants(), cls.columns)

    @classmethod
    def get_dicted_applicants(cls):
        return map(lambda x: x.dict, cls._instances)

    @classmethod
    def save_into_shelve_file(cls):
        sm.save_into_shelve(cls.shelve_file, 'full_name', cls._instances)

    @classmethod
    def get_from_shelve(cls):
        cls._instances = sm.read_from_shelve(cls.shelve_file)

    def add_to_shelve(self):
        sm.add_single(self.shelve_file, 'full_name', self)

    @classmethod
    def find_dude(cls, name):
        sm.find_single(cls.shelve_file, name)


if __name__ == '__main__':
    ap = Applicant('sadk kqwewqu xmvxvxp', '11-01-2000', 'economy', 'economist', 3.23)
    ab = Applicant('zhorik kqwe1231wqu xmvopopxvxp', '11-11-2020', 'economy', 'economist', 3.23)
    az = Applicant('sadk dasvqqqwe htyhyhyh', '11-03-2009', 'economy', 'economist', 3.23)

    Applicant.save_into_shelve_file()

    aa = Applicant('sadk rrr htyhyhyh', '11-03-2009', 'economy', 'economist', 3.23)
    aa.add_to_shelve()

    Applicant.get_from_shelve()
    print(len(Applicant._instances))
    print(Applicant.find_dude('zhorik kqwe1231wqu xmvopopxvxp'))
