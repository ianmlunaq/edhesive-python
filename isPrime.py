import math

checkPrime = int(input('Input a number: '))
isPrime = True

print('')

endOfLoop = int(math.sqrt(checkPrime)) + 1
#endOfLoop = math.sqrt(checkPrime)

print(endOfLoop - 1)

a = input('Continue')

for i in range(2, endOfLoop):
    print(i)
    if checkPrime % i == 0:
        #print(i)
        isPrime = False

print(isPrime)
