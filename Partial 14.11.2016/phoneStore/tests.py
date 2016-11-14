__author__ = 'sorynsoo'

from phoneStore.phoneManager import *

def testsMain(lst):
    populate(lst)
    testAddPhone(lst)
    testRemovePhone(lst)
    testChangePrice(lst)
    testSortedPhoneList(lst)

def populate(lst):
    lst.append(["Nokia", "1100", 200])
    lst.append(["Apple", "7S Plus", 4000])
    lst.append(["Samsung", "S7 Edge", 2800])
    lst.append(["Samsung", "S4 Mini", 800])
    lst.append(["Xiaomi", "MI2", 1100])
    lst.append(["Asus", "ZenPhone", 1000])
    lst.append(["HTC", "M10", 2900])
    lst.append(["Allview", "P5-Dual", 219])
    lst.append(["LGe", "G2c", 920])
    lst.append(["Sony", "Z3c", 2500])
    return lst

def testAddPhone(lst):
    crt = len(lst)
    addPhone(lst, "Samsung", "J5-2016", 900)
    assert len(lst) == crt + 1
    addPhone(lst, "Microsoft", "Lumia 640", 1500)
    assert len(lst) == crt + 2
    addPhone(lst, "Huawei", "Mate 9", 2350)
    assert len(lst) == crt + 3

    try:
        addPhone(lst, "B", "ZXL", 2124)
    except Exception as e:
        assert str(e) == "One field contains lass than three characters. Opsey"

    try:
        addPhone(lst, "eBoda", ".", 305)
    except Exception as e:
        assert str(e) == "One field contains lass than three characters. Opsey"

def testRemovePhone(lst):
    crt = len(lst)
    removePhone(lst, "Samsung", "J5-2016")
    assert len(lst) == crt - 1
    removePhone(lst, "Microsoft", "Lumia 640")
    assert len(lst) == crt - 2
    removePhone(lst, "Huawei", "Mate 9")
    assert len(lst) == crt - 3

    try:
        removePhone(lst, "B", "ZXL")
    except Exception as e:
        assert str(e) == "Phone manufacturer and model not found. Opsey"

    try:
        removePhone(lst, "eBoda", ".")
    except Exception as e:
        assert str(e) == "Phone manufacturer and model not found. Opsey"

def testChangePrice(lst):
    changePrice(lst, "Sony", "Z3c", 2599)
    for crt in lst:
        if crt[0] == "Sony" and crt[1] == "Z3c":
            assert crt[2] == 2599

    changePrice(lst, "LGe", "G2c", 950)
    for crt in lst:
        if crt[0] == "LGe" and crt[1] == "G2c":
            assert crt[2] == 950


    try:
        changePrice(lst, "Bsad", "ZXL", 1005)
    except Exception as e:
        assert str(e) == "Phone manufacturer and model not found. Opsey"

    try:
        changePrice(lst, "Sony", "Z9", 4315)
    except Exception as e:
        assert str(e) == "Phone manufacturer and model not found. Opsey"

def testSortedPhoneList(lst):
    sortedLst = sortedPhoneList(lst)
    for i in range(len(lst) - 1):
        if sortedLst[i][2] > sortedLst[i+1][2]:
            assert False