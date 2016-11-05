__author__ = 'sorynsoo'

from NumericalList.ui import *
from NumericalList.utils import *
from NumericalList.tests import *

def initFunction():
    '''
    Main function of the program:
       - calls the printMenu function
       - gets user input and calls parse function
    '''
    lst = []
    lstState = []

    #testing(lstState, lst)
    testInit(lstState, lst)
    printMenu()

    inputValue = input("Give an operation: ")
    while(inputValue != "exit"):
        try:
            lst = parse(lstState, lst, inputValue)
        except RuntimeError as e:
            print(e)
        inputValue = input("Give an operation: ")

initFunction()