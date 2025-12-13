#WM 2nd Final
import sys
import random
import slow_print as sp


player_stats={

}
perk_list_thing = {
    1:"ToughSkin",
    2:"Reckless",
    3:"Quick-footed",
    4:"Cat-like reflexes",
    5:"Prodigy",
    6:"The Accursed",
    7:"The Hated",
}
#Game setup function
def gameSetup():
    #setting stats
    global player_stats
    global inventory
    global artifacts
    hp_mod = 0
    str_mod = 0
    dex_mod = 0
    player_stats = {
    "CurHealth":15,
    "MaxHealth":15,
    "Strength":1,
    "Dexterity":1,
    "Level":1,
    "XP":0,
    "XPrq":100,
    "Name":"",
    "Perk1":"",
    "Perk2":""
    }


    #setting inventory
    inventory = {
    "Sword":{
        "Name":"Copper Shortsword",
        "Damage":4,
        "Affinity":"Strength",
    },
    "Gold":50,
    "Health potions":0,
}
    

    #Setting artifacts
    artifacts = {
        "Wolf-fang necklace":{
            "Obtained":False,
            "Boost to health":0,
            "Boost to strength":2,
            "Boost to dexterity":0,
            "Hint":"Quest"
        },
        "Hermes shoes":{
            "Obtained":False,
            "Boost to health":0,
            "Boost to strength":0,
            "Boost to dexterity":2,
            "Hint":"Quest"
        },
        "Captain's chainmail":{
            "Obtained":False,
            "Boost to health":5,
            "Boost to strength":0,
            "Boost to dexterity":0,
            "Hint":"Quest"
        },
        "Enchanted Ring":{
            "Obtained":False,
            "Boost to health":5,
            "Boost to strength":1,
            "Boost to dexterity":1,
            "Hint":"Quest"
        }
    }


    #Setting perks
    global toughskin
    global reckless
    global quickfooted
    global catlike_reflexes
    global prodigy
    global the_accursed
    global the_hated

    toughskin = False
    reckless = False
    quickfooted = False
    catlike_reflexes = False
    prodigy = False
    the_accursed = False
    the_hated = False



    #Name setup and stats
    x = 26
    while x > 25:
        player_stats["Name"] = input("Choose a name with up to 25 characters\n")
        x = 0
        for i in player_stats["Name"]:
            x += 1
        if x > 25:
            print("Too long")
            continue
    print(f"Greetings, {player_stats["Name"]}")
    print("You are allowed to allocate 2 skill points to begin with")
    a = 0
    while a != 2:
        point_choice = int(input("What would you like to increase, 1.health, 2.strength, or 3.dexterity. strength affects most weapons damage, while dexterity affects fleeing, who goes first in combat, and some weapons."))
        if point_choice == 1:
            player_stats["MaxHealth"] += 5
            player_stats["CurHealth"] += 5
            a += 1
        elif point_choice == 2:
            player_stats["Strength"] += 1
            a += 1
        elif point_choice == 3:
            player_stats["Dexterity"] += 1
            a += 1
        else:
            print("Invalid choice")



    #Perk setup
    print("\nYou can choose up to two perks, with buffs, and sometimes debuffs.")
    sp.slow_print("\nHere is the list of perks you can choose from:\n1.ToughSkin:You have a flatout 20 percent damage reduction\n2.Reckless:You always land heavy attacks, but at the cost of taking 1/3 of the damage they deal" \
    "\n3.Quick-footed:When combat starts your dex checks gets an additonal 50 percent effectivness, and so does your fleeing.\n4.Cat-like Reflexes: have a 20 percent chance to dodge an attack, alongside all dex related things getting 30 percent more effectivness. Have 1/3 less hp" \
    "\n5.Prodigy: You get 50 percent more experiance from all sources.\n6.The Accursed:half your own attack, increase enemy damage by 1.5x, make you extremly unlucky when it comes to drops\n7.The Hated:make people not offer you better things, and the things they do offer would be 50% more exspensive. You also recive half the rewards from quests. (last two not implemented yet)")
    while True:
        perk_choice1 = int(input("Enter the number that corresponds with the perk: "))
        perk_choice2 = int(input("Enter the number that corresponds with the perk: "))
        if perk_choice1 == perk_choice2:
            print("You can't have the same perk twice")
            continue
        elif perk_choice1 != perk_choice2:
            if perk_choice1 in perk_list_thing:
                if perk_choice2 in perk_list_thing:
                    print(f"You have choosen {perk_list_thing[perk_choice1]}, and {perk_list_thing[perk_choice2]}")
                    player_stats["Perk1"] = {perk_list_thing[perk_choice1]}
                    player_stats["Perk2"] = {perk_list_thing[perk_choice2]}
                    if perk_choice1 == 1 or perk_choice2 == 1:
                        toughskin = True
                    if perk_choice1 == 2 or perk_choice2 == 2:
                        reckless = True
                    if perk_choice1 == 3 or perk_choice2 == 3:
                        quickfooted = True
                    if perk_choice1 == 4 or perk_choice2 == 4:
                        player_stats["MaxHealth"] -= 5
                        player_stats["CurHealth"] -= 5
                        catlike_reflexes = True
                    if perk_choice1 == 5 or perk_choice2 == 5:
                        prodigy = True
                    if perk_choice1 == 6 or perk_choice2 == 6:
                        the_accursed = True
                    if perk_choice1 == 7 or perk_choice2 == 7:
                        the_hated = True
                    break
                elif perk_choice2 not in perk_list_thing:
                    print("Invalid choice")
                    pass
            elif perk_choice1 not in perk_list_thing:
                print("Invalid choice")
    #Intro text
    sp.slow_print("intro thing here")

    
    return hp_mod,str_mod,dex_mod,player_stats,toughskin,reckless,quickfooted,catlike_reflexes,prodigy,the_accursed,the_hated,inventory,artifacts
