__author__ = 'sorynsoo'
import copy
import operator
from NumericalList.utils import *
from NumericalList.ui import *

def parse(lstState, lst, str):
    '''
    :param lstState: the list of states
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
            if crt["returns"] == True:
                lst = crt["function"](lstState, lst, str[len(command):])
            else:
                crt["function"](lst, str[len(command):])

            isOk = True
            break

    if not isOk:
      raise RuntimeError("Invalid command")

    return lst

def computeAdd(lstState, lst, str):
    '''
    :param lstState: the list of states
    :param lst:  list of complex numbers
    :param str:  string with user input command
    :return: the list of complex numbers with the current parsed number appended
    '''
    str = str.lstrip().rstrip()
    lst.append(parseComplexNumber(str))
    addState(lstState,lst)
    return lst

def computeInsert(lstState, lst, str):
    '''
    :param lstState: the list of states
    :param lst:  list of complex numbers
    :param str:  string with user input command
    :return: the list of complex numbers with a new number inserted into specific position
    '''
    str = str.rstrip().lstrip().split("at")
    complexNumber = parseComplexNumber(str[0])
    indexPosition = int(str[1])

    isPositionValid(lst, indexPosition)
    lst.insert(indexPosition, complexNumber)
    addState(lstState,lst)
    return  lst

def computeRemove(lstState, lst, str):
    '''
    :param lstState: the list of states
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

    addState(lstState,lst)
    return lst

def computeReplace(lstState, lst, str):
    '''
    :param lstState: the list of states
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

    addState(lstState,lst)
    return lst

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
        if lst[i][1] == 0:
          newLst.append(lst[i])

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

def computeFilterReal(lstState, lst, str):
    '''
    :param lstState: the list of states
    :param lst: list of complex numbers
    :param str: string with user input command
    :return: the list with only the real numbers remaining
    '''
    newLst = []
    for crt in lst:
        if crt[1] == 0:
            newLst.append(crt)

    lst = copy.deepcopy(newLst)
    addState(lstState,lst)
    return lst

def computeFilterModuloIf(lstState, lst, str):
    '''
    :param lstState: the list of states
    :param lst: list of complex numbers
    :param str: string with user input command
    :return: the list with only the complex number that respect the given conditiion
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

    lst = copy.deepcopy(newLst)
    addState(lstState,lst)
    return lst

def addState(lstState, lst):
    '''
    :param lstState:  the list of states
    :param lst:  the list of complex number
    :return: adds a state to the current lstState
    '''
    newAuxLst = copy.deepcopy(lst)
    lstState.append(newAuxLst)

def restoreState(lstState, lst, str):
    '''
    :param lstState: the list of states
    :param lst: list of complex numbers
    :param str: string with user input command
    :return: the list restored to one state before
    '''
    if len(lstState) >= 2:
        lst = lstState[len(lstState)-2]
        lstState.pop()
    elif len(lstState) == 1:
        lst = []
        lstState.pop()
    else:
        raise RuntimeError("Can't undo anymore")
    return lst

def callPrintMenu(lst, str):
    '''
    :param lst: list of complex numbers
    :param str: string with user input command
    :return: calls the function which prints the list
    '''
    printMenu()

commands = [
            {"regex": re.compile(r"^(add)[ ]+\d+[+]\d+[i]$"), "function" : computeAdd, "returns": True},
            {"regex": re.compile(r"^add[\s]\d+[+]\d+i[\s]at[\s][\d]+$"), "function" : computeInsert, "returns": True},
            {"regex": re.compile(r"^remove[\s][\d]+$"), "function" : computeRemove, "returns": True},
            {"regex": re.compile(r"^remove[\s][\d]+[\s]to[\s][\d]+$"), "function" : computeRemove, "returns": True},
            {"regex": re.compile(r"^replace[\s]\d+[+]\d+i[\s]with[\s]\d+[+]\d+i$"), "function" : computeReplace, "returns": True},
            {"regex": re.compile(r"^list$"), "function" : computeListAll, "returns": False},
            {"regex": re.compile(r"^list[\s]real[\s][\d]+[\s]to[\s][\d]+$"), "function": computeListRealInRange, "returns": False},
            {"regex": re.compile(r"^list[\s]modulo[\s][<>=][\s][\d]+$"), "function": computeListModuloIf, "returns": False},
            {"regex": re.compile(r"^sum[\s][\d]+[\s]to[\s][\d]+$"), "function": computeSumInRange, "returns": False},
            {"regex": re.compile(r"^product[\s][\d]+[\s]to[\s][\d]+$"), "function": computeProductInRange, "returns": False},
            {"regex": re.compile(r"^filter real$"), "function": computeFilterReal, "returns": True},
            {"regex": re.compile(r"^filter[\s]modulo[\s][<>=][\s][\d]+$"), "function": computeFilterModuloIf, "returns": True},
            {"regex": re.compile(r"^undo$"), "function": restoreState, "returns": True},
            {"regex": re.compile(r"^help$"), "function": callPrintMenu, "returns": False}
           ]
