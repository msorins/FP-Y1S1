'''
3) The sequence a = 𝑎1, …, 𝑎𝑛 with integer elements is given. Determine all strictly increasing
subsequences of sequence a (conserve the order of elements in the original sequence).
'''

def bk(k, a, v):
    '''
    :param k: step
    :param v: vector of elements
    :param a: backtrack vector of positions
    '''

    msg = ""
    for i in range(k):
        msg += str(v[a[i]])
    print(msg)

    for i in range(a[k-1] + 1, len(v)):
        a[k] = i
        bk(k+1, a, v)

def compute():
    n = int( input("n= "))
    v = []
    a = []
    for i in range(n):
        v.append( int( input("v["+str(i)+"] = ")) )
        a.append( 0 )
    a.append(0)

    bk(1, a, v)

compute()
