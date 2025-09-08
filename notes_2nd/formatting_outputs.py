# WM 2nd Format Outputs Notes

name = "Jake"
age = 21
grade = .75
money = 25

# this is old, don't use this method. print("Hello {}, nice to meet you! You are {:b}, that is really old! You have a {:%} in this class. You have ${:.2f}, that is a lot of money!".format(name, age, grade, money))

print(f"Hello {name}, nice to meet you! \nYou are {age:b}, that is really old! \nYou have a {grade:%} in this class. \nYou have ${money:.2f}, that is a lot of money!")