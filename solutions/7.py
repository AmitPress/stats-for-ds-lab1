# problem statement: Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
# the list. Do not use any built-in function.

def sum_of_list(lis):
    i = 0
    sum = 0
    for i in lis:
        sum += i
    return sum
if __name__ == '__main__':
    li = list(map(int, input("Enter the integers:\n").split()))
    print(sum_of_list(li))

# test:
# Enter the integers:
# 4 5 6 5 4
# 24