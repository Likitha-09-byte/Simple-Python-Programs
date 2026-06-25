#Calculate the total cost of items in a shopping cart
numberof_items = int(input("Enter the number of items iun cart: "))
def total_cost_items(numberof_items):
  total_cost = 0
  for i in range( numberof_items):
    total_cost = total_cost * 10 
  return total_cost

print(f" The total cost of all items in the cart: ${total_cost_items(numberof_items)}")
        
  