#!/usr/bin/python3

words = {}
while True:
    s = input()
    if s is '':
        break
    for i in s.split(' '):
        if words.get(i) is None:
            words[i] = 1
        else:
            words[i] = words[i] + 1
    words = sorted(words.items(), key=lambda x:x[1], reverse = True)
    print(words[0][0] if len(words) < 2 or words[0][1] > words[1][1] else '---')
