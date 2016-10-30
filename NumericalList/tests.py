__author__ = 'sorynsoo'
from NumericalList.compute import *

def testing(lstState, lst):
    testInit(lstState, lst)
    testAdd(lstState, lst)
    testInsert(lstState, lst)
    testRemove(lstState, lst)
    testRemoveRange(lstState, lst)
    testReplace(lstState, lst)
    testList(lstState, lst)
    testListRealInRange(lstState, lst)
    testListModuloIf(lstState, lst)
    testSumInRange(lstState, lst)
    testProductInRange(lstState, lst)
    testFilterReal(lstState, lst)
    testFilterModuloIf(lstState, lst)
    testRestoreState(lstState, lst)

def testInit(lstState, lst):
    lst.append([1,1])
    lst.append([2,2])
    lst.append([3,3])
    lst.append([4,4])
    lst.append([5,5])
    lst.append([6,6])
    lst.append([7,7])

def testAdd(lstState, lst):
    parse(lstState, lst, "add 8+8i")
    assert [8,8] in lst
    parse(lstState, lst, "add 9+9i")
    assert [9,9] in lst
    parse(lstState, lst, "add 10+10i")
    assert [10,10] in lst
    parse(lstState, lst, "add 10+10i")
    assert lst.count([10,10]) == 2
    parse(lstState, lst, "add 1+1i")
    assert lst.count([1,1]) == 2

def testInsert(lstState, lst):
    parse(lstState, lst, "add 0+1i at 0")
    assert lst.index([0,1]) == 0
    parse(lstState, lst, "add 99+99i at 11")
    assert lst.index([99,99]) == 11
    parse(lstState, lst, "add 999+999i at 11")
    assert lst.index([999,999]) == 11

    try:
        parse(lstState, lst, "add 1-1i at 1")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "add 1+1j a 1")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "add 1+1i at 13312")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testRemove(lstState, lst):
    parse(lstState, lst, "remove 10")
    assert(lst.count([10,10]) == 1)

    parse(lstState, lst, "remove 12")
    assert([10,10] not in lst)

    try:
        parse(lstState, lst, "remove -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "remove -15")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "remove 20")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

    try:
        parse(lstState, lst, "remove 30")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testRemoveRange(lstState, lst):
    parse(lstState, lst, "remove 10 to 13")
    assert [999,999] not in lst
    assert [99,99] not in lst
    assert lst.count([1,1]) == 1
    parse(lstState, lst, "remove 0 to 1")
    assert [0,1] not in lst

    try:
        parse(lstState, lst, "remove 0 to -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "remove 5 to 17")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testReplace(lstState, lst):
    parse(lstState, lst, "list")
    parse(lstState, lst, "replace 9+9i with 10+10i")
    assert [9,9] not in lst and [10,10] in lst

    parse(lstState, lst, "replace 10+10i with 9+9i")
    assert [9,9] in lst and [10,10] not in lst

    parse(lstState, lst, "replace 1+1i with 99+99i")
    assert [1,1] not in lst and [99,99]  in lst

    try:
        parse(lstState, lst, "replace 1+1i with 3-3i")
    except RuntimeError as e:
        assert str(e) == "Invalid command"
    try:
        parse(lstState, lst, "replace 1+1i with 4i")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "replace 1+1i with 96+12i")
    except RuntimeError as e:
        assert str(e) == "Number is not in the list"

def testList(lstState, lst):
    assert computeListAll(lst, "") == lst
    parse(lstState, lst, "add 17+17i")
    assert computeListAll(lst, "") == lst

def testListRealInRange(lstState, lst):
    #assert computeListRealInRange(lst, "real 1 to 3") == [[2,0],[3,0]]
    #assert computeListRealInRange(lst, "real 1 to 4") == [[2,0],[3,0],[4,0]]
    #assert computeListRealInRange(lst, "real 1 to 5") == [[2,0],[3,0],[4,0],[5,0]]

    try:
        parse(lstState, lst, "list real 1 to -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "list real 5 to 5000")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testListModuloIf(lstState, lst):
    assert computeListModuloIf(lst, "modulo = 2") == [[2,2]]
    assert computeListModuloIf(lst, "modulo > 20") == [[99,99], [17,17]]
    assert computeListModuloIf(lst, "modulo < 5") == [[2,2], [3,3]]

    try:
        parse(lstState, lst, "modulo | 3")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        parse(lstState, lst, "modulo < -3")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

def testSumInRange(lstState, lst):
    assert computeSumInRange(lst, "1 to 3") == [5,5]
    assert computeSumInRange(lst, "0 to 3") == [104,104]
    assert computeSumInRange(lst, "2 to 8") == [33,33]

    try:
        parse(lstState, lst, "sum 1 to -5")
    except RuntimeError as e:
        print(e)
        assert str(e) == "Invalid command"

    try:
        computeSumInRange(lst, "1 to -5")
    except RuntimeError as e:
        print(e)
        assert str(e) == "Your position does not exist"

    try:
        computeSumInRange(lst, "5 to 500")
    except RuntimeError as e:
        print(e)
        assert str(e) == "Your position does not exist"

def testProductInRange(lstState, lst):
    assert computeProductInRange(lst, "1 to 3") == [6,6]
    assert computeProductInRange(lst, "0 to 3") == [594,594]
    assert computeProductInRange(lst, "2 to 8") == [20160,20160]

    try:
        parse(lstState, lst, "product 1 to -5")
    except RuntimeError as e:
        assert str(e) == "Invalid command"

    try:
        computeProductInRange(lst, "1 to -5")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

    try:
        computeProductInRange(lst, "5 to 500")
    except RuntimeError as e:
        assert str(e) == "Your position does not exist"

def testFilterReal(lstState, lst):
    assert computeFilterReal(lstState, lst, "") == []

    parse(lstState, lst, "add 1+0i")
    parse(lstState, lst, "add 2+2i")
    parse(lstState, lst, "add 3+0i")
    parse(lstState, lst, "add 4+0i")
    assert len(computeFilterReal(lstState, lst, "")) == 3

    parse(lstState, lst, "add 5+0i")
    parse(lstState, lst, "add 6+6i")
    assert len(computeFilterReal(lstState, lst, "")) == 4

    parse(lstState, lst, "add 2+0i")
    assert len(computeFilterReal(lstState, lst, "")) == 5

def testFilterModuloIf(lstState, lst):
    print(lst)
    assert computeFilterModuloIf(lstState, lst, "modulo < 2") == [[1,0]]
    assert len(computeFilterModuloIf(lstState, lst, "modulo < 5")) == 7
    assert len(computeFilterModuloIf(lstState, lst, "modulo < 10")) == 13
    assert len(computeFilterModuloIf(lstState, lst, "modulo > 1")) == 16
    assert len(computeFilterModuloIf(lstState, lst, "modulo > 100")) == 1
    assert len(computeFilterModuloIf(lstState, lst, "modulo > 20")) == 2

def testRestoreState(lstState, lst):
    parse(lstState, lst, "add 1+1i")
    parse(lstState, lst, "add 312+2134i")
    parse(lstState, lst, "add 1+7i")

    crtLength = len(lst)
    lst = parse(lstState, lst, "undo")
    assert len(lst) == crtLength - 1

    lst = parse(lstState, lst, "undo")
    assert len(lst) == crtLength - 2

    computeFilterModuloIf(lstState, lst, "modulo < 1")
    lst = parse(lstState, lst, "undo")
    assert len(lst) == crtLength - 2
