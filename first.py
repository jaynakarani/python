from collections import Counter

string = input()

count = Counter(string)

for letter,value in count.items():
    print(letter,value)
