#Create the player stats as a dictionary with starting values
#Player_stats
#health is 15
    #If it reaches 0 the player loses and gets a gameover
    #If the player puts stat points into it, it'll increase by 5 per
#strength is 1
    #Strength will affect most weapons damage
    #Each point increases it by 1
#dexteriaty is 1
    #Dexteriaty will affect who goes first in combat, and some of the weapons damage, alongside fleeing from combat
    #Increases same as strength
#level is 1
    #Level will increase whenever the player reaches an exp threshold, which will increase by somewhere between 25%-50% per level depending on what works best.
    #Whenever level increases the player will gain a stat point to allocate into one of the 3 stats.
#Gear
    #The player will have a menu which will tell them what they have equipped and the boosts it gives.
    #They will have armor which increases hp and their weapon increases damage, along with a few item slots for things like magic rings and such that increases stats.
#Perks
    #There will be a list of perks the player can choose from. They will get 2
    #Each perk will have either small buffs, or have larger buffs but also debuffs to offset them.
    #There will be two perks which are actually just horrible
    #They will be called the Accursed, and the Despised
    #The Accursed would half your own attack, increase enemy damage by 1.5x, make you extremly unlucky when it comes to drops
    #The Hated would make people less likely to offer you better things, and the things they do offer would be 50% more exspensive. You also recive half the rewards from quests.
    #These will simply exist if someone wants the game to be harder.
    #The rest would be boosts like having a boost to your dex in the initiation of combat or like 10% more damage, cheaper items by like 5% or 10%

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