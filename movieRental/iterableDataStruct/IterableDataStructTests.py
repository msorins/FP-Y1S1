import unittest
from movieRental.iterableDataStruct.IterableDataStruct import *

class Tests(unittest.TestCase):
    def setUp(self):
        self._obj = IterableDataStruct()
        self._obj[0] = 0
        self._obj[1] = 1
        self._obj[2] = 2
        self._obj[3] = 3
        self._obj[4] = 4
        self._obj[5] = 5

    def testSetGetItem(self):
        self._obj[0] = 9
        assert self._obj[0]  == 9

        self._obj[1] = 10
        assert self._obj[1] == 10

        self._obj[2] = 11
        assert self._obj[2] == 11

        self._obj[6] = 6
        assert self._obj[6] == 6

        self._obj[611] = 7
        assert self._obj[7] == 7

    def testDel(self):
        self._obj.__delitem__(0)

        assert self._obj[0] != 0

        prevLen = len(self._obj)
        self._obj.__delitem__(1)
        self._obj.__delitem__(2)

        assert len(self._obj) == prevLen - 2

        self._obj.__delitem__(0)
        assert len(self._obj) == prevLen - 3

    def testIterating(self):
        crt = 0
        for i in self._obj:
            crt += 1

        assert len(self._obj) == crt

    def isEven(self, nr):
        return ( nr % 2 ) == 0

    def isOdd(self, nr):
        return ( nr % 2 ) == 1

    def testFilter(self):

        newLst = self._obj.filter([1,2,3,4,5], self.isEven)
        for crt in newLst:
            assert  crt % 2 == 0

        newLst2 = self._obj.filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 121, 2313, 59812], self.isOdd)
        for crt in newLst2:
            assert crt % 2 == 1

    def getItem(self, nr):
        return nr

    def testSort(self):

        newLst = self._obj.sort([5, 4, 3, 2, 1], self.getItem)
        for i in range(len(newLst) -1):
            assert  newLst[i] < newLst[i+1]

        newLst2 = self._obj.sort([5, 4, 3, 2, 1, 21, 512, 21939123919, 21, 0, 2131, 9238913819472918738123, 2381131], self.getItem)
        for i in range(len(newLst2) - 1):
            assert newLst2[i] <= newLst2[i + 1]

