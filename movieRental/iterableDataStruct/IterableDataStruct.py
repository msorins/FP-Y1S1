import sys

class IterableDataStruct:
    def __init__(self):
        '''
        :param lst: a list
        '''
        self._lst = []
        self._i = 0

    def __setitem__(self, key, value):
        '''
        :param key: index of the element from the list (integer)
        :param value: value to be setted
        '''
        if key >= len(self._lst):
            self._lst.append(value)
        else:
            self._lst[key] = value

    def __getitem__(self, item):
        '''
        :param item: index of the element from the list
        :return: the element
        '''
        if item >= len(self._lst):
            return Rai

        return self._lst[item]

    def __delitem__(self, key):
        '''
        :param key: index of the element from the list
        :return:
        '''
        if key < len(self._lst):
            self._lst.pop(key)

    def __iter__(self):
        '''
        :return: Returns an iterator to the list that we iterate over
        '''
        return iter(self._lst)

    def __next__(self):
        '''
        :return: the next item from the lst list
        '''
        if self._i >= len(self._lst):
            raise StopIteration
        else:
            self._i += 1
            return self._lst[self._i]

    def __len__(self):
        return len(self._lst)


    def filter(self, lst, func):
        '''
        :param func: Returns True if the element must be in the filtered lsit
        :return: the new filtered list
        '''
        newLst = []
        for crt in lst:
            if func(crt):
                newLst.append(crt)

        return newLst

    def getBytes(self, step, number):
        '''
        :param number: an integer value
        :return:
        '''
        return (number >> (step * 8)) & 255

    def append(self, item):
        self.__setitem__(len(self._lst), item)

    def pop(self, index):
        self.__delitem__(index)

    def sort(self, lst, getItem):
        '''
         RADIX SORT
        :param lst: the list to be sorted
        :param getItem: returns the item for sorting
        :return: sorted list
        '''
        nrSteps = 0
        maxNrSteps = 0

        for crt in lst:
            maxNrSteps = max(maxNrSteps, sys.getsizeof(getItem(crt)))

        while(True):
            queue = {}
            for crt in lst:
                if not self.getBytes(nrSteps, getItem(crt)) in queue:
                    queue[ self.getBytes(nrSteps, getItem(crt)) ] = []

                queue[self.getBytes(nrSteps, getItem(crt))].append(crt)

            lst = []
            for i in range(256):
                if i in queue:
                    for crt in queue[i]:
                        lst.append(crt)

            if nrSteps == maxNrSteps:
                break

            nrSteps += 1

        return lst
