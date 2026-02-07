class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return float(self.base_salary)


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary + self.base_salary * self.bonus_percent / 100


class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500
class Intern(Employee):
    pass
data = input().split()
role, name, base_salary = data[0], data[1], int(data[2])
if role == "Manager":
    emp = Manager(name, base_salary, int(data[3]))
elif role == "Developer":
    emp = Developer(name, base_salary, int(data[3]))
else: 
    emp = Intern(name, base_salary)
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")