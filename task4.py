# =========================================
# Loops Lab Tasks (for & while)
# =========================================

# 1. Print squares of numbers from 1 to 10
print("1. Squares from 1 to 10")
for i in range(1, 11):
    print(i, "square =", i * i)
print("-" * 40)

# 2. Count vowels in a string
print("2. Count vowels in a string")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
print("-" * 40)

# 3. Print marks greater than 50
print("3. Marks greater than 50")
marks = [45, 67, 89, 34, 55, 72]
for m in marks:
    if m > 50:
        print(m)
print("-" * 40)

# 4. Print odd numbers between 1 and 20 using while loop
print("4. Odd numbers from 1 to 20")
num = 1
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1
print("-" * 40)

# 5. Ask for password until correct
print("5. Password Checker")
correct_password = "python123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access Granted")
        break
    else:
        print("Wrong password, try again")
print("-" * 40)

# 6. Take input until user types 'stop'
print("6. Type 'stop' to end")
while True:
    user_input = input("Enter something: ")
    if user_input.lower() == "stop":
        print("Program stopped")
        break
print("-" * 40)

# 7. Sum of numbers from 1 to n
print("7. Sum from 1 to n")
n = int(input("Enter value of n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)
print("-" * 40)
