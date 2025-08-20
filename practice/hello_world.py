# WM 2nd Hello world

admin = "Will"
admin_two = "Ms. LaRose"
user_one = "Carl"
user_two = "Adam"
user_three = "Kaitlin"
user_four = "Abigal"
user_five = "Kent"
name = input("What's your name?: ")
if name == admin or name == admin_two:
    print("Welcome back admin")
elif name==user_one:
    print("Glad to see you again Carl")
elif name==user_two:
    print("Glad to see you again Adam")
elif name==user_three:
    print("Glad to see you again Kaitlin")
elif name==user_four:
    print("Glad to see you again Abigal")
elif name==user_five:
    print("Glad to see you again Kent")
else:
    print("Hello", name)