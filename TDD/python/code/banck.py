from datetime import date

class Funcionario:
    def __init__(self, name, birth_date, wage):
        self._name = name
        self._birth_date = birth_date
        self._wage = wage

    @property
    def name(self):
        return self._name

    @property
    def wage(self):
        return self._wage

    def ages(self):
        birth_date = self._birth_date.split('/')
        year_birth = birth_date[-1]
        current_year = date.today().year
        return current_year - int(year_birth)

    def last_name(self):
        full_name = self.name.strip()
        name_broken = full_name.split(' ')
        return name_broken[-1]


    def _is_partner(self):
        surname = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._wage >= 100000) and (self.surname() in surnames)


    def decrease_wage(self):
        if self._is_partner():
            decrease = self._wage * 0.1
            self._wage = self._wage - decrease


    def calculate_bonus(self):
        value = self._wage * 0.1
        if value > 1000:
            raise Exception('Salary is too high to receive a bonus')
        return value

    def __str__(self):
        return f'Funcionario({self._name}, {self._birth_date}, {self._wage})'