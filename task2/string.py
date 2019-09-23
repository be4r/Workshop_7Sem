#!/usr/bin/python3

s = input()

for i in range(1,int(len(s)/2 + 1)): #optimisation
    for j in range(0,len(s),i):
        if s[j:j+i] != s[:i]:
            break
    else:
        print(int(len(s)/i))
        break
else:
    print(1)
