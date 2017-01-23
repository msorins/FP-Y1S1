'''
12) Consider the natural number n (n<=10) and the natural numbers 𝑎1, …, 𝑎𝑛. Determine all the
possibilities to insert between all numbers 𝑎1, …, 𝑎𝑛 the operators + and – such that by evaluating the
expression the result is positive.
'''

result = 0
def bk(i, n, data):
    if i == len(data[0]):
        sum = 0
        for j in range(0, n):
            if data[1][j] == 1:
                sum += data[0][j]
            else:
                sum -= data[0][j]

        if sum > 0:
            global result
            result += 1
            s = ""
            for j in range(0,n):

                if data[1][j] == 1:
                    s = s + " + " + str(data[0][j])
                else:
                    s = s + " - " + str(data[0][j])
            print(s)


    else:
            data[1][i] = 0
            bk(i + 1, n, data)

            data[1][i] = 1
            bk(i + 1, n, data)

def compute():
    n = int( input("n= ") )
    a = []
    k = []

    for i in range(n):
        a.append(int(input("a" + str(i) + ": ")))
        k.append(0)

    bk(0, n, [a, k])

    return result



print( str(compute()) )