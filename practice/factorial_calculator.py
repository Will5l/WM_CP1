#WM 2nd Factorial Calculator
run = True
#Have a function that does the actual calculation
factorial_list = ""
def factorial(num):
    factorial_list = ""
    total = 1
    if num == 0:
        return total
    while num > 0:
        total *= num
        extra_num = str(num)
        factorial_list = factorial_list+extra_num+"x"
        if num == 1:
            factorial_list = factorial_list[:-1]
        num -= 1
    return total, factorial_list

    pass
    #it will take the number given as the factorial, and have a while loop run multiplication for it.
while run == True:
    factorial_num = input("What positive number would you like the factorial of? ")
    if factorial_num.isnumeric() == True:
        factorial_num = int(factorial_num)
        if factorial_num >= 0:
            total, factorial_list = factorial(factorial_num)
            print(f"The factorial of {factorial_num} is written as {factorial_list} and equals {total}")
            thing = input("Would you like to contiune?")
            thing = thing.lower()
            if thing == "no":
                break
            elif thing == "yes":
               factorial_list = ""
               continue 
            pass
        elif factorial_num < 0:
            print("Invalid, number needs to be positive.")
    else:
        print("Invalid, input a number.")
#input for the number inside a while loop, that allows them to use it till they don't want to.