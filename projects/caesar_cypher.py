# WM 2nd caesar cypher

# Ask for encode or decode
# Make a list for capital letter
final_msg = ""
cap = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(cap.index("C"))
lower = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# Make a list for lower case letters
while True:
    choice = input("Would you like to (1)encode or (2)decode? ")
    # Ask for the message, and change display based on previous option. loop till a valid choice is given

    if choice == 1:
        msg = input("What would you like to encode? ")
        shift = input("What would you like to shift by? ")
        if shift.isnumeric():
            w
        else:
            print("Shift isn't a number")
    elif choice == 2:
        msg = input("What would you like to decode? ")
        shift = input("What would you like to shift by? ")
        if shift.isnumeric():
            w
        else:
            print("Shift isn't a number")
    else:
        print("Invalid choice")
# Ask for the integer to encode with
# Make a function for the encoding and one for decoding
def encoding(x):
    for i in x:
        if i in cap:
            y = cap.index(i)
            y = y+shift
            for i in cap:
                if cap.index(i) == y:
                    final_msg = final_msg+i
        elif i in lower():
            y = lower.index(i)
            y = y+shift
            for i in lower:
                if lower.index(i) == y:
                    final_msg = final_msg+i
# Make it ignore numbers spaces and other special chars. Ignore negatives
# Use indexes to shift the letters
# Take the encoded/decoded value, and display it with the respective title