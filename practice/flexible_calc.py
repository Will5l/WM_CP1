# WM 2nd period Flexible Calculator
global nums
#make a variable that will control the loop
run = True
# I will set up a seperate function for all the equations that will use *args so it can take any amount of numbers
def sum(*nums):
    total = 0
    for num in nums:
        total += num
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
    nums = []
    operation = int(input("Choose an operation: \n1. Sum\n2. Average\n3. Min\n4. Max\n5. Product\n"))
    while giving_num == True:
        given_num = input("Number:")
        if given_num.isnumeric() == True:
            given_num = int(given_num)
            nums.append(given_num)
        elif given_num == "done":
            giving_num = False
            if operation == 1:
                print(f"The sum of {nums} is {sum(nums)}")
            elif operation == 2:
                print(f"The average of {nums} is {average(nums)}")
            elif operation == 3:
                print(f"The min of {nums} is {min(nums)}")
            elif operation == 4:
                print(f"The max of {nums} is {max(nums)}")
            elif operation == 5:
                print(f"The product of {nums} is {product(nums)}")
        else:
            print("Invalid")
#The code will have to have some conditionals to check which operation was used, and then use the appropriate function.
#The whole thing needs to be in a loop that will break if they say no and continue if they say yes.