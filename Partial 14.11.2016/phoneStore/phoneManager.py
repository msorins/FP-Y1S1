__author__ = 'sorynsoo'

def addPhone(lst, manufacturer, model, price):
    '''
    :param lst: the phone list
    :param manufacturer: a string with length >= 3
    :param model: a string with length >= 3
    :param price: an integer
    :return: the phone list with a new entry
    :exception: if manufacturer and model have length lower than 3
    '''
    if len(manufacturer) < 3 or len(model) < 3:
        raise RuntimeError("One field contains lass than three characters. Opsey")

    price = int(price)

    lst.append([manufacturer, model, price])

def removePhone(lst, manufacturer, model):
    '''
    :param lst: the phone list
    :param manufacturer: a string with length >= 3
    :param model: a string with length >= 3
    :return: the phone list with an erased element
    :exception: if manufacruter and model not found in the phone list
    '''
    for i in range(len(lst)):
        if lst[i][0] == manufacturer and lst[i][1] == model:
            lst.pop(i)
            return lst

    raise RuntimeError("Phone manufacturer and model not found. Opsey")

def changePrice(lst, manufacturer, model, price):
    '''
    :param lst: the phone list
    :param manufacturer: a string with length >= 3
    :param model: a string with length >= 3
    :param price: an integer
    :return: the phone list with a new entry
    :exception: if manufacruter and model not found in the phone list
    '''
    price = int(price)

    for i in range(len(lst)):
        if lst[i][0] == manufacturer and lst[i][1] == model:
            lst[i][2] = price
            return lst

    raise RuntimeError("Phone manufacturer and model not found. Opsey")

def sortedPhoneList(lst):
   '''
   :param lst: the phone list
   :return: the phone list sorted by increasing price
   '''
   return sorted(lst, key=lambda x: int(x[2]))