hp_mod,str_mod,dex_mod,player_stats,toughskin,reckless,quickfooted,catlike_reflexes,prodigy,the_accursed,the_hated,inventory,artifacts = gameSetup()
print(player_stats)

#Level up
def levelUp():
    while True:
        player_stats["CurHealth"] = player_stats["MaxHealth"]
        point_choice = int(input("What would you like to increase, 1.health, 2.strength, or 3.dexterity. strength affects most weapons damage, while dexterity affects fleeing, who goes first in combat, and some weapons."))
        if point_choice == 1:
            player_stats["MaxHealth"] += 5
            player_stats["CurHealth"] += 5
            player_stats["XP"] -= player_stats["XPrq"]
            player_stats["XPrq"] *= 1.2
        elif point_choice == 2:
            player_stats["Strength"] += 1
            player_stats["XP"] -= player_stats["XPrq"]
            player_stats["XPrq"] *= 1.2
        elif point_choice == 3:
            player_stats["Dexterity"] += 1
            player_stats["XP"] -= player_stats["XPrq"]
            player_stats["XPrq"] *= 1.2
        else:
            print("Invalid")
        if player_stats["XP"] >= player_stats["XPrq"]:

            continue
        elif player_stats["XP"] < player_stats["XPrq"]:
            break
    return player_stats

#Enemy Stats
basic_enemies = {
    "Wolf":{
        "Health":10,
        "strength":2,
        "weapondmg":2,
        "dexterity":1,
        "gold":0,
        "XP":25,
    },
    "Bandit":{
        "Health":15,
        "strength":1,
        "weapondmg":3,
        "dexterity":2,
        "gold":10,
        "XP":35,
    },
    "Elite Bandit":{
        "Health":20,
        "strength":2,
        "weapondmg":4,
        "dexterity":4,
        "gold":25,
        "XP":55,
    },
    "Corrupt Knight":{
        "Health":35,
        "strength":4,
        "weapondmg":6,
        "dexterity":2,
        "gold":50,
        "XP":65,
    },
    "Royal Guard":{
        "Health":45,
        "strength":5,
        "weapondmg":8,
        "dexterity":3,
        "gold":100,
        "XP":100,
    },
    "boss": {
    "Health":200,
    "strength":8,
    "weapondmg":15,
    "dexterity":6,
    "gold":100,
    "XP":100,
}
}


