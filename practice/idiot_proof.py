# WM 2nd Idiot Proof

full_name = input("What is your full name? ").title()
phone_num = input("What is your phone number? ")
GPA = input("What is your GPA? ")
if phone_num.index[3] == "-" and phone_num.index[7] == "-":
    print(f"Name: {full_name}\nPhone: {phone_num}\nGPA: {GPA:.1}")
elif phone_num.index[3] =="-" and phone_num.index[7] == " ":
    phone_num = phone_num.replace[7, "-"]