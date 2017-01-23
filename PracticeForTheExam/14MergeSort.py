'''
MergeSort
'''


def mergeSort(l):
    if len(l) >= 2:
        middle = len(l) // 2

        lSt = mergeSort(l[:middle])
        lDr = mergeSort(l[middle:])

        lNew = []
        c1 = c2 = 0

        while c1 < len(lSt) and c2 < len(lDr):
            if lSt[c1] < lDr[c2]:
                lNew.append(lSt[c1])
                c1 += 1
            else:
                lNew.append(lDr[c2])
                c2 +=1

        while c1 < len(lSt):
            lNew.append(lSt[c1])
            c1 += 1

        while c2 < len(lDr):
            lNew.append(lDr[c2])
            c2+=1

        return lNew
    return l

v = [5,4,3,2,1,0, 9 , 21 , 2913813, 21, 15]
print(mergeSort(v))
print(v)



