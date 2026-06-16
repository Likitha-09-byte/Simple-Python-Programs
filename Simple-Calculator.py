#Concepts: Variables, Data Types, Basic Operators , Functions, I/O.
#define functions for all operations
def add(x,y):
  return x+y
  
def sub(x,y):
  return x-y

def mul(x,y):
  return x*y

def div(x,y):
  return x/y

#User input 
selection = input("Please enter the operation you want to perform: ").lower().strip()
print(selection)
try:
  x= float(input("Enter the value for x: "))
  y= float(input("Enter the value for y: "))


  #Implement the logic 
  if selection == 'add':
    print("The sum of given numbers are: ",add(x,y))
  elif selection == "sub" :
    print("The Difference of given numbers are: ", sub(x,y))
  elif selection == "mul":
    print("The product of given numbers are: ",mul(x,y))
  elif selection =="div":
    #Logic for the divide by 0 issue.
    if y!=0 :
      print("The division of given numbers are: ",div(x,y))
    else:
      print("Division by 0 is invalid ")
  else:
    print("Provide proper selection")
    
except ValueError:
  print("Provide proper input:  you must enter numbers for x and y ")