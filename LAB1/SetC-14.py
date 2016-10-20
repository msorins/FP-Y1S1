__author__ = 'sorynsoo'

'''
Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,... obtained from the
sequence of natural numbers by replacing composed numbers with their prime divisors, each
divisor d being written d times, without memorizing the elements of the sequence.
'''

def isPrime(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False

    return True

def generatePrimeDivisors(number):
    lst = []

    for i in range(2, number):
        if number % i ==0 and isPrime(i):
            lst.append(i)
    return lst

def computeSequence(nth):
    crtNumber = 0
    counter = 0

    while counter < nth:
        crtNumber = crtNumber + 1
        crtLst = generatePrimeDivisors(crtNumber)

        if len(crtLst) == 0:
            counter += 1
        else:
            for i in crtLst:
                counter += i
                if counter >= nth:
                    return i

    return crtNumber



inputNth = int(input("Give the n-th value: "));
print("N-th element is: ", computeSequence(inputNth))