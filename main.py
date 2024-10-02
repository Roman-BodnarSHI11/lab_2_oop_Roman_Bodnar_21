class Payroll:
    def __init__(self, name, age, salary, is_happy):
        self.name = name
        self.age = age
        self.salary = salary
        self.is_happy = is_happy

    def calculate_net_salary(self):
        salary_after_tax = self.salary - self.calculate_tax()
        salary_after_bonus = salary_after_tax + self.calculate_bonus()
        return salary_after_bonus * 12

    def calculate_tax(self):
        income_tax = self.salary * 0.18
        military_tax = self.salary * 0.015
        return income_tax + military_tax

    def calculate_bonus(self):
        return self.salary * 0.1

    def get_data(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Salary: {self.salary}, Is Happy: {self.is_happy}")

    @classmethod
    def get_employees(cls):
        return


class JobDetails:
    def __init__(self, position, company):
        self.position = position
        self.company = company

    def get_job_details(self):
        return f"Position: {self.position}, Company: {self.company}"


class Developer(Payroll, JobDetails):
    def __init__(self, name, age, salary, is_happy, language, position, company):
        Payroll.__init__(self, name, age, salary, is_happy)
        JobDetails.__init__(self, position, company)
        self.language = language

    def get_data(self):
        return (f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, "
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
        return (f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, "
                f"Mood: {self.is_happy}, Department: {self.department}, "
                f"Position: {self.position}, Company: {self.company}")

    @classmethod
    def get_employees(cls):
        return


if __name__ == '__main__':
    employees = {'developer': 'John Smith', 'manager': 'Jane Doe'}

    for employee, name in employees.items():
        if employee == 'developer':
            developer = Developer(name, 30, 21000, True, 'Python', 'Software Engineer', 'ABC')
            print(developer.get_data())
            print(f"Net annual salary (after tax and bonus): {developer.calculate_net_salary()}")

        elif employee == 'manager':
            manager = Manager(name, 40, 14000, True, 'Finance', 'Sales Manager', 'XYZ')
            print(manager.get_data())
            print(f"Net annual salary (after tax and bonus): {manager.calculate_net_salary()}")