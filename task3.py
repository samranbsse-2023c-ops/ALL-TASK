# =========================================
# Conditions and Functions Lab Tasks
# =========================================

# 1. Input three numbers and print the largest
print("1. Largest of Three Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest number:", max(a, b, c))
print("-" * 40)

# 2. Discount calculation
print("2. Discount Calculation")
total = float(input("Enter total amount: "))
if total >= 500:
    discount = total * 0.20
elif total >= 200:
    discount = total * 0.10
else:
    discount = 0
print("Discount:", discount)
print("Final Amount:", total - discount)
print("-" * 40)

# 3. Username and Password Check
print("3. Login System")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")
print("-" * 40)

# 4. Password Strength Checker
print("4. Password Strength")
pwd = input("Enter password: ")
if len(pwd) < 6:
    print("Weak")
elif len(pwd) < 10:
    print("Medium")
else:
    print("Strong")
print("-" * 40)

# 5. Speed Fine Checker
print("5. Speed Fine Checker")
speed = int(input("Enter speed: "))
if speed <= 60:
    print("No Fine")
elif speed <= 80:
    print("Small Fine")
else:
    print("Heavy Fine")
print("-" * 40)

# 6. Shop Discount Final Price
print("6. Shop Discount")
price = float(input("Enter total price: "))
if price >= 1000:
    discount = price * 0.20
elif price >= 500:
    discount = price * 0.10
else:
    discount = 0
print("Final Price:", price - discount)
print("-" * 40)

# 7. Weather Classification
print("7. Weather Classification")
temp = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
wind = float(input("Enter wind speed: "))

if temp < 25 and humidity < 60 and wind < 20:
    print("Pleasant Weather")
elif temp < 35:
    print("Normal Weather")
else:
    print("Harsh Weather")
print("-" * 40)

# 8. Function: Price after Tax
print("8. Price After Tax Function")
def final_price(price, tax):
    return price + (price * tax / 100)

print("Final Price:", final_price(1000, 15))
print("-" * 40)

# 9. Function: Factorial
print("9. Factorial Function")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))
print("-" * 40)

# 10. Function: Average of List
print("10. Average of Numbers")
def average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average([10, 20, 30, 40, 50]))
print("-" * 40)

# 11. Function: Temperature Category
print("11. Temperature Category")
def temp_status(temp):
    if temp < 10:
        return "Cold"
    elif temp <= 25:
        return "Warm"
    else:
        return "Hot"

print("Temperature Status:", temp_status(18))
print("-" * 40)

# 12. Function: Sum, Difference, Product
print("12. Sum, Difference, Product")
def calculations(x, y):
    return x + y, x - y, x * y

s, d, p = calculations(10, 5)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)
print("-" * 40)
