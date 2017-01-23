'''
GnomeSort
'''


def gnomeSort(l):
    pos = 0
    while pos < len(l):
        if pos == 0 or l[pos] >= l[pos-1]:
            pos += 1
        else:
            l[pos], l[pos-1] = l[pos-1], l[pos]
            pos -= 1

v = [5,4,3,2,1,0]
print(gnomeSort(v))
print(v)



