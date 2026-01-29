# ================================
# Python Lab Tasks (All in One File)
# ================================

# 1. Area of a Circle
print("1. Area of a Circle")
radius = float(input("Enter radius: "))
area = 3.14159 * radius * radius
print("Area of the circle:", area)
print("-" * 30)

# 2. Swap Two Numbers
print("2. Swap Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
print("-" * 30)

# 3. Celsius to Fahrenheit
print("3. Celsius to Fahrenheit")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
print("-" * 30)

# 4. Total Marks and Percentage
print("4. Total Marks and Percentage (5 Subjects)")
marks = []
for i in range(5):
    m = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("-" * 30)

# 5. Integer to Float and Float to Integer
print("5. Integer to Float and Float to Integer")
num1 = int(input("Enter an integer: "))
num2 = float(input("Enter a float number: "))
print("Integer to Float:", float(num1))
print("Float to Integer:", int(num2))
print("-" * 30)

# 6. List of Five Numbers (Sum, Max, Min)
print("6. List Operations (Sum, Max, Min)")
numbers = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

print("List:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("-" * 30)

# 7. Take 5 Names and Store in a List
print("7. Store 5 Names in a List")
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
print("Names List:", names)
print("-" * 30)

# 8. Add an Element Using append()
print("8. Add Element Using append()")
my_list = [1, 2, 3]
my_list.append(4)
print("List after append:", my_list)
print("-" * 30)

# 9. Insert an Element at a Specific Index
print("9. Insert Element Using insert()")
my_list = [1, 2, 4]
my_list.insert(2, 3)
print("List after insert:", my_list)
print("-" * 30)

# 10. Remove an Element Using remove() and pop()
print("10. Remove Element Using remove() and pop()")
my_list = [10, 20, 30, 40]
my_list.remove(20)
print("After remove():", my_list)
my_list.pop()
print("After pop():", my_list)
print("-" * 30)
