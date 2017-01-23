class A:
    def f(self, l, nr):
        l.append(nr)

class B:
    def g(self, l, nr):
        nr=nr-1
        l = l+[-2]

a = A()
b = B()
l = [1,2]

c = -1
a.f(l,6)
b.g(l,c)
print(l,c)

'''
l = [1, 2, 6]
c = -1
'''