#Attack Function
def attacks(choice,e1hp,e1str,e1wdmg,t):
    flee = False
    if t == player_stats["Name"]:
        if choice == 1 or 2:
            dmg = player_stats[inventory["Sword"]["Affinity"]]+inventory["Sword"]["Damage"]+random.randint(1,5)
            if choice == 1:
                e1hp -= dmg
                print(f"You hit for {dmg}, leaving the enemy at {e1hp}")
                return e1hp, player_stats["CurHealth"], flee, inventory
            elif choice == 2 and reckless == True:
                e1hp -= dmg*2
                player_stats["CurHealth"] -= round(dmg*.3, 0)
                sdmg = round(dmg*.3, 0)
                print(f"You hit for {dmg}, leaving the enemy at {e1hp}, but your recklessness also caused you to take {sdmg} yourself")
                return e1hp, player_stats["CurHealth"], flee, inventory
            elif choice == 2 and reckless == False:
                if random.randint(1,100) >= 40:
                    e1hp -= dmg*2
                    print(f"You hit for {dmg}, leaving the enemy at {e1hp}")
                return e1hp, player_stats["CurHealth"], flee, inventory
        if choice == 3:
            print(inventory["Health potions"])
            if (inventory["Health potions"]) == 0:
                print("You spend your turn franticly looking for something you don't have")
                return e1hp, player_stats["CurHealth"], flee, inventory
            if inventory["Potions"]["Health potions"] > 0:
                print("You drink a health potion and heal")
                inventory["Potions"]["Health potions"] -= 1
                player_stats["CurHealth"] += player_stats["MaxHealth"]*.4
                if player_stats["CurHealth"] > player_stats["MaxHealth"]:
                    player_stats["CurHealth"] = player_stats["MaxHealth"]
            return e1hp, player_stats["CurHealth"], flee, inventory
        if choice == 4:
            if catlike_reflexes == True and quickfooted == True:
                player_stats['Dexterity'] *= 1.8
            elif catlike_reflexes == True:
                player_stats['Dexterity'] *= 1.3
            elif quickfooted == True:
                player_stats['Dexterity'] *= 1.5
            if random.randint(1,100) < player_stats["Dexterity"]:
                flee = True
                return e1hp, player_stats["CurHealth"], flee, inventory
    elif t == "enemy":
        dmg = e1str+e1wdmg+random.randint(1,5)
        if choice == 1 and toughskin == False:
            player_stats["CurHealth"] -= dmg
            print(f"The enemy hit you for {dmg}, leaving you at {player_stats["CurHealth"]}")
            return e1hp, player_stats["CurHealth"], flee, inventory
        elif choice == 2 and toughskin == False:
            if random.randint(1,100) >= 40:
                dmg *= 2
                player_stats["CurHealth"] -= dmg
                print(f"The enemy hit you for {dmg}, leaving you at {player_stats["CurHealth"]}")
            else:
                print("The enemy missed!")
            return e1hp, player_stats["CurHealth"], flee, inventory
        elif choice == 1 and toughskin == True:
            player_stats["CurHealth"] -= round(dmg*.8)
            print(f"The enemy hit you for {dmg}, leaving you at {player_stats["CurHealth"]}")
            return e1hp, player_stats["CurHealth"], flee, inventory
        elif choice == 2 and toughskin == True:
            if random.randint(1,100) >= 40:
                dmg *= 2
                player_stats["CurHealth"] -= dmg
                print(f"The enemy hit you for {dmg}, leaving you at {player_stats["CurHealth"]}")
            else:
                print("The enemy missed!")
            return e1hp, player_stats["CurHealth"], flee, inventory
    


