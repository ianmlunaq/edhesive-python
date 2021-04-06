# 7.2.1.py | ian luna | 2020.05.11

info = input('Enter your word or phrase: ')
isDigit = info.isdigit()
flag = 0

if isDigit == False:
    for char in range(len(info)+1):
        for num in range(10):
            infoFind = info.find(str(num), char, char+1)
            if infoFind > -1:
                flag = 1
                print('Contains a ' + str(num))
    if flag == 0:
        print('Does not contain numbers')

elif isDigit == True:
    print('All numbers')
