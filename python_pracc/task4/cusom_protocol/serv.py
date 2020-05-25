#!/usr/bin/python3

import socket
import ast
import csv
import re
from pycorenlp import StanfordCoreNLP


def namedEntities(nlp, line):
    result = nlp.annotate(line, properties={ 'annotators': 'ner', 'outputFormat': 'json', 'timeout': 1000, })
    pos = []
    if type(result) == str:
        return result
    for word in result["sentences"][1]['tokens']:
        pos.append('{} ({})'.format(word['word'], word['ner']))
    return (" ".join(pos))

def count(data):
    tags = data.split(';')
    content = tags[6::18]
    rts = tags[8::18]
    uname = tags[3::18]
    country = tags[10:18]

    #1) top10 words: sort by encounter each of them, out words
    #2) top10 tweets: sort by RTs, out RTS+uname/nick
    #3) top10 authors: sum(rts), out uname/nick
    #4) country

#    words = sorted(word_temp, key=labmda x: x[1])[:10]
    words_w = {}
    words = re.findall(r"[\w]+"," ".join(content))
    for word in words:
        if words_w.get(word) is None:
            words_w[word] = 1
        else:
            words_w[word] += 1
    try:
        top10words = sorted(words_w.items(), key = lambda x: -int(x[1]))[:10]
    except ValueError:
        pass

    maxrts = [(0,0) for i in range(10)]
    rts_w = {}
    try:
        for i in range(len(rts)):
            if int(rts[i]) > maxrts[9][0]:
                maxrts.append((rts[i],uname[i]))
            maxrts = sorted(maxrts, key = lambda x: -int(x[0]))[:10]
            if rts_w.get(uname[i]) is None:
                rts_w[uname[i]] = rts[i]
            else:
                rts_w[uname[i]] += rts[i]

    except ValueError:
        pass
    try:
        top10authors = sorted(rts_w.items(), key = lambda x: -int(x[1]))[:10]
    except ValueError:
        pass

    countriesr = {}
    countriesp = {}
    try:
        for i in country:
            if countriesp.get(i) is None:
                countriesp[i] = 1
            else:
                countriesp[i] += 1
        for i in range(len(content)):
            if content[i].startswith("RT @"):
                if countriesr.get(country[i]) is None:
                    countriesr[country[i]] = 1
                else:
                    countriesr[country[i]] += 1
    except:
        pass
    result = {}
    result['top10words'] = top10words
    result['maxreposts'] = maxrts
    result['top10authors'] = top10authors
    result['countries_produce'] = countriesp
    result['countries_retweet'] = countriesr
    return result


def main():
    result = ""
    with socket.socket() as sock:
        sock.bind(("", 30000))
        sock.listen()
        
        while True:
            conn, addr = sock.accept()
            with conn:
                data = conn.recv(1024)
                print(data)
                req = ast.literal_eval(data.decode("utf8"))

                conn.send(b'accept')
                data = b""
                while True:
                    line = conn.recv(1024)
                    data += line
                    print(line)
                    print(len(data), req['size'])
                    if line == b"" or len(data) >= req['size']:
                        break

                if req['cmd'] == 'ENTI':
                    nlp = StanfordCoreNLP('http://127.0.0.1:9000')
                    result = namedEntities(nlp, data.decode("utf-8"))
                if req['cmd'] == 'STAT':
                    result = str(count(data.decode("utf-8")))

                conn.send(result.encode("utf-8"))
                conn.close()

main()
