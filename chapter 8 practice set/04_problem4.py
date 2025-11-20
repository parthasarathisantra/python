def sum(n):
  if(n==1):
    return 1
  else:
    return n + sum(n-1)
n = int(input("enter a number: "))
a = sum(n)
print(f"sum of n natural number is {a}")
    
  
