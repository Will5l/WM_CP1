# WM 2nd User Sign in
username_input = input("Enter Username(case sensitive): ")
password_input = input("Enter Password(case sensitive): ")
username = "OneRing"
password = "RuleThemAll"
if username_input == username:
    if password_input == password:
        print(f"Welcome, {username_input}")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")