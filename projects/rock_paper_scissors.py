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
    user = input(slow_print("Choose rock paper or scissors"))
    computer = random.randint(1,3)
    if user == "rock":
        if computer == 1:
            print("Tie")
            print(
    "  ___" \
    " /   |" \
    " |   /" \
    "/    |" \
    "|____|"
)*2

    elif user == "paper":
        if computer == 1:

    elif user == "scissor":
        if

print(
    "  ___" \
    " /   |" \
    " |   /" \
    "/    |" \
    "|____|"
)
print(
    " __"
    "(__)" \
    " __   ____" \
    "(__)/"
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