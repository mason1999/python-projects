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
    pass

emp_1 = Employee('mason', 'wong', 50000)
emp_2 = Employee('test', 'user', 60000)

# all the raise amounts are gotten from the class variable
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount,'\n')

# print out the namespace. Instances see the raise_amount from the class variable
print(Employee.__dict__,'\n')

# all the instances get their raise_amount changed
Employee.raise_amount = 2
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount,'\n')

# only emp_1's raise_amount was changed. 
emp_1.raise_amount = 1.08
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount,'\n')

# number of num_of_employees
print('number of employees is ', Employee.num_of_employees)
