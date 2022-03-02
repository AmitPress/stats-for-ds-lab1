# problem statement: For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single
# digit any of the numbers is divisible by 5

def solution():
    li = [j for j in [i for i in range(1, 1001)] if j % 5 == 0]
    # print(li)
    large = -999
    for n in li:
        digits = [int(x) for x in str(n)]
        large = max(large, max(digits))
    print(f"Highest single digit present in a number that is divisible by 5 is {large}")
if __name__ == '__main__':
    # x1, y1 = list(map(int, input("Enter the integers:\n").split()))
    # n = int(input(""))
    solution()

# test:
# Highest single digit present in a number that is divisible by 5 is 9