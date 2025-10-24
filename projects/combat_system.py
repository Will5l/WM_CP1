# WM 2nd Combat System
health = 0
defense = 0
attack = 0
damage = 0
health_potions = 3
def user_turn():
    print("What do you want to do?")
    if user_class == "Fighter":
        (f"1. Normal Attack\n 2. Second Wind\n 3. Drink Health Potion({health_potions} left)\n 4. Flee")
user_class_choice = input("What class are you?\n1 Fighter\n 2 Mage\n 3 Rogue")
if user_class_choice == "1":
    health = 30
    defense = 16
    dex_mod = 3
    str_mod = 5
    int_mod = 1
    user_class = "Fighter"
elif user_class_choice == "2":
    health = 20
    defense = 10
    dex_mod = 2
    str_mod = 1
    int_mod = 5
    user_class = "Mage"
elif user_class_choice == "3":
    health = 25
    defense = 14
    dex_mod = 5
    str_mod = 3
    int_mod = 2
    user_class = "Rogue"
