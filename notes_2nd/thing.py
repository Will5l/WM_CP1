num = int(input("Give me a number: "))
num2 = int(input("Give me a number: "))
choice = int(input("Would you like the numbers to be (1)added, or (2) multipled: "))
if choice==1:
    print(num+num2)
elif choice==2:
    print(num*num2)
else:
    print("Invalid option")