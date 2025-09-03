while True:
 menu ={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
 }

 print("Welcome to Python restaurant menu!")
 print("Pizza: RS40\nPasta: RS50\nBurger: RS60\nSalad: RS70\nCoffee: RS80")

 order_total = 0

 item_1 = input("Enter the name of item you want to orde = ")
 if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

 else:
    print(f"Sorry, {item_1} isn't available")
 another_order = input("Do you want to order another item? (y/n): ")
 another_order = another_order.lower()
 if another_order == "y":
    item_2 = input("Enter the second item= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Sorry, {item_2} isn't available")


 print(f"Your total bill amount is {order_total}")