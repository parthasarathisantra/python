n = int(input("Enter a number: "))

if(n<0):
    print("Enter a valid number")
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("The factorial of the number is",fact)
   