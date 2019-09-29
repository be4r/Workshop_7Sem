#!/usr/bin/python3
'''
Module docstring
Pylint told me to write this
Modules only purpose being implementation of a function that can
find most frequently used word in text which does not
contain to or more consequent newlines
Also previous line is split into 3 lines 10 WORDS each
because Pylint thinks that one is too long even though its just
some documentations nobody will ever read. . .
'''
WORDS = {}
while True:
    S = input() # s is not constant, why should it be caps?
    if S == '':
        break
    for i in S.split(' '):
        if WORDS.get(i) is None:
            WORDS[i] = 1
        else:
            WORDS[i] = WORDS[i] + 1
    WORDS = sorted(WORDS.items(), key=lambda x: x[1], reverse=True)
    print(WORDS[0][0] if len(WORDS) < 2 or WORDS[0][1] > WORDS[1][1] else '---')
