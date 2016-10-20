'''
Consider a given natural number n. Determine the product p of all the proper factors of n
'''

def computeProductOfFactor(n):
    i = 2
    prod = 1

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            prod = prod * i

    return prod


evalNumber = int(input("Your number: "))
print("Product of all the proper factors of n: ", computeProductOfFactor(evalNumber))


'''
10 = 2 * 5

12 =
12 / 2 = 6 / 2 = 3 / 3 = 1
'''