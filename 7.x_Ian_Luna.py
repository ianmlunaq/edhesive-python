# 7.x.py | ian luna | 2020.04.21 | chr ord

characterList = []
numberList = []

for x in range(3):
    prompt = input("Enter a number: ")
    character = chr(int(prompt))
    characterList.append(character)

print()

for x in range(3):
    prompt = input("Enter ONE character: ")
    number = ord(prompt)
    numberList.append(number)

print()

print(characterList, 'length is', len(characterList))
print(numberList, 'length is', len(numberList))

"""
The first for() loop takes 3 numbers, uses chr() to convert it into a character, then appends it to characterList.
The second for() loop takes 3 characters, uses ord() to convert it into an integer, then appends it to numberList.
At the end I use len() to output the length of each list.
"""
