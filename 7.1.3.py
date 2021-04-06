# 7.1.3.py | ian luna | 2020.05.08

character = input('Enter a character: ')
if len(character) > 1:
    print('Not a character')
else:
    print('ASCII #' + str(ord(character)))
