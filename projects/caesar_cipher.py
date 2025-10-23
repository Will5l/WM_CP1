# WM 2nd caesar cypher
final_msg = ""
# Ask for encode or decode
def overrun(z):
    if z >= 26:
        return (z-26)
    else:
        return z
def encoding(x):
    global final_msg
    for i in x:
        if i in cap:
            y = cap.index(i)
            y = y+shift
            y = overrun(y)
            for i in cap:
                if cap.index(i) == y:
                    final_msg = final_msg + i
        elif i in lower:
            y = lower.index(i)
            y = y+shift
            y = overrun(y)
            for i in lower:
                if lower.index(i) == y:
                    final_msg = final_msg + i
def decoding(x):
    global final_msg
    for i in x:
        if i in cap:
            y = cap.index(i)
            y = y+shift
            y = overrun(y)
            for i in cap:
                if cap.index(i) == y:
                    final_msg = final_msg+i
        elif i in lower():
            y = lower.index(i)
            y = y+shift
            y = overrun(y)
            for i in lower:
                if lower.index(i) == y:
                    final_msg = final_msg+i
        else:
            final_msg = final_msg+i
# Make a list for capital letter
cap = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# Make a list for lower case letters
while True:
    choice = input("Would you like to (1)encode or (2)decode? ")
    # Ask for the message, and change display based on previous option. loop till a valid choice is given

    if choice == "1":
        msg = input("What would you like to encode? ")
        shift = int(input("What would you like to shift by? "))
        encoding(msg)
        print(f"Encoded:{final_msg}")
        break
    elif choice == "2":
        msg = input("What would you like to decode? ")
        shift = int(input("What would you like to shift by? "))
        decoding(msg)
        print(f"Decoded:{final_msg}")
        break
    else:
        print("Invalid choice")
# Ask for the integer to encode with
# Make a function for the encoding and one for decoding

# Make it ignore numbers spaces and other special chars. Ignore negatives
# Use indexes to shift the letters
# Take the encoded/decoded value, and display it with the respective title