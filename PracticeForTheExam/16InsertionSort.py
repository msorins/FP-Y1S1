'''
InsertionSort
'''


def insertionSort(l):
    for i in range(1, len(l)):
        index = i - 1
        elem = l[i]

        while index >= 0 and elem < l[index]:
            l[index + 1] = l[index]
            index -= 1

        l[index + 1] = elem



v = [5,4,3,2,1,0, -5, 9999]
print(insertionSort(v))
print(v)



