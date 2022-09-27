class Employee: 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def summary(self):
        first = self.first
        last = self.last
        pay = self.pay
        email = self.email
        string = 'first name is: {}\nlast name is: {}\nemail is: {}\npay is: {}\n'.format(first, last, email, pay)
        return string

emp_1 = Employee('mason', 'wong', 50000)
emp_2 = Employee('test', 'user', 60000)


# The following two are the same
print(emp_1.summary()) # this is what we usually see
print(Employee.summary(emp_1)) # this is what is happening in the background. 
