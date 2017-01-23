def power(x, n):

    if n == 0:
        return 1
    if n == 1:
        return x

    #Divide
    aux = power(x, n // 2)

    #Conquer
    if n % 2 == 0:
        return aux * aux
    else:
        return aux * aux * x


print( power(2,5) )

