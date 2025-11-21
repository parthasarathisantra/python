class Demo:
    a = 4
o = Demo()
print(o.a) # prints the class attribute because instance attribute is not preseent
o.a = 0    # Instance is set

print(o.a)   # prints the instance attribute because instance attribure is present
print(Demo.a)