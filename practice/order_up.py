# WM 2nd Order up
#Make 3 different dictionaries to store mains, sides, and drinks
main_picked = False
side1_picked = False
side2_picked = False
drink_picked = False
mains = {
 'Burger': 5.99,
 'Steak': 7.99,
 'Sandwich': 6.99,
 'Grilled Cheese': 4.99,
}
sides = {
    'Steak fries': 1.99,
    'Curly fries': 1.99,
    'Sweet potato fries': 1.99,
    'Tater Tots': 1.99
}
drinks = {
    'Water': 1.99,
    'Sprite': 1.99,
    'Pepsi': 1.49,
    'Cream soda': 1.49
}
def order(choice, dict, picked, price):
    while True:
        choice = input("What would you like for your main?" )
        choice = choice.capitalize()
        for key in dict.keys():
            if key == choice:
                picked = True
        if picked == True:
            price = mains[main_choice]
            break
#Print the menu and prices
print("Mains")
for key in mains.keys():
    print(f"{key} : {mains[key]}")
print("Sides")
for key in sides.keys():
    print(f"{key} : {sides[key]}")
print("Drinks")
for key in drinks.keys():
    print(f"{key} : {drinks[key]}")
#Have 3 while loops that runs while variables for main the 2 sides and drink are false, and have them be made true when they choose a valid item.
while True:
    #Have a variable that stores their choice and have a for loop check if its vaild, if it is, save its price, and break out of the loop.
    main_choice = input("What would you like for your main?" )
    main_choice = main_choice.capitalize()
    for key in mains.keys():
        if key == main_choice:
            main_picked = True
    if main_picked == True:
        main_price = mains[main_choice]
        break
    else:
        print("Invalid choice")
while True:
    #Repeat previous step
    side1_choice = input("What would you like for your first side?" )
    side1_choice = side1_choice.capitalize()
    for key in sides.keys():
        if key == side1_choice:
            side1_picked = True
    if side1_picked == True:
        side1_price = sides[side1_choice]
        break
    else:
        print("Invalid choice")
while True:
    #Repeat previous step
    side2_choice = input("What would you like for your second side?" )
    side2_choice = side2_choice.capitalize()
    for key in sides.keys():
        if key == side2_choice:
            side2_picked = True
    if side2_picked == True:
        side2_price = sides[side2_choice]
        break
    else:
        print("Invalid choice")
while True:
    #Repeat previous step
    drink_choice = input("What would you like to drink?" )
    drink_choice = drink_choice.capitalize()
    for key in drinks.keys():
        if key == drink_choice:
            drink_picked = True
    if drink_picked == True:
        drink_price = drinks[drink_choice]
        break
    else:
        print("Invalid choice")
meal_cost = main_price+side1_price+side2_price+drink_price
#Have them choose a tip percent and calculate it.
tip = (int(input("What percent would you like to tip? ")))/100
tip_price = meal_cost*tip
#When all of it is taken, add a tax
tax = meal_cost*0.08
total = meal_cost+tip_price+tax
print(f"You order a {main_choice} with a side of {side1_choice} and {side2_choice}, with some {drink_choice} to drink.\nYour total comes out to {total:.2f}")