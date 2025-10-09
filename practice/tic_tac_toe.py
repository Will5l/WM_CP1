#WM 2nd Pseudo tic tac toe

#import random module

#Display "We're gonna play Tic Tac Toe"

#Game board setup as a 3x3 matrix named BOARD, with each spot being labeled 1-9 from top left to bottom right
#Set SCORE to equal 0

#Main Loop
#While GAME_OVER is False
    #tell player they are X and to go first, 1-9
    #If player enters something invalid, display "Invalid input" and go back to the top.
    #If player tries to go in a filled space display "Space already filled" and go back to top.
    #Replace coresponding part of list with an X if valid.
    #Have computer take its turn with random.randint choosing both indexes, and looping it till it chooses a valid one randomly
    #Display board after both take turns
    #Check if either X or O have a win, by looking at if there is a line vertically, horizotonally or diagonolly, and display corresponding win or lose statment, and then ask if they want to keep playing, if they do restart the loop, otherwise break
    #Check if board blackouts, and display a tie statment, then does the same as above
    #If there is neither a blackout or win, loop back up to continue the game.
    #If they choose to keep going, keep a tally of the score, and increment it by one correspondingly when someone wins.
