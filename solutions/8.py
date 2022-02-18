# problem statement: Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
# the even-indexed elements in the list.

def sum_of_even_indexed_numbers(lis):
    sum = 0
    for i, n in enumerate(lis):
        if i % 2 == 0:
            sum += n
    return sum
if __name__ == '__main__':
    lis = list(map(int, input("Enter the integers:\n").split()))
    # n = int(input(""))
    print(f"The sum of the list is {sum_of_even_indexed_numbers(lis)}")