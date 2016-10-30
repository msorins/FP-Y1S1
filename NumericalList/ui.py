__author__ = 'sorynsoo'

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
    1.  add <complexNumber>
    2.  add <complexNumber> at <complexNumber>
    3.  remove <position>
    4   remove <startPosition> to <endPosition>
    5.  replace <oldComplexNumber> with <newComplexNumber>
    6.  list
    7.  list real <startPosition> to <endPosition>
    8.  list modulo < | > | = <number>
    9.  sum <startPosition> to <endPosition>
    10. product <startPosition> to <endPosition>
    11. filter real
    12. filter modulo < | > = <number>
    13. undo
    14. help
    15. exit
    """)
