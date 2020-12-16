class Human:
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    def full_name(self):
        return " ".join([self._first_name, self._last_name]).title()


class Employee(Human):
    def __init__(self, first_name: str, last_name: str, salary: int):
        super().__init__(first_name, last_name)
        self.__salary = salary

    @property
    def first_name(self):
        return self._first_name.capitalize()

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name.capitalize()

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @classmethod
    def from_string(cls, employee_str: str):
        parameters = employee_str.split('-')
        if len(parameters) != 3:
            print("Salary is invalid")
            return None

        try:
            salary_value = int(parameters[2])
        except ValueError:
            print("Salary is invalid")
            return None

        return cls(parameters[0], parameters[1], salary_value)


emp1 = Employee('JOAN', 'Smith', 85000)
emp2 = Employee.from_string('John-doe-73000')
print(emp1.first_name)  # ➞ 'Joan'
print(emp1.full_name())  # ➞ 'Joan Smith'
print(emp1.salary)  # ➞ 85000
print(emp2.first_name)  # ➞ 'John'
print(emp2.full_name())  # ➞ 'John Doe'
print(emp2.salary)  # ➞ 73000
