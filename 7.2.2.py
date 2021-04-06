# 7.2.2.py | ian luna | 2020.05.11

word = input('Enter your word: ')
number = input('Enter a number: ')
if len(word) < 8:
    print('Not long enough.')
else:
    word = word.replace("e", "@")
    word = word.replace("s", "$")
    word = word.replace("S", "$")
    word = word.replace("t", "+")
    word = word.replace("T", "+")

    word = word.capitalize()

    print(word + str(number))
