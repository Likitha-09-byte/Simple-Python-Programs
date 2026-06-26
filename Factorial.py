#Check the factorial of a number using recursion:
n = int(input("enter the number : "))
def factorial(n):
  if n ==1 or n==0:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(n))