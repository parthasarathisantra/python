def gratest(a, b, c):
    if(a>b and b>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

d = gratest(a, b, c)
print(f"The gratest value of a,b,c is {d}")