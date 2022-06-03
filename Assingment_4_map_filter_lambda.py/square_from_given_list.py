from tkinter import N


def square_num(n):
    return n*n 
nums = [3,6,7,8]
print("Original list:", nums)
result = map(square_num, nums)
print("Square the elements of the given list using map():")
print(list(result))
