
'''
For a given natural number n find the largest natural number written with the same digits. E.g.
n=3658, m=8653.
'''


def findNumber(n):
    m = 0
    lst = []
    while n != 0:
        lst.append(n%10)
        n = int(n / 10)

    lst.sort(key=int, reverse=True)

    for i in lst:
        m = m * 10 + i

    return m


evalNumber = int(input("Your number:"))
print("Request Numbers:", findNumber(evalNumber))
