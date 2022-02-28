# problem statement: Count the number of spaces in a string (use string above)

def solution():
    string = "Practice Problems to Drill List Comprehension in Your Head."
    count = 0
    for c in string:
        if c == ' ':
            count += 1
    print(count)
if __name__ == '__main__':
    solution()

# test:
# 8