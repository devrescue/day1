#variables and types
name = "Khaleel"
age = 30
height = 5.9
is_active = True

print(name, age, height, is_active)
print(type(name), type(age), type(height), type(is_active))

#lists and dictionaries
numbers = [1,2,3,4]
numbers.append(5)

user = {
    "id": 1,
    "email": "user@gmail.com",
    "is_admin": False
}

print(numbers)
print(user["email"])

#conditionals
score = 85

if score >= 90:
    result = "excellent"
elif score >= 70:
    result = "pass"
else:
    result = "fail"

print(result)

#loops
for n in numbers:
    print(n * 2)

for key, value in user.items():
    print(key, value)

total = 0
for n in numbers:
    total += n

#total
print(total)