# =========================================
# Advanced OOP Lab Tasks
# =========================================

# 1. Bank Account with private balance
print("1. Bank Account Class (Encapsulation)")
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.__balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("-" * 40)

# 2. Student class with private attributes
print("2. Student Class (Encapsulation)")
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print(f"Student Name: {self.__name}")
        print(f"Marks: {self.__marks}")

s = Student("Ali", [80, 90, 75])
s.display()
print("-" * 40)

# 3. Employee class with private salary
print("3. Employee Salary (Encapsulation)")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def update_salary(self, new_salary):
        self.__salary = new_salary

    def display_salary(self):
        print(f"{self.name}'s Salary: {self.__salary}")

e = Employee("Sara", 50000)
e.display_salary()
e.update_salary(60000)
e.display_salary()
print("-" * 40)

# 4. Vehicle and Car inheritance
print("4. Vehicle and Car Classes (Inheritance)")
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.display()
print("-" * 40)

# 5. Person and Student inheritance
print("5. Person and Student Classes (Inheritance)")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

student = Student("Usman", 20)
student.display()
print("-" * 40)

# 6. Family hierarchy: Grandparent → Parent → Child
print("6. Family Hierarchy")
class Grandparent:
    def __init__(self, gp_name):
        self.gp_name = gp_name

class Parent(Grandparent):
    def __init__(self, gp_name, p_name):
        super().__init__(gp_name)
        self.p_name = p_name

class Child(Parent):
    def __init__(self, gp_name, p_name, c_name):
        super().__init__(gp_name, p_name)
        self.c_name = c_name

    def display(self):
        print(f"Grandparent: {self.gp_name}, Parent: {self.p_name}, Child: {self.c_name}")

child = Child("Ahmed", "Bilal", "Sara")
child.display()
print("-" * 40)

# 7. Device → Computer → Laptop
print("7. Device Hierarchy")
class Device:
    def __init__(self, brand):
        self.brand = brand

class Computer(Device):
    pass

class Laptop(Computer):
    def display(self):
        print(f"Laptop Brand: {self.brand}")

laptop = Laptop("Dell")
laptop.display()
print("-" * 40)

# 8. Person → Employee → Manager
print("8. Company Structure")
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    pass

class Manager(Employee):
    def display(self):
        print(f"Manager Name: {self.name}")

mgr = Manager("Hina")
mgr.display()
print("-" * 40)

# 9. Multiple inheritance: Academics + Sports
print("9. Student with Academics and Sports")
class Academics:
    def __init__(self, subject):
        self.subject = subject

class Sports:
    def __init__(self, sport):
        self.sport = sport

class Student(Academics, Sports):
    def __init__(self, subject, sport):
        Academics.__init__(self, subject)
        Sports.__init__(self, sport)

    def display(self):
        print(f"Subject: {self.subject}, Sport: {self.sport}")

stu = Student("Math", "Cricket")
stu.display()
print("-" * 40)

# 10. Multiple inheritance: Camera + Music Player → Smartphone
print("10. Smartphone Features")
class Camera:
    def __init__(self, camera_feature):
        self.camera_feature = camera_feature

class MusicPlayer:
    def __init__(self, music_feature):
        self.music_feature = music_feature

class Smartphone(Camera, MusicPlayer):
    def __init__(self, camera_feature, music_feature):
        Camera.__init__(self, camera_feature)
        MusicPlayer.__init__(self, music_feature)

    def display(self):
        print(f"Camera Feature: {self.camera_feature}, Music Feature: {self.music_feature}")

phone = Smartphone("108MP Camera", "High-Quality Audio")
phone.display()
print("-" * 40)
