from constants import INCOME_TAX_RATE, MILITARY_TAX_RATE, BONUS_RATE, MONTHS_IN_YEAR
from job_details import JobDetails
import datetime

class Payroll:
    def __init__(self, name, age, salary, is_happy):
        self.name = name
        self.age = age
        self.salary = salary
        self.is_happy = is_happy

    @property
    def net_salary(self):
        salary_after_tax = self.salary - self._calculate_tax()
        salary_after_bonus = salary_after_tax + self._calculate_bonus()
        return salary_after_bonus * MONTHS_IN_YEAR

    def _calculate_tax(self):
        income_tax = self.salary * INCOME_TAX_RATE
        military_tax = self.salary * MILITARY_TAX_RATE
        return income_tax + military_tax

    def _calculate_bonus(self):
        return self.salary * BONUS_RATE

    @property
    def data(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Salary: {self.salary}, Is Happy: {self.is_happy}")

    def salary_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def is_eligible_for_bonus(self):
        return self.is_happy

    @classmethod
    def get_employees(cls):
        return []

    @property
    def birth_year(self):
        return datetime.datetime.now().year - self.age

    def display_summary(self):
        print(f"Employee: {self.name}, Age: {self.age}, Salary: {self.salary}")
        print(f"Net Annual Salary: {self.net_salary}")
        print(f"Is Happy: {'Yes' if self.is_happy else 'No'}")

class Developer(Payroll, JobDetails):
    def __init__(self, name, age, salary, is_happy, language, position, company):
        Payroll.__init__(self, name, age, salary, is_happy)
        JobDetails.__init__(self, position, company)
        self.language = language

    def get_data(self):
        return (f"Name: {self.name}, Year of Birth: {self.birth_year}, Age: {self.age}, Salary: {self.salary}, "
                f"Mood: {self.is_happy}, Language: {self.language}, "
                f"Position: {self.position}, Company: {self.company}")

    @classmethod
    def get_employees(cls):
        return


class Manager(Payroll, JobDetails):
    def __init__(self, name, age, salary, is_happy, department, position, company):
        Payroll.__init__(self, name, age, salary, is_happy)
        JobDetails.__init__(self, position, company)
        self.department = department

    def get_data(self):
        return (f"Name: {self.name}, Year of Birth: {self.birth_year},Age: {self.age}, Salary: {self.salary}, "
                f"Mood: {self.is_happy}, Department: {self.department}, "
                f"Position: {self.position}, Company: {self.company}")

    @classmethod
    def get_employees(cls):
        return
