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

#make a function for normal combat
    #All combat will be 1v1 and start with checking if the players or enemies dex is higher.
    #Whoever has the higher dex will go first in the combat.
    #When the player takes a turn they will be given options, 1. Attack, 2. Heavy Attack, 3. Potions, 4. Flee
    #If they attack, the function will check the stat mod for the weapon, and then add that to the weapons damage before applying it to the enemies health and decreasing it.
    #If they choose to use heavy attack, then it calculate the damage same as the attack, before doubling it, but there is also a 40% chance it misses and you lose your turn.
    #If they choose to use potions, it will open their bag, and list all their potions with numbers and the amount of them, with the boost they give. There will also be an additional option to shut the bag after opening it and going back to your options.
    #If they choose to flee, then a value will be retreived from a dictionary that represents the escape chance as a percent for each type of monster. Dex is then doubled and added to it. If it equals or exceeds 100% then they will guaranteed escape. otherwise then waste the turn trying to escape 