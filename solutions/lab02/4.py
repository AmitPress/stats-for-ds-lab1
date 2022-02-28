# problem statement: Remove all of the vowels in a string (use string above)

def solution():
    string = "Practice Problems to Drill List Comprehension in Your Head."
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for c in string:
        if not c in vowels:
            result += c
    print(result)
if __name__ == '__main__':
    solution()

# test:
# Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd.