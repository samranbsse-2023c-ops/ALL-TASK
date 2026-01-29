# =========================================
# Tuple, Set, and Dictionary Lab Tasks
# =========================================

# 1. Create a tuple with 10 elements (int, float, string)
print("1. Tuple with 10 elements")
my_tuple = (1, 2, 3.5, 4.7, "A", "B", "Python", 10, 2, 3.5)
print(my_tuple)
print("-" * 40)

# 2. Count a specific element in tuple
print("2. Count specific element in tuple")
element = 2
count = my_tuple.count(element)
print(f"Element {element} appears {count} times")
print("-" * 40)

# 3. Convert tuple to list, modify, and convert back to tuple
print("3. Tuple → List → Modify → Tuple")
temp_list = list(my_tuple)
temp_list.append("NewItem")
my_tuple = tuple(temp_list)
print(my_tuple)
print("-" * 40)

# 4. Nested tuple and access inner elements
print("4. Nested Tuple")
nested_tuple = (1, 2, (10, 20, 30), 4)
print("Inner tuple element:", nested_tuple[2][1])
print("-" * 40)

# 5. Define a set of 7 elements
print("5. Set with int, float, string")
my_set = {1, 2, 3.5, "A", "B", 7, 9.8}
print(my_set)
print("-" * 40)

# 6. Add element using add() and update()
print("6. Add elements to set")
my_set.add(100)
my_set.update([200, "Python", 5.5])
print(my_set)
print("-" * 40)

# 7. Remove element using remove() and discard()
print("7. Remove elements from set")
my_set.remove(1)
my_set.discard("B")
print(my_set)
print("-" * 40)

# 8. Union of two sets
print("8. Union of sets")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))
print("-" * 40)

# 9. Intersection of two sets
print("9. Intersection of sets")
print("Intersection:", set1.intersection(set2))
print("-" * 40)

# 10. Dictionary of 3 students with marks
print("10. Dictionary of students")
students = {
    "Ali": 85,
    "Sara": 90,
    "Ahmed": 78
}
for key, value in students.items():
    print(key, ":", value)
print("-" * 40)

# 11. Add new key-value pair to dictionary
print("11. Add new key-value pair")
students["Usman"] = 88
print(students)
print("-" * 40)

# 12. Access value using key
print("12. Access value using key")
print("Marks of Sara:", students["Sara"])
print("-" * 40)

# 13. Add new key-value pair using assignment
print("13. Add using assignment")
students["Ayesha"] = 92
print(students)
print("-" * 40)

# 14. Update an existing value
print("14. Update existing value")
students["Ali"] = 95
print(students)
print("-" * 40)

# 15. Remove key-value pair using pop() and del
print("15. Remove using pop() and del")
students.pop("Ahmed")
del students["Usman"]
print(students)
print("-" * 40)

# 16. Use items() to print keys and values
print("16. Print keys and values using items()")
for key, value in students.items():
    print(key, value)
print("-" * 40)

# 17. Find number of items using len()
print("17. Number of items in dictionary")
print("Total items:", len(students))
print("-" * 40)

# 18. Merge two dictionaries using update()
print("18. Merge dictionaries using update()")
extra_students = {
    "Bilal": 80,
    "Hina": 87
}
students.update(extra_students)
print(students)
print("-" * 40)
