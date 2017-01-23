'''
Created on Sep 29, 2016

@author: http://www.python-course.eu/global_vs_local_variables.php
'''

'''
    NB!
    Uncomment each of the sections separated by ### below,
    one at a time and run them
'''



#############################
'''
    What happens in the example below?
'''
def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)
    '''
        NB!
        Learn to use the locals() and globals() functions to figure out what's what

         print(locals())
         print(globals())
     '''

a,b,x,y = 1,15,3,4
foo(17,4)
print(a,b,x,y)

'''
PRINT:
42 17 4 17
42 15 3 4


'''