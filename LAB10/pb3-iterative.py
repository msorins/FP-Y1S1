'''
3) The sequence a = 𝑎1, …, 𝑎𝑛 with integer elements is given. Determine all strictly increasing
subsequences of sequence a (conserve the order of elements in the original sequence).
'''
import copy
def compute():
    n = int( input("n= "))
    v = []
    st = []
    for i in range(n):
        v.append( int( input("v["+str(i)+"] = ")) )

    st.append([0])
    while(len(st)):
        crt = st[ len(st) - 1 ]
        st.pop()

        msg = ""
        for i in range(len(crt)):
            msg += str(v[crt[i]])
        print(msg)

        if len(crt) < len(v):
            last = crt[ len(crt) - 1]
            crt.append(0)
            for i in range(last + 1, len(v)):
                crt[ len(crt) - 1 ] = i
                st.append(copy.deepcopy(crt))

compute()