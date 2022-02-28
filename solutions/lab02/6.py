# problem statement: Use a dictionary comprehension to count the length of each word in a sentence (use string above)

def solution():
    string = "Practice Problems to Drill List Comprehension in Your Head."
    words = string.split(" ")
    word_count = dict.fromkeys(words, 0)
    
    for word in words:
        word_count[word] = len(word)

    for k,v in word_count.items():
        print(f"\"{k}\"s length is {v}")
if __name__ == '__main__':
    solution()

# test:
# "Practice"s length is 8
# "Problems"s length is 8
# "to"s length is 2
# "Drill"s length is 5
# "List"s length is 4
# "Comprehension"s length is 13
# "in"s length is 2
# "Your"s length is 4
# "Head."s length is 5
