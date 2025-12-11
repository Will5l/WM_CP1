#WM 2nd Final

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
        "Name":"",
        "Damage":0,
        "Affinity":"",
    },
    "Armor":{
        "Name":"",
        "Boost":0,
    },
    "Gold":50,
    "Health potions":0,
    "Strength potions":0,
    "Speed potions":0,
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
    "\n5.Prodigy: You get 50 percent more experiance from all sources.\n6.The Accursed:half your own attack, increase enemy damage by 1.5x, make you extremly unlucky when it comes to drops\n7.The Hated:make people not offer you better things, and the things they do offer would be 50% more exspensive. You also recive half the rewards from quests.")
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
                    if perk_choice1 or perk_choice2 == 1:
                        toughskin = True
                    if perk_choice1 or perk_choice2 == 2:
                        reckless = True
                    if perk_choice1 or perk_choice2 == 3:
                        quickfooted = True
                    if perk_choice1 or perk_choice2 == 4:
                        catlike_reflexes = True
                    if perk_choice1 or perk_choice2 == 5:
                        prodigy = True
                    if perk_choice1 or perk_choice2 == 6:
                        the_accursed = True
                    if perk_choice1 or perk_choice2 == 7:
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
    player_stats["CurHealth"] = player_stats["MaxHealth"]
    point_choice = int(input("What would you like to increase, 1.health, 2.strength, or 3.dexterity. strength affects most weapons damage, while dexterity affects fleeing, who goes first in combat, and some weapons."))
    if point_choice == 1:
        player_stats["MaxHealth"] += 5
        player_stats["CurHealth"] += 5
    elif point_choice == 2:
        player_stats["Strength"] += 1
    elif point_choice == 3:
        player_stats["Dexterity"] += 1
    pass




#Enemy Stats
basic_enemies = {
    "Wolf":{
        "Health":10,
        "strength":2,
        "dexterity":1,
        "gold":0,
        "XP":25,
    },
    "Bandit":{
        "Health":15,
        "strength":1,
        "dexterity":2,
        "gold":10,
        "XP":35,
    },
    "Elite Bandit":{
        "Health":20,
        "strength":2,
        "dexterity":4,
        "gold":25,
        "XP":55,
    },
    "Corrupt Knight":{
        "Health":35,
        "strength":4,
        "dexterity":2,
        "gold":50,
        "XP":65,
    },
    "Royal Guard":{
        "Health":45,
        "strength":5,
        "dexterity":3,
        "gold":100,
        "XP":100,
    },
}

print(player_stats["Name"])

def attacks():
    pass


# Combat funtion
def combat(enemy1name,enemy2name,enemy3name,enemyamount):
    options = [1,2,3,4]
    #Enemy stats get set
    enemy1hp = basic_enemies[enemy1name["Health"]]
    enemy1str = basic_enemies[enemy1name["strength"]]
    enemy1dex = basic_enemies[enemy1name["dexterity"]]
    enemy1gold = basic_enemies[enemy1name["gold"]]
    enemy1xp = basic_enemies[enemy1name["XP"]]
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
            sp.slow_print("What would you like to do? 1.Normal attack \n2.Heavy attack \n3.look at potions \n4.Flee")
            choice = int(input())
            if choice not in options:
                print("Invalid")
            elif choice in options:
                if enemyamount == 1:
                    atk_choice = 1
                    enemy1hp, player_stats["CurHealth"]=attacks(choice,enemy1hp,atk_choice,enemy1str)
    else:
        print(f"{enemy1name} attacks")
        choice = random.randint(1,2)
        enemy1hp, player_stats["CurHealth"]=attacks(choice,enemy1hp,atk_choice,enemy1str)
    while True:
            sp.slow_print("What would you like to do? 1.Normal attack \n2.Heavy attack \n3.look at potions \n4.Flee")
            choice = int(input())
            if choice not in options:
                print("Invalid")
            elif choice in options:
                    atk_choice = 1
                    enemy1hp, player_stats["CurHealth"]=attacks(choice,enemy1hp,atk_choice,enemy1str)
                    if enemy1hp <= 0:
                        enemy1alive == False
            if enemy1alive == True:
                print(f"{enemy1name} attacks")
                choice = random.randint(1,2)
                enemy1hp, player_stats["CurHealth"]=attacks(choice,enemy1hp,atk_choice,enemy1str)
        

    pass
