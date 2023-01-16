import sys

input = sys.stdin.readline

number = int(input())

wordList = []
for i in range(number):
    word = input()
    if wordList.count(word):
        continue
    wordList.append(word)

wordList.sort(key=lambda x: (len(x), x))

for i in wordList:
    print(i, end="")