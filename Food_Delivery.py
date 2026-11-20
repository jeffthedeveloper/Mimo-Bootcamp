italian_food = [
  "Pasta Bolognese",
  "Pepperoni pizza",
  "Margherita pizza",
  "Lasagna"
]
indian_food = ["Curry","Chutney","Samosa","Naan"]
def find_meal(name, menu):
  return name if name in menu else None

def select_meal(name,food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else:
    return None

def display_available_meals(food_type):
  print(f"Available {food_type} Meals:")
  if food_type == "Italian":
    for meal in italian_food:
      print(meal)
  elif food_type == "Indian":
    for meal in indian_food:
      print(meal)
  else:
      print("Menu não existente!")

def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
type_input = input("Escolha o tipo de comida que você deseja comer: ")
display_available_meals(type_input)
name_input = input("Enter the name of the meal you want to order: ")
amount_input = int(input("Enter the quantity you want to order: "))

result = create_summary(name_input, amount_input, type_input)
print(result)