#make a function for normal combat
    #combat will be 1v1-1v3ish and start with checking if the players or enemies dex is higher.
    #Whoever has the higher dex will go first in the combat, and the order will go in order from the highest to lowest.
    #When the player takes a turn they will be given options, 1. Attack, 2. Heavy Attack, 3. Potions, 4. Flee
    #If they attack, the function will check the stat mod for the weapon, and then add that to the weapons damage before applying it to the enemies health and decreasing it.
    #If they choose to use heavy attack, then it calculate the damage same as the attack, before doubling it, but there is also a 40% chance it misses and you lose your turn.
    #If they choose to use potions, it will open their bag, and list all their potions with numbers and the amount of them, with the boost they give. There will also be an additional option to shut the bag after opening it and going back to your options.
    #If they choose to flee, then a value will be retreived from a dictionary that represents the escape chance as a percent for each type of monster. Dex is then doubled and added to it. If it equals or exceeds 100% then they will guaranteed escape. otherwise they waste the turn trying to escape, and rng decides if they do or not
    #After the players turn, or if the monster has higher dex it will take its turn.
    #The monster will have a chance to either normal attack, or do a heavy attack, with a 70% chance and 30% respectivly, and the damage will be calculated the same way as the player, from a dictionray where the enemy stats are stored.
    #After the monster attacks or fails to attack play will go to the next, which will either, return to the character, or the next monster, and will repeat these same steps until either the player flees succesfully, kills the monsters, or the player dies.
    #If the player dies then they will get a game over text and the option to play again.
    #If they flee it will say they fled and will return them to whatever location they were at before combat started.
    #If they win they will get a battle win text, telling them how much xp they got, if they leveled up, if they got gold, and if they got any items.
def town1():
    pass
def town2():
    pass
def town3():
    pass
def forestOrSomething():
    pass



def castle():
    pass
#each of the 3 towns/villages will be a function
    #when they enter each town, the text will greet them, saying something similar to "welcome to x"
    #It will then present them with options for the town.
        #Each of the three towns will have the same options locations wise, but the items in each shop and the prices would change, with one being worse, one being mediumish, and one being end game geared.
    #The first will be the gear shop
        #The gear shop would have the armor and the weapons that the player can buy.
        #The shopkeep would greet them and then they would get a list that displays the items and their cost.
            #there would be a dictionary for each shop, with the key being the items name and the value being the items cost. The stats would be given in parenthases
        #The last option would be to go back outside, and the shopkeep would say bye to them as they leave.
    #The second option would be to go to an apothecary
        #The player would be greeted with a slightly different text then before.
        #The potions would then be displayed, with the names and prices, alongside stats
            #The potions would also be stored in a dictionary.
    #The third shop would be a stable
        #The stable would, of course, sell/rent horses to the player.
        #The horses would have varying prices depending on its stats.
        #The horses would mostly be useful for decreasing the chance of you getting attacked by bandits while traveling between locations
            #Certain more expensive horses would also get you from point a to b in one day, so you wouldn't hvae to experince a night outside walls, and risk getting robbed or ambushed.
    #You'd be able to sell things in their respective shops.
    #There would also be a quest board of sorts, which would mostly be combat things, like go clear out a bandit camp or something in the woods near the town. These would reward the player with extra gold and xp, but also usually be harder than random encounters.
        #There would only be 2 quests, with different diffuclty depending on which town its in.
        #After the quest is taken, a new location would appear in the location select, that would be named something like "Bandit Camp" if thats the quest they choose.
        #When they choose it, there would be travel text, and of course the chance of being ambushed like any other travel, but once they make it there, combat starts immediatly.
    #The last option would be to travel to another location.
        #When they choose this option it would display all the other locations names, that are accesiable.
            #If they go to choose the castle, which is the final area and does not let you leave after entering, it would display a warning message twice to make sure they are ready, as they can't leave once they go there.
    #When the character finally decides to go to the castle, it would print text describing the castle, it would be gloomy and despairing. Combat would quickly start with higher level enemies, and you would have to fight through 3 waves of enemies before the base, with there only being a break right before the boss to rest and regain your health from it. None of these battles will allow the player to flee.
        #There would be two different endings here.
            #The first would be the good ending where you defeat the final boss and save the kingdom
            #The second would be the bad ending, where you die to the final boss and the kingdom falls.
    #The boss fight would be different from other fights.
    #The boss would of course have more health then the average enemy, alongside more damage, but they can also summon 2 of the unit you fought waves of to reach him to aid him in combat. These would be slightly weaker variants to make it easier, and he would only summon them every 4 turns, and can't have more than 2.
        #On the first round the boss would spawn with 2 of the weaker variants already there, and the count would start there. 5 rounds later, a conditional would check if they are alive. each one would be labled and have a boolean that is True if they live, and False if they are dead.
        #They are only summoned if its False