# WM 2nd Order up
#Make 3 different dictionaries to store mains, sides, and drinks
main_picked = False
side1_picked = False
side2_picked = False
drink_picked = False
mains = {
 "Burger": 5.99,
 "Steak": 7.99,
 "Sandwich": 6.99,
 "Grilled Cheese": 4.99,
}
sides = {
    "Steak fries": 1.99,
    "Curly fries": 1.99,
    "Sweet potato fries": 1.99,
    "Tater Tots": 1.99
}
drinks = {
    "Water": 1.99,
    "Sprite": 1.99,
    "Pepsi": 1.49,
    "Cream soda": 1.49
}
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
while main_picked == False:
    main_choice = input("What would you like for your main?" )
#Have each choice grab that item if it exists, and add the price to a total
#When all of it is taken, add a tax