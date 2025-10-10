# WM 2nd Password Strength Checker

#Set up a list for the special characters, SPECIAL_CHARS
special_chars = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",",",".","<",">","?"]
length = False
upper = False
lower = False
num = False
special = False
#Setup a variable for the rating, starting it at 0
rating = 0
#Ask user for their password input and store it as PASSWORD
password = input("Enter your password to check its strength: ")
#Check length of password, if it is more than 8, add 1 to the rating
if len(password) >= 8:
    rating += 1
    length = True
#Check the password for uppercase, if it has one, add 1 to the rating
for i in password:
    if i.isupper():
        rating += 1
        upper = True
#Check the password for the lowercase, if it has one, add 1 to the rating
for i in password:
    if i.islower():
        rating += 1
        lower = True

#Check the password for numbers, if it has any, add 1 to the string
for i in password:
    if i.isnumeric():
        rating += 1
        num = True

#Check the password with the special character list, if it has one of them, add 1 to the rating
for i in password:
    if i in special_chars:
        rating += 1
        special = True
#Display the rating of the password, and how strong it is, 1-2 points: Weak 3 points: Moderate 4 points: Strong 5 points: Very Strong
if rating == 1 or rating == 2:
    print("Your password is weak")
elif rating == 3:
    print("Your passwords strength is ok, but could be better")
elif rating == 4:
    print("Your password is strong")
elif rating == 5:
    print("Your password is very strong")
#If the password is missing something, display what its missing, and make a suggestion for the corresponding problem.
if rating < 5:
    if length == False:
        print("You should make your password longer")
    if upper == False:
        print("You should add some capitals to your password")
    if lower == False:
        print("You should add some lower case letters to your password")
    if num == False:
        print("You should add a number to your password")
    if special == False:
        print("You should add special characters to your password")

#Make a bar that fills in by fifths based on the strength.