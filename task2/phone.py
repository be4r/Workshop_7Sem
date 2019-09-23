#!/usr/bin/python3

numbers = {"1":"O_O", "2":"abc", "3":"def", 
           "4":"ghi", "5":"jkl", "6":"mno", 
           "7":"pqrs", "8":"tuv", "9":"wxyz",
           "0":" "}

words = [''] #placeholder
num = input()
for i in num:
    if numbers.get(i) is not None:
        tmp = []
        for j in numbers[i]:
            for k in words:
                tmp.append(k+j)
        words = tmp

print(words)
