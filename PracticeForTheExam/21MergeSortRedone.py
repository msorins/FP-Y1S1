

def mergeSort(l):

    if len(l) == 1:
        return l

    middle = len(l) // 2
    first = mergeSort(l[:middle])
    second = mergeSort(l[middle:])

    new = []
    c1 = c2 = 0

    while c1 < len(first) and c2 < len(second):
        if first[c1] < second[c2]:
            new.append(first[c1])
            c1 += 1
        else:
            new.append(second[c2])
            c2 += 1

    while c1 < len(first):
        new.append(first[c1])
        c1 += 1

    while c2 < len(second):
        new.append(second[c2])
        c2 += 1

    return new


print(mergeSort([9, 8, 7, 1514, 0, 123, 8, 3, 2 ,2 ]))