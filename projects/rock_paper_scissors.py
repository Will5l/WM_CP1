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
user_score = 0
computer_score = 0
while True:
    print(f"Score \nUser:{user_score}\nComputer:{computer_score}")
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
)
        elif computer == 2:
            print("You lost")
            computer_score += 1
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
            user_score += 1
            print(
    "  ___\n" \
    " /   |\n" \
    " |   /\n" \
    "/    |\n" \
    "|____|\n"
)
            print("8<")

    elif user == "paper":
        if computer == 1:
            print("You win")
            user_score += 1
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
)
        elif computer == 3:
            print("You lost")
            computer_score += 1
            print(
    " __________\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|          |\n" \
    "|__________|\n" \
)
            print("8<")
    elif user == "scissors":
        if computer == 1:
            print("You lost")
            computer_score += 1
            print("8<")
            print(
    "  ___\n" \
    " /   |\n" \
    " |   /\n" \
    "/    |\n" \
    "|____|\n"
)  
        elif computer == 2:
            print("You won")
            user_score += 1
            print("8<")
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
            print("\n8<")
    elif user == "q":
        break
    else:
        print("Invalid")
print("Session Terminated")