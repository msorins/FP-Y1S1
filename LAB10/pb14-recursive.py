'''
14) Generate all numbers of n digits with the property that no number has two identical neighboring
subsequences. For example, for n=6, 121312 is correct, and 121313 and 132132 are not correct.
'''

def bk(k, n, v):

    if k == n:
        msg = ''
        for crt in v:
            msg += str(crt)
        print(msg)
    else:
        if k == 0:
            st = 1
        else:
            st = 0

        for i in range(st, 10):
            v[k] = i
            bk(k+1, n, v)


def compute():
    n = int( input("n = ") )
    a = []
    for i in range(n):
        a.append(0)
    bk(0, n, a)

compute()