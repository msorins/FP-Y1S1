__author__ = 'sorynsoo'

from phoneStore.phoneManager import *

def printMenu():
    '''
    Prints the app menu
    '''
    msg  = "\n--- MENU ---\n"
    msg += "1. Add phone\n"
    msg += "2. Remove phone\n"
    msg += "3. Change phone price\n"
    msg += "4. List phone\n"

    print(msg)

def getCommand():
    '''
    :return: Gets a user command and returns it
    '''
    cmd = int( input("Command number: ") )
    return cmd

def printOption(lst, cmd):
    '''
    :param lst: the phone list
    :param cmd: user input command
    Calls the appropriate functions
    '''
    if cmd == 1:
        addPhone(lst, input("Manufacturer: "), input("Model: "), input("Price: "))
    if cmd == 2:
        removePhone(lst, input("Manufacturer: "), input("Model: "))
    if cmd == 3:
        changePrice(lst, input("Manufacturer: "), input("Model: "), input("Price: "))
    if cmd == 4:
        print(beautifyPhoneList(sortedPhoneList(lst)))

def beautifyPhoneList(lst):
    '''
    :param lst: the phone list
    :return: a string containing all the phones, but in a more beautiful manner
    '''
    msg = "\nNr | Brand | Model | Price\n"
    for i in range(len(lst)):
        msg = msg + str(i) + ".   " + lst[i][0] + "   " + lst[i][1] + "   " + str(lst[i][2]) + "\n"

    return msg