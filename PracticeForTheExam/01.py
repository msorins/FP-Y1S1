def f(l):
    print("A")
    if l == []:
       raise ValueError()
    print("B")

def start():
   l = []
   try:
       print("A")
       f(l)
       print("D")
   except ValueError:
       print("C")
start()