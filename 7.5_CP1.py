# 7.4_CP1.py | ian luna | 2020.07.30

#
inFile = open('temperatures.txt', 'r')

line = inFile.readline()
#

sum = 0
numOfNumbers = 0

while line:
    number = float(line)
    # DEBUG: print(number)
    sum += number
    # DEBUG: print('Adding to sum')
    numOfNumbers += 1
    # DEBUG: print('Increasing numOfNumbers by 1')
    line = inFile.readline()

line = inFile.close()
average = sum / numOfNumbers
print(average)
