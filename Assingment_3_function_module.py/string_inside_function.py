def reverse(s):
    str = " "
    for i in s:
        str = i + str
    return str

s = "5 AVENGERS with 10 villens"
print("The Original string is:",end = " ",)
print(s)
print("The reversed string is:",end=" ")
print(reverse(s))