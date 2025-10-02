# WM 2nd Multiplication table

thing = 0
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
table = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],]
for num in nums:
    table[thing].insert(0, num*1)
    table[thing].insert(1, num*2)
    table[thing].insert(2, num*3)
    table[thing].insert(3, num*4)
    table[thing].insert(4, num*5)
    table[thing].insert(5, num*6)
    table[thing].insert(6, num*7)
    table[thing].insert(7, num*8)
    table[thing].insert(8, num*9)
    table[thing].insert(9, num*10)
    table[thing].insert(10, num*11)
    table[thing].insert(11, num*12)
    thing += 1
for row in table:
    print(row)