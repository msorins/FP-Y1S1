'''
 A number of n coins are given, with values of 𝑎1, …, 𝑎𝑛 and a value s. Display all payment modalities
for the sum s. If no payment modality exists print a message.
'''

def bk(k, sum, answer, stopSum, v):
    '''
    :param k: current iteration step (integer)
    :param sum: sum until the current iteration (integer)
    :param v: list of interegers representing the sum
    '''
    if k == len(v) and sum == stopSum:
        msg = ""
        for crt in answer:
            msg += str(crt) + " "
        print(msg)
    else:
        for crt in v:
            if sum + crt  <= stopSum:
                answer[k] = crt
                bk(k+1, sum + crt, answer, stopSum, v)

def compute():
    n = int( input("n = "))
    s = int( input("s = "))
    v = []
    answer = []

    for i in range(n):
        v.append( int( input("v["+str(i)+"] = ")))
        v.append( 0 )

    print( bk(0, 0, answer, s, v) )