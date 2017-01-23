def function(n):
   '''
   :param n: an integer
   :return: True if the number is prime, False otherwise
   '''
   d = 2
   while (d < n - 1) and n % d > 0:
       d += 1

   return d >= n - 1


def testFunction():
    assert function(5) == True
    assert function(17) == True
    assert function(1123) == True
    assert function(1124) == False
    assert function(6) == False
    assert function(12) == False

testFunction()
