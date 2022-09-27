import datetime as dt

class Employee: 

    raise_amount = 1.04 # a class variable
    num_of_employees = 0 # another class variable will incremement every time we call the init method. We should always access this via the class

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_employees += 1

    def summary(self):
        first = self.first
        last = self.last
        pay = self.pay
        email = self.email
        string = 'first name is: {}\nlast name is: {}\nemail is: {}\npay is: {}\n'.format(first, last, email, pay)
        return string

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # we get different results depending on whether we did self.raise_amount or Employee.raise_amount!

    # we now receive the class as the first argument rather than the instance. We use cls because class is a reserved key word. 
    @classmethod  
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # using a class method as an alternative constructor. suppose we got info in the form of 'first-last-pay'
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods dont include self or cls as their first argument
    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # monday --> 0 ,..., sunday --> 6
            return 'it is not a work day'
        return 'it is a work day'


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
emp_1 = Employee('mason', 'wong', 50000)
emp_2 = Employee('test', 'user', 60000)

# both print out 1.04
print(emp_1.raise_amount)
print(emp_2.raise_amount, '\n')

# change the raise_amount to 1.05
Employee.set_raise_amount(1.05) # same thing as Employee.raise_amount = 1.05. However the former has the advantage of being read only!
print(emp_1.raise_amount)
print(emp_2.raise_amount, '\n')

# we can also run the class method from the instance. There's no difference but it's just less common
emp_1.set_raise_amount(2)
print(emp_1.raise_amount)
print(emp_2.raise_amount, '\n')

# alternative constructor use
emp_3_str = 'john-doe-70000'
emp_3 = Employee.from_string(emp_3_str)
print(emp_3.summary())

# testing our static method
my_date = dt.date(2016, 7, 10)
print(Employee.is_workday(my_date))
