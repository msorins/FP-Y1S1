'''
6) Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two
solutions: (()) and ()().
'''

def bk(k, nrOpenBrackets, n, sol):
    '''
    :param k: current step
    :param nrOpenBrackets: integer
    :param sol: list
    '''
    if k == n:
        msg = ""
        for crt in sol:
            msg = msg + crt
        print(msg)
    else:
        if nrOpenBrackets > 0:
            sol[k] = ')'
            bk(k+1, nrOpenBrackets - 1, n, sol)

        if nrOpenBrackets < n - (k+1):
            sol[k] = '('
            bk(k + 1, nrOpenBrackets + 1, n, sol)

def compute():
    sol = []
    n = int( input("n= ") )

    for i in range(n):
        sol.append(0)

    bk(0, 0, n, sol)


compute()