n = int(input("Enter a number: "))
if(n<=0):
    print("Please Enter a valid number")
else:
    sum = 0
    while(n>0):
         sum += n
         n -= 1
    print("sum of n natural number is",sum)



