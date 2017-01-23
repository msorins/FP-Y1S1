'''
12) Consider the natural number n (n<=10) and the natural numbers 𝑎1, …, 𝑎𝑛. Determine all the
possibilities to insert between all numbers 𝑎1, …, 𝑎𝑛 the operators + and – such that by evaluating the
expression the result is positive.
'''

def suc(k):
    ok = False
    for i in range(len(k)-1, -1, -1):
        if k[i] == 0:
            k[i] = 1
            ok = True
            break
        else:

            k[i] = 0
            continue
    if ok:
        return k
    else:
        return -1

def compute():
    n = int( input("n= ") )
    a = []
    k = []
    result = 0

    for i in range(n):
        a.append( int(input("a" + str(i) + ": ")) )
        k.append(0)

    while(1):
        sum = 0
        for j in range(n):
            if k[j] == 0:
                sum += a[j]
            if k[j] == 1:
                sum -= a[j]


        if sum > 0:
            result += 1
            s = ""
            for j in range(n):

                if k[j] == 0:
                    s = s + " + " + str(a[j])
                else:
                    s = s + " - " + str(a[j])
            print(s)

        k = suc(k)
        if k == -1:
            return

    return result

print( str(compute()) )
