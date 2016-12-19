from MODEL.studentModel import *


class UI():
    def __init__(self, studentController):
        self.printMenu()
        self._studentController = studentController

        try:
            while 1 == 1:
                self.readCommand()
        except Exception as e:
            print(e)

    def printMenu(self):
        menu = [
            '',
            '1. Add student',
            '2. Give a bonus.',
            '3. Display students (select by partial name)',
            '4. Display students (decreasing order of their grades)',
            ''
        ]

        for line in menu:
            print(line)

    def readCommand(self):

        nr = int(input("Command: "))

        if nr == 1:
            self._studentController.add( Student( self._studentController.getNumberOfStudents() + 1, input("Name: "), input("Attendance count: "), input("Grade: ") ) )

        if nr == 2:
            p = int(input("p: "))
            b = int(input("b: "))

            self._studentController.giveBonus(p, b)

        if nr == 3:
            partialName = input("Partial name: ")

            obj = self._studentController.displayStudentsSelective(partialName)
            for crt in obj:
                print(str(crt.getId()) + ", " + str(crt.getName()) + ", " + str(crt.getAttendanceCount()) + ", " + str(
                    crt.getGrade()))

        if nr == 4:
            obj = self._studentController.displayStudentsSorted()
            for crt in obj:
                print(str(crt.getId()) + ", " + str(crt.getName()) + ", " + str(crt.getAttendanceCount()) + ", " + str(
                    crt.getGrade()))
