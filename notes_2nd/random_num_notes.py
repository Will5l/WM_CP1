# WM 2nd Random Numbers Notes
import random

print(random.random()) # Float between 0 and 1

print(random.randint(1,100))


name =input("What is your name: \n").strip().title()

# Stat Gen
stat_one = random.randint(1,10)+random.randint(1,10)
stat_two = random.randint(1,10)+random.randint(1,10)
stat_three = random.randint(1,10)+random.randint(1,10)
stat_four = random.randint(1,10)+random.randint(1,10)
stat_five = random.randint(1,10)+random.randint(1,10)
stat_six = random.randint(1,10)+random.randint(1,10)
stat_seven = random.randint(1,10)+random.randint(1,10)

print(f"Your stat option are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

strength = int(input("Which stat are you making strength?"))