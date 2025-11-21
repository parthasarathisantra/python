class Employee:
    language = "Python"  # this is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    # def greet(self):
    #     print("Good Morning")
    @staticmethod    #  when there is no use to object then it is better to mark this as a static method
    def greet():
        print("Good Morning")

harry = Employee()
harry.language = "javascript"   # this is a instance attribute

harry.greet()
harry.getInfo()   #employee.getInfo(harry)

