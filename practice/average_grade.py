# WM 2nd Average Grade
    
comb_grade = 0
amt_of_classes = float(input("How many classes do you have (use numbers): "))
counter = 1
while amt_of_classes >= counter:
    print("wah")
    grade = float(input("What is your percent for the next class?\n"))
    comb_grade = float(grade+comb_grade)

    counter = counter+1
    print(grade)
comb_grade = comb_grade/amt_of_classes
comb_grade = round(comb_grade, 2)
print(comb_grade, "%")