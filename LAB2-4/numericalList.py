__author__ = 'sorynsoo'
import re
import math
import operator

def parse(lst, str):
    '''
    :param lst: list of complex numbers
    :param str: string with current user input command ready to be parsed
    :return: the list with complex numbers
    :exception: command empty or invalid (if it is not matched with any regex)
    '''
    if not str:
        raise RuntimeError("Empty input, please write a valid command")
    command = str.split()[0]

    isOk = False
    for crt in commands:
        if crt["regex"].match(str):
          crt["function"](lst, str[len(command):])
          isOk = True
          break

    if not isOk:
      raise RuntimeError("Invalid command")

    return lst

def computeAdd(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  string with user input command
    :return: the list of complex numbers with the current parsed number appended
    '''
    str = str.lstrip().rstrip()
    lst.append(parseComplexNumber(str))

def computeInsert(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  string with user input command
    :return: the list of complex numbers with a new number inserted into specific position
    '''
    str = str.rstrip().lstrip().split("at")
    complexNumber = parseComplexNumber(str[0])
    indexPosition = int(str[1])

    isPositionValid(lst, indexPosition)
    lst.insert(indexPosition, complexNumber)

def computeRemove(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  string with user input command
    :return: the list of complex numbers with an element from a specific position removed
    '''
    str = str.rstrip().lstrip()
    if "to" in str:
        str = str.split("to")
        i1 = int(str[0])
        i2 = int(str[1])
        isPositionValid(lst, i1)
        isPositionValid(lst, i2)
        del lst[i1:i2]
    else:
        i1 = int(str)
        isPositionValid(lst, i1)
        del lst[i1]

def computeReplace(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  string with user input command
    :return: the list of complex numbers with a specific element replaced
    '''
    str = str.rstrip().lstrip().split("with")

    firstNumber = parseComplexNumber(str[0])
    secondNumber = parseComplexNumber(str[1])

    if firstNumber in lst:
        lst[lst.index(firstNumber)] = secondNumber
    else:
        raise RuntimeError("Number is not in the list")

def computeListAll(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  str with user input command
    :function: calls a function which prints all the elements of the list
    '''
    computePrint(lst);
    return lst

def computeListRealInRange(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  str with user input command
    :return: calls a function which prints only the real elements in the index range given
    '''
    str = str[5:]
    str = str.split("to")
    i1 = int(str[0])
    i2 = int(str[1])

    isPositionValid(lst, i1)
    isPositionValid(lst, i2)

    newLst = []
    for i in range(i1, i2):
        crt = []
        crt.append(lst[i][0]);
        crt.append(0);
        newLst.append(crt)

    computePrint(newLst)
    return newLst

def computeListModuloIf(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  string with user input command
    :return: calls a function which prints only the Modulo elements that respect a propriety
    '''
    validCondition = {"<" : operator.lt, ">" : operator.gt, "=" : operator.eq}
    str = str[7:]
    str = str.split()

    op = str[0]
    number = int(str[1])

    newLst = []
    for crt in lst:
        if validCondition[op](int(moduloOfComplexNumber(crt)), number) == True:
            newLst.append(crt)

    computePrint(newLst)
    return newLst


def computeSumInRange(lst, str):
    '''
    :param lst: list of complex numbers
    :param str: string with user input command
    :return: prints the sum of complex numbers in a range
    '''
    str = str.split("to")
    i1 = int(str[0])
    i2 = int(str[1])

    isPositionValid(lst, i1)
    isPositionValid(lst, i2)

    realPart = 0
    imaginaryPart = 0

    for i in range(i1, i2):
        realPart = realPart + lst[i][0]
        imaginaryPart = imaginaryPart + lst[i][1]

    printComplexNumber([realPart, imaginaryPart])
    return [realPart, imaginaryPart]

def computeProductInRange(lst, str):
    '''
    :param lst: list of complex numbers
    :param str: string with user input command
    :return: prints the product of complex numbers in a range
    '''
    str = str.split("to")
    i1 = int(str[0])
    i2 = int(str[1])

    isPositionValid(lst, i1)
    isPositionValid(lst, i2)

    realPart = 1
    imaginaryPart = 1

    for i in range(i1, i2):
        realPart = realPart * lst[i][0]
        imaginaryPart = imaginaryPart * lst[i][1]

    printComplexNumber([realPart, imaginaryPart])

    return [realPart, imaginaryPart]

def isPositionValid(lst, poz):
    if poz > len(lst) or poz < 0:
          raise RuntimeError("Your position does not exist")

def moduloOfComplexNumber(complexNumber):
    '''
    :param number: a list with 2 elements, first is the real part, the second is the imaginary part
    :return: the modulo of that element
    '''
    return math.sqrt(complexNumber[0] * complexNumber[0] + complexNumber[1] * complexNumber[1])

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

'''
IO PART:
'''

commands = [
            {"regex": re.compile(r"^(add)[ ]+\d+[+]\d+[i]$"), "function" : computeAdd},
            {"regex": re.compile(r"^add[\s]\d+[+]\d+i[\s]at[\s][\d]+$"), "function" : computeInsert},
            {"regex": re.compile(r"^remove[\s][\d]+$"), "function" : computeRemove},
            {"regex": re.compile(r"^remove[\s][\d]+[\s]to[\s][\d]+$"), "function" : computeRemove},
            {"regex": re.compile(r"^replace[\s]\d+[+]\d+i[\s]with[\s]\d+[+]\d+i$"), "function" : computeReplace},
            {"regex": re.compile(r"^list$"), "function" : computeListAll},
            {"regex": re.compile(r"^list[\s]real[\s][\d]+[\s]to[\s][\d]+$"), "function": computeListRealInRange},
            {"regex": re.compile(r"^list[\s]modulo[\s][<>=][\s][\d]+$"), "function": computeListModuloIf},
            {"regex": re.compile(r"^sum[\s][\d]+[\s]to[\s][\d]+$"), "function": computeSumInRange},
            {"regex": re.compile(r"^product[\s][\d]+[\s]to[\s][\d]+$"), "function": computeProductInRange}
           ]

def printComplexNumber(number):
    print(str(number[0]) + " + " + str(number[1]) + "i")

def computePrint(lst):
    printMSG = ""
    for i in range(len(lst)):
        if(lst[i][1] != 0):
            printMSG = printMSG + str(lst[i][0]) + " + " + str(lst[i][1]) +"i";
        else:
            printMSG = printMSG + str(lst[i][0])
        if i < len(lst) - 1:
            printMSG = printMSG + ", "

    print(printMSG)

def printMenu():
    '''
    Prints the menu to the user (at program start time)
    '''
    print (""" Commands
    1.  add <number>
    2.  add <number> at <number>
    3.  remove <position>
    4   remove <startPosition> to <endPosition>
    5.  replace <oldComplexNumber> with <newComplexNumber>
    6.  list
    7.  list real <startPosition> to <endPosition>
    8.  list modulo < | > | = <number>
    9.  sum <startPosition> to <endPosition>
    10. product <startPosition> to <endPosition>
    11. Exit
    """)

'''
TESTING PART:
'''

def testing(lst):
    testInit(lst)
    testAdd(lst)
    testInsert(lst)
    testRemove(lst)
    testRemoveRange(lst)
    testReplace(lst)
    testList(lst)
    testListRealInRange(lst)
    testListModuloIf(lst)
    testSumInRange(lst)
    testProductInRange(lst)

def testInit(lst):
    lst.append([1,1])
    lst.append([2,2])
    lst.append([3,3])
    lst.append([4,4])
    lst.append([5,5])
    lst.append([6,6])
    lst.append([7,7])

def testAdd(lst):
    parse(lst, "add 8+8i")
    assert [8,8] in lst
    parse(lst, "add 9+9i")
    assert [9,9] in lst
    parse(lst, "add 10+10i")
    assert [10,10] in lst
    parse(lst, "add 10+10i")
    assert lst.count([10,10]) == 2
    parse(lst, "add 1+1i")
    assert lst.count([1,1]) == 2

def testInsert(lst):
    parse(lst, "add 0+1i at 0")
    assert lst.index([0,1]) == 0
    parse(lst, "add 99+99i at 11")
    assert lst.index([99,99]) == 11
    parse(lst, "add 999+999i at 11")
    assert lst.index([999,999]) == 11

    try:
        parse(lst, "add 1-1i at 1")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "add 1+1j a 1")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "add 1+1i at 13312")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testRemove(lst):
    parse(lst, "remove 10")
    assert(lst.count([10,10]) == 1)

    parse(lst, "remove 12")
    assert([10,10] not in lst)

    try:
        parse(lst, "remove -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "remove -15")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "remove 20")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

    try:
        parse(lst, "remove 30")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testRemoveRange(lst):
    parse(lst, "remove 10 to 13")
    assert [999,999] not in lst
    assert [99,99] not in lst
    assert lst.count([1,1]) == 1
    parse(lst, "remove 0 to 1")
    assert [0,1] not in lst

    try:
        parse(lst, "remove 0 to -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "remove 5 to 17")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testReplace(lst):
    parse(lst, "list")
    parse(lst, "replace 9+9i with 10+10i")
    assert [9,9] not in lst and [10,10] in lst

    parse(lst, "replace 10+10i with 9+9i")
    assert [9,9] in lst and [10,10] not in lst

    parse(lst, "replace 1+1i with 99+99i")
    assert [1,1] not in lst and [99,99]  in lst

    try:
        parse(lst, "replace 1+1i with 3-3i")
    except RuntimeError as e:
        assert str(e) == "Invalid command"
    try:
        parse(lst, "replace 1+1i with 4i")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "replace 1+1i with 96+12i")
    except RuntimeError as e:
        assert str(e) == "Number is not in the list"

def testList(lst):
    assert computeListAll(lst, "") == lst
    parse(lst, "add 17+17i")
    assert computeListAll(lst, "") == lst

def testListRealInRange(lst):
    assert computeListRealInRange(lst, "real 1 to 3") == [[2,0],[3,0]]
    assert computeListRealInRange(lst, "real 1 to 4") == [[2,0],[3,0],[4,0]]
    assert computeListRealInRange(lst, "real 1 to 5") == [[2,0],[3,0],[4,0],[5,0]]

    try:
        parse(lst, "list real 1 to -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "list real 5 to 5000")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testListModuloIf(lst):
    assert computeListModuloIf(lst, "modulo = 2") == [[2,2]]
    assert computeListModuloIf(lst, "modulo > 20") == [[99,99], [17,17]]
    assert computeListModuloIf(lst, "modulo < 5") == [[2,2], [3,3]]

    try:
        parse(lst, "modulo | 3")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lst, "modulo < -3")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

def testSumInRange(lst):
    assert computeSumInRange(lst, "1 to 3") == [5,5]
    assert computeSumInRange(lst, "0 to 3") == [104,104]
    assert computeSumInRange(lst, "2 to 8") == [33,33]

    try:
        parse(lst, "sum 1 to -5")
    except RuntimeError as e:
        print(e)
        assert str(e) == "Invalid command"

    try:
        computeSumInRange(lst, "1 to -5")
    except RuntimeError as e:
        print(e)
        assert str(e) == "Your position does not exist"

    try:
        computeSumInRange(lst, "5 to 500")
    except RuntimeError as e:
        print(e)
        assert str(e) == "Your position does not exist"

def testProductInRange(lst):
    assert computeProductInRange(lst, "1 to 3") == [6,6]
    assert computeProductInRange(lst, "0 to 3") == [594,594]
    assert computeProductInRange(lst, "2 to 8") == [20160,20160]

    try:
        parse(lst, "product 1 to -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        computeProductInRange(lst, "1 to -5")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

    try:
        computeProductInRange(lst, "5 to 500")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def compute():
    '''
    Main function of the program:
       - calls the printMenu function
       - gets user input and calls parse function
    '''
    lst = []
    printMenu()
    #testing(lst)

    inputValue = input("Give an operation: ")
    while(inputValue != "exit"):
        try:
            parse(lst, inputValue)
        except RuntimeError as e:
            print(e)

        inputValue = input("Give an operation: ")


compute()
