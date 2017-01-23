'''
6) Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two
solutions: (()) and ()().
'''
import copy


def compute():
    sol = []
    st = []
    n = int( input("n= ") )


    sol.append('(')
    st.append(sol)

    while(len(st)):
        crt = st[len(st) -1]
        st.pop()

        if len(crt) == n:
            nrp = 0
            ok = True
            for i in crt:
                if i == '(':
                    nrp += 1

                if i == ')':
                    nrp -= 1

                if nrp < 0:
                    ok = False
                    break


            if nrp == 0 and ok:
                res = ''
                for i in crt:
                    res += i
                print(res)

            continue

        crt.append('(')
        st.append(copy.deepcopy(crt))

        crt.pop()
        crt.append(')')
        st.append(copy.deepcopy(crt))


compute()
