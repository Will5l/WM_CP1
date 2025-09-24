# WM 2nd Letter Grade
grade = 1
while grade != 0:
    grade = float(input("Give me your grade percentage and I'll give you your letter grade. Type 0 if you want to end."))
    if grade >= 94:
        print(f"You have {grade:.2f}%, an A")
    elif grade >= 90:
        print(f"You have {grade:.2f}%, an A-")
    elif grade >= 87:
        print(f"You have {grade:.2f}%, a B+")
    elif grade >= 83:
        print(f"You have {grade:.2f}%, a B")
    elif grade >= 80:
        print(f"You have {grade:.2f}%, a B-")
    elif grade >= 77:
        print(f"You have {grade:.2f}%, a C+")
    elif grade >= 74:
        print(f"You have {grade:.2f}%, a C")
    elif grade >= 70:
        print(f"You have {grade:.2f}%, a C-")
    elif grade >= 67:
        print(f"You have {grade:.2f}%, a D+")
    elif grade >= 63:
        print(f"You have {grade:.2f}%, a D")
    elif grade >= 60:
        print(f"You have {grade:.2f}%, a D-")
    elif grade > 0:
        print(f"You have {grade:.2f}%, a F")
    else:
        print("Something went wrong, invalid.")