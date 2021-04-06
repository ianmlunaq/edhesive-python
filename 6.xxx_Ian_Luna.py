# 6.xxx_Ian_Luna.py | ian luna | 2020.05.06 | First 100 prime numbers

import math
prime = 0

def isPrime(number):
    global prime
    prime = number
    endOfLoop = int(math.sqrt(number)) + 1
    for i in range (2 , endOfLoop):
        if number % i == 0:
            prime = 0
            break

    return prime

def main():
    totalPrimes = 0
    primeSum = 0
    theNumber = 2

    while(totalPrimes < 100):
        checkPrime = isPrime(theNumber)
        theNumber += 1
        primeSum += checkPrime
        if checkPrime > 0:
            print(checkPrime)
            totalPrimes += 1

    print('')
    print('Total number of prime numbers in this list: ' + str(totalPrimes))
    print('Sum of all the prime numbers in this list: ' + str(primeSum))

if __name__ == "__main__":
    main()

'''
theNumber is run through the isPrime() function where prime is made equal to
number. It then takes the square root of number, type casts it into an int, and
is set as endOfLoop. I also add one to endOfLoop so as to make the for loop
include the square root as a number to check.

Inside the for loop, is an if statement. The if statement checks if number, when
divided by i leaves a remainder. If at any point number is divided by i and
leaves no remainder, prime is made equal to 0 and the loop is broken. If number
is not able to be divided evenly into any number, prime is returned, prime
already being equal to theNumber.

Back in the main() function theNumber is increased by one, checkPrime is added
to primeSum. An if statement then checks if checkPrime is greater than 0. If it
is, totalPrimes is increased by one. After the while() loop is complete,
totalPrimes and primeSum are outputted.
'''
