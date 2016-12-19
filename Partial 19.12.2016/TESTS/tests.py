__author__ = 'sorynsoo'

import unittest
from CONTROLLER.studentController import *
from REPOSITORY.studentFileRepository import *

setup = False

class Tests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        self._studentFileRepository = StudentFileRepository('/Users/sorynsoo/Desktop/UBB/Partial 19.12.2016/DATA/db-test.txt')
        self._studentControllerObj = StudentController(self._studentFileRepository)

    def populateValues(self):
        pass

    def testAddStudents(self):
       self._studentControllerObj.add(Student(1, "Mircea Sorin", 8, 10))
       assert self._studentControllerObj.getNumberOfStudents() == 1

       self._studentControllerObj.add(Student(1, "Mihalache Mihai", 11, 9))
       assert self._studentControllerObj.getNumberOfStudents() == 2

       self._studentControllerObj.add(Student(1, "Jugaru Robert", 3, 5))
       assert self._studentControllerObj.getNumberOfStudents() == 3

       try:
           self._studentControllerObj.add(Student(1, "Castan", 3, 5))
       except Exception as e :
           assert str(e) == "Name length must contain at least 2 words"


    def testGiveBonus(self):
        self._studentControllerObj.giveBonus(10, 1)

        obj = self._studentFileRepository.load()
        for crt in obj:
            if crt.getName() == "Mihalache Mihai" and crt.getGrade() != 10:
                assert False

        self._studentControllerObj.giveBonus(3, 5)

        obj = self._studentFileRepository.load()
        for crt in obj:
            if crt.getName() == "Jugaru Robert" and crt.getGrade() != 10:
                assert False

    def testdisplayStudentsSelective(self):

        obj = self._studentControllerObj.displayStudentsSelective("So")
        assert len(obj) == 1

        obj = self._studentControllerObj.displayStudentsSelective("a")
        assert len(obj) == 3

        obj = self._studentControllerObj.displayStudentsSelective("XXXX")
        assert len(obj) == 0



    def testdisplayStudentsSorted(self):
        obj = self._studentControllerObj.displayStudentsSorted()

        for i in range(len(obj) -1):
            if obj[i].getName() > obj[i+1].getName():
                assert False



