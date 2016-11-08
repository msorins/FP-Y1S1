__author__ = 'sorynsoo'

import re

class Utils:
    def __init__(self):
        pass

    def nonEmptyAndMoreThanThree(self, str):
        if not str:
            raise RuntimeError("Invalid input, empty input")
        if len(str) < 3:
            raise RuntimeError("Invalid input, it has to contain more than 3 letters")

    def validateCommandNumber(self, menu, command):
        rgx = re.compile(r"^[\d]+$")
        if not rgx.match(command):
            raise RuntimeError("Wrong command")
        if ( int(command) > len(menu) and int(command) !=9 ) or  int(command) < 0:
            raise RuntimeError("Invalid number")

    def validateDateFormat(self, date):
        if type(date) != str:
            return
        rgx = re.compile(r"^[\d]?[\d].[\d]?[\d].[\d][\d][\d][\d]$")
        if not rgx.match(date):
            raise RuntimeError("Wrong date format")

    def findPartial(self, string1, string2):
        string1 = string1.lower()
        string2 = string2.lower()
        #strstr
        if string1.find(string2) != -1 or string1.startswith(string2[:3]):
            return True
        else:
            return False

    def bypassValidation(str):
        if not str or len(str) < 3:
            str = "±±±"
        return str