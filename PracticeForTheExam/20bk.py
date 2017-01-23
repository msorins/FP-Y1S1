res = []
def bk(l, n):
    if len(l) == n:
        global res
        res.append(l)
    else:
        l.append(0)
        for i in range(10):
            l[-1] = i
            bk(l[:], n)

bk([], 7)
print(res)