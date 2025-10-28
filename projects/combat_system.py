# WM 2nd Combat System
import random
hit = 0
fled = False
thing = 1
def mon_turn():
    global mon_health
    global health
    global defense
    while True:
        if random.randint(1,21) > defense:
            hit = True
        else:
            hit = False
            break
        turn = random.randint(1,3)
        if hit == True and turn == 1:
            damage = random.randint(1,9)+mon_damage
            health -= damage
            print(f"The wolf hit for {damage}, and you now have {health}")
            break
        elif hit == False and turn == 1:
            print("the wolf missed")
            break
        if hit == True and turn == 2:
            damage = (random.randint(1,9)+mon_damage)*2
            health -= damage
            mon_health -= damage/4
            print(f"The monster hit its wild attack for {damage}, and did {damage/4} to itself. The monster now has {mon_health}, and you have {health}")
            break
        elif hit == False and turn == 2:
            print("The wolf missed its wild attack")
            break
def user_turn():
     global mon_health
     global health
     while True:
            turn = input("What do you want to do? 1. Normal Attack\n 2. Wild Attack(hurts self for 1/4 of damage done for double damage)\n 3. Drink Health Potion\n 4. Flee\n")
            if random.randint(1,21) > mon_defense:
                hit = True
            else:
                hit = False
            if hit == True and turn == "1":
                damage = random.randint(1,9)+damage_mod
                mon_health -= damage
                print(f"You hit for {damage}, the dire wolf now has {mon_health}")
                break
            elif hit == False and turn == "1":
               print("You missed")
               break
            if hit == True and turn == "2":
                damage = (random.randint(1,9)+damage_mod)*2
                mon_health -= damage
                health -= damage/4
                print(f"You hit your wild attack for {damage}, and did {damage/4} to yourself. The monster now has {mon_health}, and you have {health}")
                break
            elif hit == False and turn == "2":
                print("You missed your wild attack")
                break
            if turn == 3:
                health += 12
                health_potions -= 1
                break
            if turn == "4":
                flee = random.randint(1,21)
                if flee > 16:
                    print("You fled")
                    fled = True
                    break
                elif flee <= 15:
                        print("You failed to flee and used up your turn")
                        break
            else:
                print("You inputed something that wasn't an option, try again")
                
user_class_choice = input("What class are you?\n1 Fighter\n 2 Mage\n 3 Rogue\n")
if user_class_choice == "1":
    health = 30
    defense = 16
    damage_mod = 4
    user_class = "Fighter"
elif user_class_choice == "2":
    health = 20
    defense = 10
    damage_mod = 2
elif user_class_choice == "3":
    health = 25
    defense = 14
    damage_mod = 3
print(f"Your a {user_class}, you have:\n{health} hp\n{defense} Ac\n{damage_mod} damage")
mon_health = 40
mon_defense = 14
mon_damage = 3
while health > 0 and mon_health > 0 and fled == False:
    if thing == True:
        mon_turn()
        user_turn()
if health > 0:
    print("The match is over and you won")
else:
    print("The monster won")