# Combat funtion
def combat(enemy1name,player_stats):
    options = [1,2,3,4]
    #Enemy stats get set
    flee = False
    skip = False
    base_dex = player_stats["Dexterity"]
    enemy1hp = basic_enemies[enemy1name]["Health"]
    enemy1str = basic_enemies[enemy1name]["strength"]
    enemy1wdmg = basic_enemies[enemy1name]["weapondmg"]
    enemy1dex = basic_enemies[enemy1name]["dexterity"]
    enemy1gold = basic_enemies[enemy1name]["gold"]
    enemy1xp = basic_enemies[enemy1name]["XP"]
    enemy1alive = True
    player_stats['Dexterity'] += dex_mod
    player_stats["Strength"] += str_mod
    player_stats["MaxHealth"] += hp_mod
    player_stats["CurHealth"] += hp_mod
    #Setting up functions for enemy combat
    enemy_first = False
    player_first = False
    print(f"{enemy1name} enters combat with you")
    if catlike_reflexes == True and quickfooted == True:
        player_stats['Dexterity'] *= 1.8
    elif catlike_reflexes == True:
        player_stats['Dexterity'] *= 1.3
    elif quickfooted == True:
        player_stats['Dexterity'] *= 1.5
    if player_stats["Dexterity"] >= enemy1dex:
        print(f"{player_stats["Name"]} attacks first")
        player_first = True
    elif player_stats["Dexterity"] < enemy1dex:
        print("Enemies go first")
        enemy_first = True
    if player_first == True:
        while True:
            flee = False
            turn = player_stats["Name"]
            sp.slow_print("What would you like to do? \n1.Normal attack \n2.Heavy attack \n3.look at potions \n4.Flee")
            choice = int(input())
            if choice not in options:
                print("Invalid")
            elif choice in options:
                    atk_choice = 1
                    enemy1hp, player_stats["CurHealth"], flee, inventory=attacks(choice,enemy1hp,enemy1str,enemy1wdmg,turn)
                    if enemy1hp <= 0:
                        enemy1alive = False
                    break
    if flee == False:
        flee = False
        if enemy1alive == True:
            turn = "enemy"
            print(f"{enemy1name} attacks")
            choice = random.randint(1,2)
            if catlike_reflexes == True:
                if random.randint(1,100) <= 20:
                    print("You dodged with your reflexes")
                else:
                    enemy1hp, player_stats["CurHealth"], flee, inventory=attacks(choice,enemy1hp,enemy1str,enemy1wdmg,turn)
        elif enemy1alive == False:
            skip = True
    while enemy1alive == True and player_stats["CurHealth"] >= 0 and flee == False:
            flee = False
            sp.slow_print("What would you like to do? \n1.Normal attack \n2.Heavy attack \n3.look at potions \n4.Flee")
            choice = int(input())
            if choice not in options:
                print("Invalid")
            elif choice in options:
                    turn = player_stats["Name"]
                    enemy1hp, player_stats["CurHealth"], flee, inventory=attacks(choice,enemy1hp,enemy1wdmg,turn)
                    if enemy1hp <= 0:
                        enemy1alive == False
            if enemy1alive == True:
                turn = "enemy"
                print(f"{enemy1name} attacks")
                choice = random.randint(1,2)
                if enemy1alive == False:
                    print(f"You defeated {enemy1name}")
                    break
                elif catlike_reflexes == True:
                    if random.randint(1,100) <= 20:
                        print("You dodged with your reflexes")
                    else:
                        enemy1hp, player_stats["CurHealth"], flee, inventory=attacks(choice,enemy1hp,enemy1str,enemy1wdmg,turn)
    if player_stats["CurHealth"] <= 0:
        print("You died")
        thing = input("Would you like to try again? y/n")
        if thing == "y":
            gameSetup()
        elif thing == "n":
            sys.exit()
        pass
    elif flee == True:
        print("You fled from combat")
        player_stats["Dexterity"] = base_dex
        return player_stats, inventory
    elif enemy1alive == False:
        print("You killed the wolf")
        player_stats["Dexterity"] = base_dex
        if prodigy == True:
            enemy1xp *= 1.5
        player_stats["XP"] += enemy1xp
        if player_stats["XP"] >= player_stats["XPrq"]:
            player_stats = levelUp()
        inventory["Gold"] += enemy1gold
        print(f"your stats now look like this after the fight:{player_stats}\n{inventory}")
        return player_stats, inventory



