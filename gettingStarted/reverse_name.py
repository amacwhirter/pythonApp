name = input("First and last name to reverse -> ")

words = name.split(" ")

for word in words:
    lastindex = len(word) - 1
    for index in range(lastindex, -1, -1):
        print(word[index], end='')
    print(end=' ')
print(end='\n')

name = input('First and last name to reverse -> ')

first, last = name.split()

print(first[::-1], last[::-1])