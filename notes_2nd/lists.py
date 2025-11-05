# WM 2nd List notes
y = 0
import random
names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Eric", 5, 3.14, False]

print(names)
print(names[3])
print([random.randint(1,len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names += ["Joseph", "Israel", "Zee"]
names.remove(3.14)
thing = names.index(5)
names.insert(3, "Vienna")
names.pop(thing)
print(names)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

board[1][0] = "X"

print(board)
# List (changable, ordered)
# Tuple (Not changable, ordered)
classes = ("Bard", "Monk", "Barbarian", "Paladin")

# Set (changable, unordered)
fruit = {"Apple", "Orange", "Straberry", "Kiwi"}
print(fruit)