print("Welcome to pizza factory")
size = input("what size of pizza do you want?S,M or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese?Y or N")

pepperoni_for_small_pizza = 2
pepperoni_for_any_other = 3
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_size= 25
extra_cheese_price = 1
total_price = 0

if size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    total_price = total_price + small_pizza_price + extra_cheese_price + pepperoni_for_small_pizza
elif size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    total_price = total_price + medium_pizza_price + pepperoni_for_any_other + extra_cheese_price
else:
    total_price = total_price + large_pizza_size + extra_cheese_price + pepperoni_for_any_other

print(f"your total bill is {total_price}")

