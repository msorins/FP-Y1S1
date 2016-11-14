__author__ = 'sorynsoo'

from phoneStore.phoneManager import *
from phoneStore.UI import *
from phoneStore.tests import *

# Main list in which all the Phones specs are stored
phoneList = []

# Call the test function
testsMain(phoneList)

# Here the magic happens
while True:
    try:
        printMenu()
        printOption(phoneList, getCommand())
    except Exception as e:
        print(e)
