# WM 2nd Order up
#Make 3 different dictionaries to store mains, sides, and drinks
main_picked = False
side1_picked = False
side2_picked = False
drink_picked = False
main = {
 'Burger': 5.99,
 'Steak': 7.99,
 'Sandwich': 6.99,
 'Grilled cheese': 4.99,
}
side = {
    'Steak fries': 1.99,
    'Curly fries': 1.99,
    'Sweet potato fries': 1.99,
    'Tater tots': 1.99
}
drink = {
    'Water': 1.99,
    'Sprite': 1.99,
    'Pepsi': 1.49,
    'Cream soda': 1.49
}
#Function that handles the ordering, returning the prices and the dish choosen
def order(dict, choosing):
    while True:
        choice = input(f"What would you like for your {choosing}?" )
        choice = choice.capitalize()
        for key in dict.keys():
            if key == choice:
                picked = True
        if picked == True:
            price = dict[choice]
            picked == False
            return price, choice
            break
        else:
            print("Invailid choice")
#Print the menu and prices
print("Mains")
for key in main.keys():
    print(f"{key} : {main[key]}")
print("Sides")
for key in side.keys():
    print(f"{key} : {side[key]}")
print("Drinks")
for key in drink.keys():
    print(f"{key} : {drink[key]}")
#Have a function that runs while variables for main the 2 sides and drink are false, and have them be made true when they choose a valid item.
    #Have a variable that stores their choice and have a for loop check if its vaild, if it is, save its price, and break out of the loop.
main_price, main_choice = order(main, "main")
side1_price, side1_choice = order(side, "first side")
side2_price, side2_choice = order(side, "second side")
drink_price, drink_choice = order(drink, "drink")
meal_cost = main_price+side1_price+side2_price+drink_price
#Have them choose a tip percent and calculate it.
tip = (int(input("What percent would you like to tip? ")))/100
tip_price = meal_cost*tip
#When all of it is taken, add a tax
tax = meal_cost*0.08
total = meal_cost+tip_price+tax
print(f"You ordered a {main_choice} with a side of {side1_choice} and {side2_choice}, with a {drink_choice} to drink.\nYour total comes out to {total:.2f}")