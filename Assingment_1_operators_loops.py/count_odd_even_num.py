from itertools import count


numbers = (5,6,7,8,9,10,11,12,13,14,15)
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even +=1
    else:
        count_odd +=1
print("Number of Even numbers:", count_even)
print("Number of odd numbers:", count_odd)
