# Caluclate cost from a cart given in dictionary format
# Declare the dictionary
cart =[{'name':'Apple','Price':0.5,'quantity':4},
       {'name': 'Grapes','Price':0.3,'quantity':6},
       {'name': 'Oranges','Price':0.4,'quantity':5}
]

def calculate_total_cost(cart):
  total_cost=0
  for item in cart:
    total_cost += item['Price']*item['quantity']
  return total_cost

total_cost = calculate_total_cost(cart)
print(total_cost)