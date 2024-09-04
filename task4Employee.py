class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Job Title: {self.job}, Salary: ${self.salary:,.2f}"

class Manager(Employee):
    def __init__(self, name, job, salary, number_managed):
        super().__init__(name, job, salary)
        self.number_managed = number_managed

    def __str__(self):
        return f"Name: {self.name}, Job Title: {self.job}, Employees Managed: {self.number_managed}"


employee = Employee("suhaib", "Software Engineer", 75000)
print(employee) 

manager = Manager("Ali", "Project Manager", 95000, 10)
print(manager) 
