__author__ = 'sorynsoo'
import math
import re

def parseComplexNumber(str):
    '''
    :param str: string containing a complex number in a specific (validated already) format
    :return: the complex number in a list
    '''
    str = str.rstrip().lstrip()
    str = str.split('+')

    realPart = str[0]
    imaginaryPart = str[1][:-1]

    res = []
    res.append(int(realPart))
    res.append(int(imaginaryPart))
    return res

def isPositionValid(lst, poz):
    '''
    :param lst:  the list of complex numbers
    :param poz:  chosen position
    :exception if chosen position does not exist
    '''
    if poz > len(lst) or poz < 0:
          raise RuntimeError("Your position does not exist")

def moduloOfComplexNumber(complexNumber):
    '''
    :param number: a list with 2 elements, first is the real part, the second is the imaginary part
    :return: the modulo of that element
    '''
    return math.sqrt(complexNumber[0] * complexNumber[0] + complexNumber[1] * complexNumber[1])
