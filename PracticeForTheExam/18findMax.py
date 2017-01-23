
def findMax(l):

    if len(l) == 1:
        return l[0]
    else:
        m = len(l) // 2
        max1 = findMax(l[:m])
        max2 = findMax(l[m:])

        return max(max1, max2)

def findMax2(l):
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], findMax2(l[1:]))

print(findMax([9,1,4,5,921,21,21314,532,122]))
print(findMax2([9,1,4,5,921,21,21314,532,122]))