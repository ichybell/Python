class Employee:

    raise_amnt= 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#We can also use Employee.raise_amnt
#This refers to a class variable which is instatiated by class.varibale or self.variable
#No paratheses are used as it is an instance of a variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)

    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amnt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        pay = int(pay)
        return cls(first, last, pay)
# using a static method to determine whether a day is weekday or weekend
# only use static method if cls is not used within the function or if self is not needed either
# i.e. when you don't use either within the function/method

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "It is a weekend"
        return "It is a weekday"

class Developer(Employee):
    raise_amnt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, prog_lang = emp_str.split('-')
        pay = int(pay)
        return cls(first, last, pay, prog_lang)

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

import datetime
my_date = datetime.date(2016, 7, 11)


print(Employee.is_workday(my_date))
emp_1= Employee('Ian', 'Peter', 3000)
emp_2= Employee('Peter', 'Chevy', 2000)

print(f"There are currently {Employee.num_of_emps} employees: \n\t*{emp_1.fullname()}* \n\t*{emp_2.fullname()}*")
print(f"The original pay for {emp_1.fullname()} is ${emp_1.pay}")
print(f"Now we are going to increment the pay by {Employee.raise_amnt}%")
emp_1.apply_raise()
print("The incremented pay for {} is ${}".format(emp_1.fullname(),emp_1.pay))

print(f"The original pay for {emp_2.fullname()} is ${emp_2.pay}")
print(f"Now we are going to increment the pay by {Employee.raise_amnt}%")
emp_2.apply_raise()
print("The incremented pay for {} is ${}".format(emp_2.fullname(),emp_2.pay))

# using a class method
print("Now let's change the raise amount")
print(f"The initial raise amount is {Employee.raise_amnt}%")
Employee.set_raise_amnt(1.05)
print(f"The final raise amount is {Employee.raise_amnt}%")

# the code below showcases inheritance where the created class of Developer has
# inherited all the methods and attributes found in class Employee
#This is showcased by the from_string() function which can be called from the Developer class among other methods
dev_str_1 = 'John-Doe-7000-Python'
dev_1 = Developer.from_string(dev_str_1)

print(f"There are currently {Employee.num_of_emps} employees: \n\t*{emp_1.fullname()}* \n\t*{emp_2.fullname()}* \n\t*{dev_1.fullname()}*")

print(f"The original pay for {dev_1.fullname()} is ${dev_1.pay}")
print(f"Now we are going to increment the pay by {Developer.raise_amnt}%")
dev_1.apply_raise()
print("The incremented pay for {} is ${}".format(dev_1.fullname(),dev_1.pay))

mgr_1 = Manager ('Sue', 'Smith', 90000, [dev_1, emp_1])

print(mgr_1.email)

print(f"The manager: {mgr_1.fullname()} manages:")
mgr_1.print_emps()
print(f"Now let's go ahead and remove {emp_1.fullname()} from {mgr_1.fullname()}'s' list")
mgr_1.remove_emp(emp_1)
print(f"The manager: {mgr_1.fullname()} now manages:")
mgr_1.print_emps()
