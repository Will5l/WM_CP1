# WM 2nd Rock Paper Scissors
import random
import time
import sys

def slow_print(text, delay=0.05):
    """Prints text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is immediately displayed
        time.sleep(delay)
    print() # Add a newline at the end
slow_print("We are gonna play rock paper scissors")

while True:
    user = input("Choose rock paper or scissors (q to leave)")
    computer = random.randint(1,3)
    if user == "rock":
        if computer == 1:
            print("Tie")
            print(
    "  ___\n" \
    " /   |\n" \
    " |   /\n" \
    "/    |\n" \
    "|____|\n"
)*2
        elif computer == 2:
            print("You lost")
            print(
    "  ___\n" \
    " /   |\n" \
    " |   /\n" \
    "/    |\n" \
    "|____|\n"
)
            print(
    " __________\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|__________|\n" \
)
        elif computer == 3:
            print("You win")
            print(
    "  ___\n" \
    " /   |\n" \
    " |   /\n" \
    "/    |\n" \
    "|____|\n"
)
            print(
    " __\n"
    "(__)_____\n" \
    " __   ____\n" \
    "(__)/\n"
)

    elif user == "paper":
        if computer == 1:
            print("You win")
            print(
    " __________\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|__________|\n" \
)
            print(
    "  ___\n" \
    " /   |\n" \
    " |   /\n" \
    "/    |\n" \
    "|____|\n"
)
        elif computer == 2:
            print("Tie")
            print(
    " __________\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|__________|\n" \
)*2
        elif computer == 3:
            print("You lost")
            print(
    " __________\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|__________|\n" \
)
            print(
    " __\n"
    "(__)_____\n" \
    " __   ____\n" \
    "(__)/\n"
)
    elif user == "scissor":
        if computer == 1:
            print("You lost")
            print(
    " __\n"
    "(__)_____\n" \
    " __   ____\n" \
    "(__)/\n"
)
            print(
    "  ___\n" \
    " /   |\n" \
    " |   /\n" \
    "/    |\n" \
    "|____|\n"
)  
        elif computer == 2:
            print("You won")
            print(
    " __\n"
    "(__)_____\n" \
    " __   ____\n" \
    "(__)/\n"
)
            print(
    " __________\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|__________|\n" \
)
        elif computer == 3:
            print("Tie")
            print(
    " __\n"
    "(__)_____\n" \
    " __   ____\n" \
    "(__)/\n"
)*2
    elif user == "q":
        break
    else:
        print("Invalid")
print("Session Terminated")