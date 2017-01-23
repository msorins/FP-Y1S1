"""
 Compute the sum of even elements in the given list
 input:
 l - the list of numbers
 output:
 The sum of the even elements in the list

 Raises TypeError if parameter l is not a Python list
 Raises ValueError if the list does not contain even numbers
"""

def compute(l):
    '''
    :param l: the list of numbers
    :return: the sum of the even elements in the list
    '''
    sum = 0

    for crt in l:
        if crt % 2 == 0:
            sum += crt

    return sum

def testsCompute():
    assert compute([1, 2 , 3, 4]) == 6
    assert compute([1, 3, 5, 7]) == 0
    assert compute([8, 4 , 12 , 20 ]) == 44


testsCompute()