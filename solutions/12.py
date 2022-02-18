# problem statement: Given a string and an integer number n, remove characters from a string starting from zero up to n
# and return a new string. N must be less than the length of the string. Read inputs from the user. Do
# not use any built-in function.

def solution(n,s):
    sz = len(s)
    new_string = ""
    for i, c in enumerate(s):
        if not i<=n:
            new_string += c
    return new_string
if __name__ == '__main__':
    n = int(input("Enter the number:\n"))
    s = input("Enter the string:\n")
    sz = len(s)
    if n>sz:
        print("N is larger than the size of the string")
    else:
        print(f"The new string is: {solution(n,s)}") if not solution(n,s) == '' else print("All charecters removed")

# test:
# Enter the number:
# 5
# Enter the string:
# IAMTIRED
# The new string is: ED
        