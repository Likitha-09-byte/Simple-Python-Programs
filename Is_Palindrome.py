#Check whether the given string is palindrome or not .
targetword = input("Enter the word: ")
def is_palindrome(targetword):
  targetword=targetword.lower().replace(" "," ")
  temp =""
  for i in targetword:
    temp = i+temp
  if temp == targetword:
    return "Palindrome"
  else:
    return "Not a Palindrome"
  
result =is_palindrome(targetword)
print(result)