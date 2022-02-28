# problem statement: Given a list of numbers (hardcoded in the program), write a Python program to find the second
# largest element of the list.

def second_largest(lis):
    max = -9999
    smax = -9999
    for i in lis:
        if max < i:
            max = i
    for i in lis:
        if not i == max:
            if i>smax:
                smax = i
    return smax
if __name__ == '__main__':
    li = [41, -52, 77, 63, -34, 17, 42, 23]
    print(f"The second largest number is in the list: {second_largest(li)}")

# test:
# The second largest number is in the list: 63