# WM 2nd Idiot Proof

full_name = input("What is your full name? ").title()
phone_num = str(input("What is your phone number? "))
third = phone_num[3]
seven = phone_num[7]
GPA = float(input("What is your GPA? "))
phone_num = (phone_num.replace(third, "-"))
phone_num = (phone_num.replace(seven, "-"))
print(f"Name: {full_name}\nPhone: {phone_num}\nGPA: {GPA:.1f}")