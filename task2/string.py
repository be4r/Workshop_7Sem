#!/usr/bin/python3

'''
Module docstring
Pylint told me to write this
Modules only purpose being implementation of a function that can
do something with strings and i dont even
remember what is its goal to begin with.
So the process of me writing down this doc is utterly useless.
Its even more useless than it could ever have been if just i would
remember what does this program do.
Also previous line is split into much more than 3 lines by 10 words each
because Pylint thinks that one is too long even though its just
some documentations nobody will ever read. . .
'''

S = input()

for i in range(1, int(len(S)/2 + 1)): #optimisation
    for j in range(0, len(S), i):
        if S[j:j+i] != S[:i]:
            break
    else:
        print(int(len(S)/i))
        break
else:
    print(1)
