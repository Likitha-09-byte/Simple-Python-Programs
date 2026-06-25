#This program is to check whether the password is strong or not.
password = input("Enter the password")
score = 0
def pass_checker(password,score):
  symbols = '@,#,$'
  if len(password) >=8 :
    score+=20
  if  any (char in symbols for char in password):
    score+=40
  if  any(char.isdigit()for char in password):
    score+=40
    
  return score
  

if score <80:
  print(f"your password {pass_checker(password,score)}% only please make is stronger")
else:
  print(f"Your password {pass_checker(password,score)} is stronger!!")
  
  
  