#!/usr/bin/python3

'''
2xLINKED LIST, well, sorta
by BE4R, fri 13.09.2019 11:10

'''

class link:
    prev = 0
    next = 0
    val  = 0
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

class l:
    head = 0
    tail = 0

    def __init__(self, val):
        self.head = link(val % 10)
        t = self.head
        while val > 0:
            val //= 10
            if val == 0:
                break
            t.next = link(val % 10)
            t.next.prev = t
            t = t.next
        self.tail = t
        

    def __add__(self, lst):
        perenos_desyatkov_na_sleduyushuyu_iteration = 0
        res = l(0)
        h1 = self.head
        h2 = lst.head
        dif = abs(len(self) - len(lst))
        if len(self) > len(lst):
            for i in range(dif):
                lst.push(0)
        if len(self) < len(lst):
            dif *= -1
            for i in range(dif):
                self.push(0)
        while h1.next and h2.next:
            sum = h1.val + h2.val + perenos_desyatkov_na_sleduyushuyu_iteration
            res.append(sum % 10)
            perenos_desyatkov_na_sleduyushuyu_iteration = sum // 10
            h1 = h1.next
            h2 = h2.next
        res.append(h1.val + h2.val +             perenos_desyatkov_na_sleduyushuyu_iteration)
        for i in range(dif):
            if dif > 0:
                self.pop()
            else:
                lst.pop()
        res.popback()
        
        return res
        
    def __len__(self):
        i = 0
        for j in self:
            i += 1
        return i

    def reverse(self):
        res = l(0)
        for i in self:
            res.pushback(i.val)
        res.pop()
        return res
        

    def add(self, l): # link
        self.tail.next = l
        l.prev = self.tail
        t = l
        while t.next:
            t = t.next
        self.tail = t
        return self

    def push(self, val):
        self.tail.next = link(val)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        return self

    def pushback(self, val):
        self.head.prev = link(val)
        self.head.prev.next = self.head
        self.head = self.head.prev
        return self

    def insert(self, id, val):
        t = self[id]
        tmp = link(val)
        if id == 0:
            tmp.next = t
            t.prev = tmp
            self.head = tmp
        else:
            if t.next:
                tmp.next = t.next
                t.next.prev = tmp
            t.next = tmp
            t.next.prev = t

        return self
    
    def append(self, val):
        if val == 0:
            self.tail.next = link(val % 10)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            val //= 10
        while val > 0:
            self.tail.next = link(val % 10)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            val //= 10
            
        return self

    def __getitem__(self, id):
        if id == -1:
            return self.tail
        t = self.head
        i = 0
        while t and t.next and i < id:
            t = t.next
            i += 1
        if id < 0 or i < id:
            raise IndexError("no such index")
        return t
        
    def delete(self, id):
        if self.head is self.tail:
            self.head = link(0)
            return self
        t = self[id]
        if t.next:
            t.next.prev = t.prev
        if t.prev:
            t.prev.next = t.next
        if t is self.head:
            self.head = self.head.next
        if t is self.tail:
            self.tail = self.tail.prev
        return self


    def index(self, val):
        t = self.head
        i = 0
        while t:
            if t.val == val:
                return i
            t = t.next
            i += 1
        return -1
    
    def pop(self):
        tmp = self.tail
        if self.tail == self.head:
            self.tail = self.head = link(0)
        else:
            self.tail = self.tail.prev
            self.tail.next = 0
        return tmp
    
    def popback(self):
        tmp = self.head
        if self.tail == self.head:
            self.tail = self.head = link(0)
        else:
            self.head = self.head.next
            self.head.prev = 0
        return tmp

    def __repr__(self):
        t = self.head
        if t == 0:
            return "()"
        s = "(%d" % t.val
        while t.next:
            t = t.next
            s += "->%d" % t.val
        s += ")"
        return s

    def remove(self, val):
        self.delete(val)
    
    def find(self, val):
        self.index(val)



if __name__ == "__main__":
    s = input()
    a, b = s.split("+")
    a = int(("".join(a.replace(')','').replace('(','').split('->')))[::-1])
    b = int(("".join(b.replace(')','').replace('(','').split('->')))[::-1])
    print(l(a) + l(b))