def swordTown():
    print("Welcome to town1")
    global player_stats
    global inventory
    while True:
        choice = int(input("What would you like to do?\n1.Gear shop\n2.Apothecary\n3.Go somewhere else\n"))
        if choice == 1:
            choice = int(input("Welcome to the gear shop. What would you like to do?\n1.Buy something\n2.leave\n"))
            if choice == 1:
                choice = int(input("1.Iron sword - 50g - 6dmg\n2.Steel sword - 150g - 10dmg\n3.go back\n"))
                if choice == 1 and inventory["Gold"] >= 50:
                    print("You bought the Iron sword")
                    inventory["Sword"]["Name"] = "Iron sword"
                    inventory["Sword"]["Damage"] = 6
                    inventory["Sword"]["Affinity"] = "Strength"
                    inventory["Gold"] -= 50
                elif choice == 1 and inventory["Gold"] < 50:
                    print("You can't afford that")
                elif choice == 2 and inventory["Gold"] >= 150:
                    print("You bought the Steel sword")
                    inventory["Sword"]["Name"] = "Steel sword"
                    inventory["Sword"]["Damage"] = 10
                    inventory["Sword"]["Affinity"] = "Strength"
                    inventory["Gold"] -= 150
                elif choice == 2 and inventory["Gold"] < 150:
                    print("You can't afford that")
                elif choice == 3:
                    continue
        elif choice == 2:
            choice = int(input("Welcome to the Apothocary, what would you like to do?\n1.buy health potion\n2.buy 5 health potions\n3.leave\n"))
            if choice == 1 and inventory["Gold"] >= 10:
                print("You purchased one health potion!")
                inventory["Health potions"] += 1
                inventory["Gold"] -= 10
            elif choice == 1 and inventory["Gold"] < 10:
                print("You can't afford that")
            elif choice == 2 and inventory["Gold"] >= 50:
                print("You bought 5 health potions.")
                inventory["Health potions"] += 5
                inventory["Gold"] -= 50
            elif choice == 2 and inventory["Gold"] < 50:
                print("You can't afford that")
            elif choice == 3:
                continue
        elif choice == 3:
            choice = int(input("Where would you like to go?\n1.town2\n2.The dungeon\n3.The Castle\n4.Stay here\n"))
            if choice == 1:
                area = betterSwordTown()
                return area
            elif choice == 2:
                area = dungeon()
                return area
            elif choice == 3:
                choice = input("Are you sure you want to go to the castle? You can't leave it once you do. y/n\n")
                if choice == "y":
                    area = castle()
                    return area
                elif choice == "n":
                    continue
            elif choice == 4:
                continue
            pass
        else:
            print("Invalid")


