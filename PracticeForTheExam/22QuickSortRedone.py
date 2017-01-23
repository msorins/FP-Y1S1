def partition(l, left, right):
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
    pos = partition(l, left, right)

    if pos - left >= 2:
        quickSort(l, left, pos - 1 )
    if right - pos >= 2:
        quickSort(l, pos + 1, right)

    return l


print(quickSort([9, 7, 2, 1, 1921, -5 , 2], 0, 6))