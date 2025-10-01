# WM 2nd Multiplication table

thing = 0
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
table = [
    [],
    [],
    []
]
for num in nums:
    table[thing][0] = (num*1)
    table[thing][1] = (num*2)
    table[thing][1] = (num*3)
    table[thing][1] = (num*4)
    table[thing][1] = (num*5)
    table[thing][1] = (num*6)
    table[thing][1] = (num*7)
    table[thing][1] = (num*8)
    table[thing][1] = (num*9)
    table[thing][1] = (num*10)
    table[thing][1] = (num*11)
    table[thing][1] = (num*12)
    thing += 1
print(table)
