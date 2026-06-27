year = int(input('Enter the year'))

if year >0:
  if year %4==0 and year%100==0 and year%400 ==0:
    print(year," is a Leap")
  else:
    print(year,"is not a Leap year")
else:
  print("Enter a valid year")