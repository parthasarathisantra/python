class Employee:
    language = "Py"  # this is a class attribute
    salary = 1200000

harry = Employee()
harry.language = "javascript"   # this is a instance attribute
print(harry.language, harry.salary)

