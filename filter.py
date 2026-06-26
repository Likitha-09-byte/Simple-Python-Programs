#Filter function - filter out items in lits based on condition. Help for data cleaning 
#Removing unwanter elements from lists. We can write consice and efficent code for processing and manipulating collections.
def even(n):
  if n%2 ==0:
    return True
  
l =[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even,l)))

#Filter and Lambda
number =[1,2,3,4,5,6,7,8,9,10,11,12]
greater_than_five=list(filter(lambda x:x>5,number))
print(greater_than_five)

#Filter on multiple conditions
even_and_greater_than_five = list(filter(lambda x:x>5 and x%2==0,number))
print(even_and_greater_than_five)

#Filter on dictionaries - to check age is greater than 25

people=[
    {'name':'Likitha','age':28},
    {'name' :'Kanchana','age':52},
    {'name':'jack','age':43}]

def age_greater_than_25(person):
  return person['age']>40

print(list(filter(age_greater_than_25,people)))