#!/usr/bin/python3

import socket
import os
import csv
import ast 

def sendData(socket, mode = 'STAT', path = 'coreNLP/dataSet.csv'):
    '''
    mode: STAT / ENTI
    '''
    if mode not in ('ENTI, STAT'):
        print("Malformed input data")
        return 

    size = os.stat(path).st_size
    #size = 2395#8890
    initial = "GET /" + mode + " HTTP/3.0\nContent-length: " + str(size) + "\nConnection: keep-alive\n\n"
    
    socket.send(initial.encode("utf-8"))
    
    kkk = 0

    if socket.recv(128).decode("utf-8") == 'HTTP/3.0 418 I\'m a teapot\n\n':
        with open(path, encoding="utf-8", errors="replace") as ff:
            f = csv.reader(ff)
            for row in f:
                kkk += 1
                if kkk == 1:
                    continue #first useless row
                socket.send(("POST / HTTP/3.0\n"+";".join(row)+'\n').encode("utf-8"))

                if kkk > 10:
                    break


with socket.create_connection(("127.0.0.1", 80)) as sock:
    sendData(sock)#, mode="ENTI")
    sock.sendall(b"")
    result = ""
    while True:
        data =sock.recv(1024).decode("utf-8")
        if data.startswith('HTTP 200 OK\n'):
            data = data[12:]
        result += data
        if data == "":
            break
    print("Recieved: \n")
    rec= ast.literal_eval(result)
    __import__("pprint").pprint(rec)
