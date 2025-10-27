# WM 2nd Combat System
import random
turn = 0
health = 0
defense = 0
attack = 0
damage = 0
health_potions = 3
dmg_die_low = 0
dmg_die_high = 0
fled == False
def attacks(dex,ac,str,low,high,hp, shp):
    global turn
    global damage
    global attack
    global hit
    if turn == "1":
        attack = dex+random.randint(1,21)
        if attack > ac:
            hit = True
            damage =str+random.randint(low,high)
            hp -= damage
        elif attack <= ac:
            hit = False
    elif turn == "2" and user_class != "Mage":
        attack = dex+random.randint(1,21)
        if attack > ac:
            hit = True
            damage = (str+random.randint(low,high))*2
            hp -= damage
            shp -= damage/4
    else:
        print("")

def mon_turn():
    global turn
    global mon_dex_mod
    print("The dire wolf is attacking")
    turn == random.randint(1,3)
    def attacks(mon_dex_mod,defense,mon_str_mod,mon_dmg_die_low,mon_dmg_die_high,mon_health)
    if hit == True:
        print("")
def user_turn():
    print("What do you want to do?")
    global turn
    while True:
        if user_class == "Fighter":
            turn = input(f"1. Normal Attack\n 2. Wild Attack(hurts self for 1/4 of damage done for double damage)\n 3. Drink Health Potion({health_potions} left)\n 4. Flee")
            attacks(dex_mod,mon_defense,str_mod,dmg_die_low,dmg_die_high,mon_health,health)
            if hit == True and turn == "1":
                print(f"You hit for {damage}, the dire wolf now has {mon_health}")
                break
            elif hit == False and turn == "1":
               print("You missed")
               break
            if hit == True and turn == "2":
                print(f"You hit your wild attack for {damage}, and did {damage/4} to yourself. The monster now has {mon_health}, and you have {health}")
                break
            elif hit == False and turn == "2":
                print("You missed your wild attack")
                break
            if turn == 3 and health_potions > 0:
                health += 12
                health_potions -= 1
                break
            elif turn == 3 and health_potions <= 0:
                print("Your out of health potions, you use up your turn looking for something you don't have")
                break
            if turn == "4":
                flee = dex_mod+random.randint(1,21)
                if flee > 16:
                    global fled
                    print("You fled")
                    fled = True
                    break
                elif flee <= 15:
                        print("You failed to flee and used up your turn")
                        break
            else:
                print("You inputed something that wasn't an option, try again")
        elif user_class == "Mage":
            turn = input(f"1. Normal Attack\n 2. Fireball\n 3. Drink Health Potion({health_potions} left)\n 4. Flee")
            attacks(dex_mod,mon_defense,str_mod,dmg_die_low,dmg_die_high,mon_health,health)
            if hit == True:
                print(f"You hit for {damage}, the dire wolf now has {mon_health}")
                break
            elif hit == False:
                print("You missed")
                break
            if turn == 2:
                print("You cast Fireball")
                if mon_dex_mod+random.randint(1,21) > 16:
                    damage = random.randint(1,7)+random.randint(1,7)+random.randint(1,7)
                    print("The monster succecefully made a saving throw and took half damage, {damage}, and its hp is now {mon_health}")
            if turn == 3 and health_potions > 0:
                health += 12
                health_potions -= 1
                break
            elif turn == 3 and health_potions <= 0:
                print("Your out of health potions, you use up your turn looking for something you don't have")
                break
            if turn == "4":
                flee = dex_mod+random.randint(1,21)
                if flee > 16:
                    global fled
                    print("You fled")
                    fled = True
                    break
                elif flee <= 15:
                    print("You failed to flee and used up your turn")
                    break
            else:
                print("You inputed something that wasn't an option, try again")        
        elif user_class == "Rogue":
            turn = input(f"1. Normal Attack\n 2. Wild Attack(hurts self for 1/4 of damage done for double damage)\n 3. Drink Health Potion({health_potions} left)\n 4. Flee")
            attacks(dex_mod,mon_defense,str_mod,dmg_die_low,dmg_die_high,mon_health,health)
            if hit == True:
                print(f"You hit for {damage}, the dire wolf now has {mon_health}")
                break
            elif hit == False:
                print("You missed")
                break
            if hit == True and turn == "2":
                print(f"You hit your wild attack for {damage}, and did {damage/4} to yourself. The monster now has {mon_health}, and you have {health}")
                break
            elif hit == False and turn == "2":
                print("You missed your wild attack")
                break
            if turn == 3 and health_potions > 0:
                health += 12
                health_potions -= 1
                break
            elif turn == 3 and health_potions <= 0:
                print("Your out of health potions, you use up your turn looking for something you don't have")
                break
            if turn == "4":
                flee = dex_mod+random.randint(1,21)
                if flee > 16:
                    global fled
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
    dex_mod = 3
    str_mod = 5
    int_mod = 1
    dmg_die_low = 1
    dmg_die_high = 9
    user_class = "Fighter"
elif user_class_choice == "2":
    health = 20
    defense = 10
    dex_mod = 2
    str_mod = 1
    int_mod = 5
    dmg_die_low = 1
    dmg_die_high = 5
    user_class = "Mage"
elif user_class_choice == "3":
    health = 25
    defense = 14
    dex_mod = 5
    str_mod = 3
    int_mod = 2
    dmg_die_low = 1
    dmg_die_high = 7
    user_class = "Rogue"
print(f"Your a {user_class}, you have:\n{health} hp\n{defense} AC\n+{dex_mod} dex mod\n+{str_mod} str mod\n+{int_mod} int mod")

mon_health = 40
mon_str_mod = 3
mon_dex_mod = 2
mon_dmg_die_low = 1
mon_dmg_die_high = 13
mon_defense = 14
while health > 0 and mon_health > 0:
    user_inti = dex_mod+random.randint(1,21)
    mon_inti = mon_dex_mod+random.randint(1,21)
    if fled == True:
        break
    if user_inti >= mon_inti:
        user_turn()
        mon_turn()
    elif user_inti < mon_inti:
        mon_turn()
        user_turn()
if fled == True:
    print("You fled from battle")
elif mon_health <= 0:
    print("You won the battle")
elif health <= 0:
    print("The dire wolf won")