#WM 2nd Square Numbers

numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

squared = list(map(lambda num: num*num, numbers))

for i, x in zip(numbers, squared):
    print(f"Number: {i} Squared: {x}")