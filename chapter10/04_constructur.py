class Employee:
    language = "Python"  # this is a class attribute
    salary = 1200000


    def __init__(self, name, salary, language):     #_ex_ is called dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating a object")

    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
   
    @staticmethod    #  when there is no use to object then it is better to mark this as a static method
    def greet():
        print("Good Morning")

harry = Employee("Harry", 1300000, "javascript")

# harry.name= "Harry"   # this is a instance attribute

print(harry.name, harry.salary, harry.language)

# rohan = Employee()
