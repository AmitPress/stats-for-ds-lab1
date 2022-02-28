# problem statement: Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
# the even-indexed elements in the list.

def sum_of_even_indexed_numbers(lis):
    sum = 0
    for i, n in enumerate(lis):
        if i % 2 == 0:
            sum += n
    return sum
if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5] # considering 0 is even , the even indices value are 1, 3, 5
    # n = int(input(""))
    print(f"The sum of the list is {sum_of_even_indexed_numbers(lis)}")

# test:
# The sum of the list is 9