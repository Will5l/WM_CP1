# WM 2nd period Flexible Calculator
global nums
global amount_given
amount_given = 0
global run
#make a variable that will control the loop
run = True
# I will set up a seperate function for all the equations that will use *args so it can take any amount of numbers
def sum(*args):
    total = 0
    add = True
    x = 0
    while x < amount_given:
        num = args[0][x]
        total += num
        x += 1
    return total
    pass
def average(*args):
    avg = 0
    x = 0
    while x < amount_given:
        num = args[0][x]
        avg += num
        x += 1
    avg = avg/amount_given
    return avg
    pass
def min(*args):
    y = 1
    x = args[0][0]
    if x < args[0][y]:
        y += 1
    elif x > args[0][y]:
        x = args[0][y]
        y += 1

    pass
def max():
    pass
def product():
    pass
def again():
    keep_going = input("Do you want to do another calculation? ")
    keep_going = keep_going.lower()
    if keep_going == "yes":
        return True
    elif keep_going == "no":
        return False
while run == True:
    giving_num = True
    nums = []
    operation = int(input("Choose an operation: \n1. Sum\n2. Average\n3. Min\n4. Max\n5. Product\n"))
    while giving_num == True:
        given_num = input("Number:")
        if given_num.isnumeric() == True:
            given_num = int(given_num)
            nums.append(given_num)
            amount_given += 1
        elif given_num == "done":
            giving_num = False
            if operation == 1:
                print(f"The sum of {nums} is {sum(nums)}")
                run = again()
            elif operation == 2:
                print(f"The average of {nums} is {average(nums)}")
                run = again()
            elif operation == 3:
                print(f"The min of {nums} is {min()}")
                run = again()
            elif operation == 4:
                print(f"The max of {nums} is {max()}")
                run = again()
            elif operation == 5:
                print(f"The product of {nums} is {product()}")
                run = again()
        else:
            print("Invalid")

#The code will have to have some conditionals to check which operation was used, and then use the appropriate function.
#The whole thing needs to be in a loop that will break if they say no and continue if they say yes.