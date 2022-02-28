# problem statement: Find all of the words in a string that are less than 5 letters (use string above)

def solution():
    string = "Practice Problems to Drill List Comprehension in Your Head."
    words = string.split(" ")
    
    for word in words:
        if len(word)<5:
            print(word, end=" ")
if __name__ == '__main__':
    solution()

# test:
# to List in Your