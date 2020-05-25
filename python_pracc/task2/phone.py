#!/usr/bin/python3
'''
#INSERT DOCSTRING HERE#
Calculates all string that could be obtained
by pressing given number buttons on cellphone
'''
NUMBERS = {"1":"O_O", "2":"abc", "3":"def",
           "4":"ghi", "5":"jkl", "6":"mno",
           "7":"pqrs", "8":"tuv", "9":"wxyz",
           "0":" "}

WORDS = [''] #placeholder
NUM = input()
for i in NUM:
    if NUMBERS.get(i) is not None:
        TMP = []
        for j in NUMBERS[i]:
            for k in WORDS:
                TMP.append(k+j)
        WORDS = TMP

print(WORDS)
