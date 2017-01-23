def complexity_1(x):
    m = len(x)
    found = False
    while m >= 1:
        c = m - m / 3 * 3
        if c == 1:
             found = True
        m = m / 3


complexity_1([1,2,3,41,21,31,4, 4, 5, 1, 2, 3
              ])
'''
Time Complexity:
Best Case:
T(1) => O(1)

Worst Case:
T( log3(n) ) => O( log3(n) )

Average Case:
execution is
(1 + 2 + ... + log3(n)) / n = log3(n) * log3(n+1) / 2n = log3n(n^2+n) / 2n ?

Space complexity:
T(1)


'''