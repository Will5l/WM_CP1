#WM 2nd Final
#Create the player stats as a dictionary with starting values
#Player_stats
perk_list_thing = {
    1:"ToughSkin",
    2:"Reckless",
    3:"Quick-footed",
    4:"Cat-like reflexes",
    5:"Prodigy",
    6:"The Accursed",
    7:"The Hated",
}
def gameSetup():
    hp_mod = 0
    str_mod = 0
    dex_mod = 0
    player_stats = {
    "Health":15 +hp_mod,
    "Strength":1 +str_mod,
    "Dexterity":1 +dex_mod,
    "Level":1,
    "Name":"",
    "Perk1":"",
    "Perk2":""
    }
    toughskin = False
    reckless = False
    quickfooted = False
    catlike_reflexes = False
    prodigy = False
    the_accursed = False
    the_hated = False
    perk_list = {
        "ToughSkin":"", #They have a flatout 20% damage reduction
        "Reckless":"", #They always land heavy attacks, but at the cost of taking 1/3 of the damage they deal.
        "Quick-footed":"", #When combat starts their dex check gets an additonal 50% effectivness, and so does their fleeing.
        "Cat-like reflexes":"", #Is immune to being ambushed, so ambushs are just normal combat, and has 20% chance to dodge an attack. Has 1/3 less hp due to avoiding most things and not becoming resilent.
        "Prodigy":"", #Gets 50% more experiance from all sources
        #These two exist solely to make the game harder for people who want that
        "The Accursed":"", #half your own attack, increase enemy damage by 1.5x, make you extremly unlucky when it comes to drops
        "The Hated":"", #make people not offer you better things, and the things they do offer would be 50% more exspensive. You also recive half the rewards from quests.
    }
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
    print("You can choose up to two perks, with buffs, and sometimes debuffs.")
    print("Here is the list of perks you can choose from:\n1.ToughSkin:You have a flatout 20 percent damage reduction\n2.Reckless:You always land heavy attacks, but at the cost of taking 1/3 of the damage they deal" \
    "\n3.Quick-footed:When combat starts your dex check gets an additonal 50 percent effectivness, and so does your fleeing.\n4.Cat-like Reflexes: you are immune to being ambushed, so ambushs are just normal combat, and have a 20 percent chance to dodge an attack. Have 1/3 less hp" \
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
    
    print("intro thing here")


    
    return hp_mod,str_mod,dex_mod,player_stats,toughskin,reckless,quickfooted,catlike_reflexes,prodigy,the_accursed,the_hated
hp_mod,str_mod,dex_mod,player_stats,toughskin,reckless,quickfooted,catlike_reflexes,prodigy,the_accursed,the_hated = gameSetup()
print(player_stats)

#Gear
    #The player will have a menu which will tell them what they have equipped and the boosts it gives.
    #They will have armor which increases hp and their weapon increases damage, along with a few item slots for things like magic rings and such that increases stats.

#Items
    #Items will be a dictionary of if they are collected or not. Each item will have a True or False value, False if it has yet to be collected, True if it has.
    #The room the item spawns will check if it is False and if it is will say that they found it, and change it to True.
    #If they reenter the same room, and the value is True, it will not mention the item.
    #When the dictionary value is changed to True, a code will run that will add to the players stats
    #ex dictionary
        #str_ring: False
        #dex_ring: True

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