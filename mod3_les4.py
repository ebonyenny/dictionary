#create a class employee
from unicodedata import name


class Employee:
    Min_salary =3000

    def __init__(self, name, salary):
        self.name=name
        if salary >=Employee.Min_salary:
            self.salary=salary
        else:
            self.salary = Employee.Min_salary
        # print("Employee name is ", self.name)
        # print("employee salary is", self.salary)


#create an instance of a class
emp_1 = Employee(name="Eniola", salary=10000)

print("Eniola's salary is", emp_1.Min_salary)
