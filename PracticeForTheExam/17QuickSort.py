'''
QuickSort
'''

def quickPartition(l, left, right):
    pivot = l[right]
    i = left
    j = right

    while i != j:
        while pivot >= l[i] and i < j:
            i += 1

        l[j] = l[i]

        while pivot <= l[j] and i < j:
            j -= 1

        l[i] = l[j]

    l[j] = pivot
    return i


def quickSort(l, left, right):
    pos = quickPartition(l, left, right)

    if left < pos - 1:
        quickSort(l, left, pos - 1)
    if pos + 1 < right:
        quickSort(l, pos + 1, right)



v = [5, 4, 3, 2, 9, 8, 7, 6]
print(quickSort(v, 0, len(v) - 1))
print(v)


'''
3 9 2 1 5 6

pivot = 3
left = i = 0
right = j = 6

while i != j :

    1st while:
    6 >= 3 => j = 4
    5 >= 3 => j = 3

    1 < 3 .. done

    l[i] = l[j] => (1) 9 2 1 5 6

    2nd while:
    1 <= 3 => i = 1

    9 > 3 ... done

    l[j] = l[i] => (1) 9 2 9 5 6

    fin:
    1 3 2 9 5 6




'''