def betterSwordTown():
    print("Welcome to town2")
    global player_stats
    global inventory
    while True:
        choice = int(input("What would you like to do?\n1.Gear shop\nApothecary\n3.Go somewhere else\n"))
        if choice == 1:
            choice = int(input("Welcome to the gear shop. What would you like to do?\n1.Buy something\n2.leave\n"))
            if choice == 1:
                choice = int(input("1.Titanium sword - 300g - 15dmg\n2.Mythril sword - 1250g - 40dmg\n3.go back\n"))
                if choice == 1 and inventory["Gold"] >= 300:
                    print("You bought the Iron sword")
                    inventory["Sword"]["Name"] = "Titanium sword"
                    inventory["Sword"]["Damage"] = 15
                    inventory["Sword"]["Affinity"] = "Strength"
                    inventory["Gold"] -= 300
                elif choice == 1 and inventory["Gold"] < 300:
                    print("You can't afford that")
                elif choice == 2 and inventory["Gold"] >= 1250:
                    print("You bought the Steel sword")
                    inventory["Sword"]["Name"] = "Mythril sword"
                    inventory["Sword"]["Damage"] = 40
                    inventory["Sword"]["Affinity"] = "Strength"
                    inventory["Gold"] -= 1250
                elif choice == 2 and inventory["Gold"] < 1250:
                    print("You can't afford that")
                elif choice == 3:
                    continue
        elif choice == 2:
            choice = int(input("Welcome to the Apothocary, what would you like to do?\n1.buy health potion\n2.buy 5 health potions\n3.leave\n"))
            if choice == 1 and inventory["Gold"] >= 10:
                print("You purchased one health potion!")
                inventory["Health potions"] += 1
                inventory["Gold"] -= 10
            elif choice == 1 and inventory["Gold"] < 10:
                print("You can't afford that")
            elif choice == 2 and inventory["Gold"] >= 50:
                print("You bought 5 health potions.")
                inventory["Health potions"] += 5
                inventory["Gold"] -= 50
            elif choice == 2 and inventory["Gold"] < 50:
                print("You can't afford that")
            elif choice == 3:
                continue
        elif choice == 3:
            choice = int(input("Where would you like to go?\n1.town1\n2.The dungeon\n3.The Castle\n4.Stay here\n"))
            if choice == 1:
                area = swordTown()
                return area
            elif choice == 2:
                area = dungeon()
                return area
            elif choice == 3:
                choice = input("Are you sure you want to go to the castle? You can't leave it once you do. y/n\n")
                if choice == "y":
                    area = castle()
                    return area
                elif choice == "n":
                    continue
            elif choice == 4:
                continue
            pass
        else:
            print("Invalid")
    pass
def dungeon():
    global player_stats
    global inventory
    print("Welcome to the dungeon")
    while True:
        choice = int(input("What would you like to do?\n1.Fight\n2.Leave\n"))
        if choice == 1:
            thing = input("What enemy would you like to fight?\nWolf\nBandit\nElite Bandit\nCorrupt Knight\nRoyal Guard\n(Enter the name EXACTLY)\n")
            player_stats, inventory = combat(thing, player_stats)
            continue
        elif choice == 2:
            choice = int(input("Where would you like to go?\n1.town1\n2.town2\n3.The Castle\n4.Stay here\n"))
            if choice == 1:
                area = swordTown()
                return area
            elif choice == 2:
                area = betterSwordTown()
                return area
            elif choice == 3:
                choice = input("Are you sure you want to go to the castle? You can't leave it once you do. y/n\n")
                if choice == "y":
                    area = castle()
                    return area
                elif choice == "n":
                    continue
            elif choice == 4:
                continue
            pass
        else:
            print("Invalid")
    pass


def castle():
    global player_stats
    global inventory
    print("Welcome to the castle, the final fights are ahead")
    combat("Royal Guard",player_stats)
    combat("Royal Guard",player_stats)
    combat("Royal Guard",player_stats)
    print("You've reached the final boss")
    combat("boss",player_stats)
    print("You did it! you won")
    thing = input("Would you like to try again? y/n\n")
    if thing == "y":
        gameSetup()
    elif thing == "n":
        sys.exit()
    pass
area = swordTown


while True:
    area = area()