# Wm 2nd For Loop notes
import time

nums = [6,51,61,94,351,946,5489,4,654,684]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num} and is still a large number.")
    else:
        print(num)

print("We completed all the numbers!")
# Default for counting is 1, does not count backwards by default, have to use -1
time.sleep(3)
for x in range(1,10):
    print(x)
time.sleep(3)
print("Count by twos")
for x in range(2,11,2):
    print(x)
time.sleep(3)
print("Count down")
for x in range(10,0,-1):
    print(x)
    time.sleep(1)
thing = "This should be slow."
for i in thing:
    print(i)
    time.sleep(0.1)