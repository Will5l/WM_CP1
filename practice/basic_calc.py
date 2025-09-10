# WM 2nd Basic Calculator

# Number Inputs
num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))
equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison"))
# The loop
while equation_type <= 8:
    # Addition
    if equation_type == 1:
        additon_product = (num1+num2)
        print(f"{num1}+{num2}={additon_product}")
        equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison\n8. To end"))
    # Subtraction
    elif equation_type == 2:
        subtraction_product = (num1-num2)
        print(f"{num1}-{num2}={subtraction_product}")
        equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison\n8. To end"))
    # Int Div
    elif equation_type == 3:
        intger_div_product = (num1/num2)
        print(f"{num1}/{num2}={intger_div_product}")
        equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison\n8. To end"))
    # Multiplication
    elif equation_type == 4:
        multiplication_product = (num1*num2)
        print(f"{num1}*{num2}={multiplication_product}")
        equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison\n8. To end"))
    # Exponent
    elif equation_type == 5:
        exponent_product = (num1**num2)
        print(f"{num1}**{num2}={exponent_product}")
        equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison\n8. To end"))
    # Mod Div
    elif equation_type == 6:
        mod_product = (num1%num2)
        print(f"{num1}%{num2}={mod_product}")
        equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison\n8. To end"))
    # Floor Div
    elif equation_type == 7:
        floor_div_product = (num1//num2)
        print(f"{num1}//{num2}={floor_div_product}")
        equation_type = int(input("Choose an number for the arithmetic method.\n1. additon\n2. subtraction\n3. intger divison\n4. multiplication\n5. expontent \n6. modular divison\n7. floor divison\n8. To end"))