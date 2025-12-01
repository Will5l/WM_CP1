# WM 2nd period Flexible Calculator
#make a variable that will control the loop
run = True
# I will set up a seperate function for all the equations that will use *args so it can take any amount of numbers
def sum(*args):
    total = 0
    for arg in args:
        total += arg
        return total
    pass
def average():
    pass
def min():
    pass
def max():
    pass
def product():
    pass
while run == True:
    giving_num = True
    operation = input("Choose an operation: 1. Sum\n2. Average\n3. Min\n4. Max\n5. Product")
    while giving_num == True:
        nums = []
        given_num = int(input("Number:"))
        if given_num.isnumeric == True:

            nums.append(given_num)
#The code will have to have some conditionals to check which operation was used, and then use the appropriate function.
#The whole thing needs to be in a loop that will break if they say no and continue if they say yes.