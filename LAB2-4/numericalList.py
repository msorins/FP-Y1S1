__author__ = 'sorynsoo'
import re

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

def computeSum(lst, str):
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
        if i1 > len(lst) or i1 < 0 or i2 > len(lst) or i2 < 0 or i1 > i2:
          raise RuntimeError("Your position does not exist")
        del lst[i1:i2]
    else:
        i1 = int(str)
        if i1 >= len(lst) or i1 < 0:
            raise RuntimeError("Your position does not exist")
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

def computeListRealInRange(lst, str):
    '''
    :param lst:  list of complex numbers
    :param str:  str with user input command
    :return: calls a function which prints only the real elements in the index range given
    '''
    str = str[5:]
    print(str)
    str = str.split("to")
    i1 = int(str[0])
    i2 = int(str[1])

    if i1 > len(lst) or i1 < 0 or i2 > len(lst) or i2 < 0 or i1 > i2:
          raise RuntimeError("Your position does not exist")
    newLst = []

    for i in range(i1, i2):
        crt = []
        crt.append(lst[i][0]);
        crt.append(0);
        newLst.append(crt)

    computePrint(newLst)



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
IO PARTS:
'''

commands = [
            {"regex": re.compile(r"^(add)[ ]+\d+[+]\d+[i]$"), "function" : computeSum},
            {"regex": re.compile(r"^add[\s]+\d+[+]\d+i[\s]+at[\s]+[\d]+$"), "function" : computeInsert},
            {"regex": re.compile(r"^remove[\s]+[\d]+$"), "function" : computeRemove},
            {"regex": re.compile(r"^remove[\s]+[\d]+[\s]+to[\s]+[\d]+$"), "function" : computeRemove},
            {"regex": re.compile(r"^replace[\s]+\d+[+]\d+i[\s]with[\s]\d+[+]\d+i$"), "function" : computeReplace},
            {"regex": re.compile(r"^list$"), "function" : computeListAll},
            {"regex": re.compile(r"^list[\s]+real[\s]+[\d]+[\s]+to[\s]+[\d]+$"), "function": computeListRealInRange}

           ]

def computePrint(lst):
    printMSG = ""
    for i in range(len(lst)):
        if(lst[i][1] != 0):
            printMSG = printMSG + str(lst[i][0]) + " + " + str(lst[i][1]) +"i";
        else:
            printMSG = printMSG + str[lst[i][0]]
        if i < len(lst) - 1:
            printMSG = printMSG + ", "

    print(printMSG)

def printMenu():
    '''
    Prints the menu to the user (at program start time)
    '''
    print (""" Commands
    1.Add a complex number: add <number>
    2.Insert a complet number to a position: add <number> at <number>
    3.Remove a complet number from a position: remove <position>
    4.Remove a range of complex number: remove <startPosition> to <endPosition>
    5.Replace a compelx number: replace <oldComplexNumber> with <newComplexNumber>
    6.Exit
    """)


def compute():
    '''
    Main function of the program:
       - calls the printMenu function
       - gets user input and calls parse function
    '''
    lst = []
    printMenu()
    testing(lst)

    inputValue = input("Give an operation: ")
    while(inputValue != "exit"):
        try:
            print(parse(lst, inputValue))
        except RuntimeError as e:
            print(e)

        inputValue = input("Give an operation: ")


compute()


def testing(lst):
    fillValues(lst)

def fillValues(lst):
    lst.append([1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7])