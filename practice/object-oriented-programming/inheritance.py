class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)

# inheriting from the emplyee class
class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang = 'None'):
        # passes first, last and pay to our parent class and let that class handle the first three parameters
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) <-- alternative but not recommended
        self.prog_lang = prog_lang
    def __str__(self):
        first = self.first
        last = self.last
        pay = str(self.pay)
        lang = self.prog_lang
        my_str = 'first name is: ' + first + '\n' + 'last name is: ' + last + '\n' + 'pay is: ' + pay + '\n' + 'programming language is: ' + lang + '\n'
        return my_str

dev_3 = Developer('mason', 'wong', 67000)
dev_4 = Developer('jason', 'jong', 89000, 'Java')
print(dev_3)
print(dev_4)

# print(help(Developer))
# print(dev_1.raise_amt)
# dev_1.apply_raise()
# print(dev_1.raise_amt)
