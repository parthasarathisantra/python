n = int(input("Enter no of rows: "))

for i in range(0,n):
    for k in range(n-i-1):
        print("  ", end="")
    for j in range(2*i+1):
        print("* ",end = "")
    print("\n")