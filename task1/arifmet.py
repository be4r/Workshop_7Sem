#!/usr/bin/python3

'''
INPUT : 
    (1->2->3->4) + (1->2->3->4)
    numbers are written backwards, it is equivalent to 4321 + 4321
OUTPUT:
    (2->4->6->8)
    which is 8642
'''

from list import l

if __name__ == "__main__":
    s = input()
    a, b = s.split("+")
    a = int(("".join(a.replace(')','').replace('(','').replace(' ','').split('->')))[::-1])
    b = int(("".join(b.replace(')','').replace('(','').replace(' ','').split('->')))[::-1])
    print(l(a) + l(b))
