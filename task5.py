# =========================================
# OOP Lab Tasks (Classes and Objects)
# =========================================

# 1. Car class
print("1. Car Class")
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

my_car = Car("Toyota Corolla", "Red")
print("Car Model:", my_car.model)
print("Car Color:", my_car.color)
print("-" * 40)

# 2. Rectangle class (area & perimeter)
print("2. Rectangle Class")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
print("-" * 40)

# 3. Student class with average marks
print("3. Student Average")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # List of 3 marks

    def average(self):
        return sum(self.marks) / len(self.marks)

student1 = Student("Ali", [80, 75, 90])
print(f"{student1.name}'s Average:", student1.average())
print("-" * 40)

# 4. Check pass or fail
print("4. Pass/Fail Check")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def has_passed(self):
        if all(mark >= 40 for mark in self.marks):
            return True
        return False

student2 = Student("Sara", [50, 35, 70])
if student2.has_passed():
    print(f"{student2.name} has Passed")
else:
    print(f"{student2.name} has Failed")
print("-" * 40)

# 5 & 6. Account class with debit, credit, balance
print("5 & 6. Account Class")
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New Balance: {self.balance}")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Debited {amount}. New Balance: {self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: {self.balance}")

acc = Account("ACC123", 1000)
acc.credit(500)
acc.debit(200)
acc.display_balance()
print("-" * 40)

# 7 & 8. Employee class with annual salary
print("7 & 8. Employee Class")
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary  # Monthly salary

    def annual_salary(self):
        return self.salary * 12

emp = Employee(101, "Usman", 50000)
print(f"Employee Name: {emp.name}")
print(f"Monthly Salary: {emp.salary}")
print(f"Annual Salary: {emp.annual_salary()}")
print("-" * 40)
