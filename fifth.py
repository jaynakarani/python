# There are many exceptions in python but we will have few of them

# 1st ZeroDivision Error
# This error occurs when we try dividing a number with zero

# try:
#     division = 100/0
#     print(division)
# except ArithmeticError:
#     division = 100/10
#     print(division)

# 2nd Index Error
# This error occurs when index value is out of range

# try:
#     arr = [1,2,3]
#     print(arr[3])
# except IndexError:
#     print("Index out of bound")

# 3rd TypeError
# This type of error occur when we type in something wrong or forgot something to type

# def func(name,roll):
#     print(name ,roll)
#
# try:
#     func("Bhavya")
# except TypeError:
#     func("Bhavya",79)

# 4th KeyError
# This error occurs when there is no key present in the given dictionary

# dictionary = {"a":1,"b":2,"c":3}
#
# try:
#     print(dictionary["d"])
# except KeyError:
#     print("Key doesn't exist in dictionary")

# 5th ValueError
# This occurs when we try accessing a string value as an integer or anyother similar like that

# try:
#     print(int('a'))
# except ValueError:
#     print("Value doesn't exist")
