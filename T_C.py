#Convert Celsius to Fahrenheit and vice versa:

temp =float(input("Enter the current temperature: "))
unit = input("Enter the unit of the temperature: ")
def f_to_c(temp,unit):
  if unit =='f':
    return(temp -32)*5/9
  elif unit =='c':
    return (temp*9/5) +32
print(f"The coverted temp from :  {f_to_c(temp,unit)}")
