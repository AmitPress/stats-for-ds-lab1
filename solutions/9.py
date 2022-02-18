# problem statement: Given a list of numbers (hardcoded in the program), write a Python program to find the largest and
# smallest element of the list. Define two functions largest_number_<your-student-id> and
# smallest_number_<your-student-id> in your program. Do not use any built-in function.

def largest_number_2019_1_60_136(lis):
    large = -9999
    for n in lis:
        if n>large:
            large = n
    return large

def smallest_number_2019_1_60_136(lis):
    smallest = 9999
    for n in lis:
        if n<smallest:
            smallest = n
    return smallest
if __name__ == '__main__':
    li = [41, -52, 77, 63, -34, 17, 42, 23]
    print(f"The largest number and smallest number present in the list are {largest_number_2019_1_60_136(li)} and {smallest_number_2019_1_60_136(li)} respectively")

# test:
# The largest number and smallest number present in the list are 77 and -52 respectively