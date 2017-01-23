def complexity_2(x):
    found = False
    n = len(x) - 1
    while n != 0 and not found:
        if x[n] == 7:
            found = True
        else:
            n = n - 1
    return found


'''
Time Complexity:
Best case:
T(1) => O(1) -> the number is found in the first step

Worst case:
T(n) => O(n) -> the number is found the last

Average case:
(1+2+3+..+n)/n = n(n+1)/2 * 1/ n = (n+1)/2

'''