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
    
    initial = {'cmd': mode,'size': os.stat(path).st_size}
    #initial['size'] = 2301#8890
    socket.send(str(initial).encode("utf-8"))
    
    kkk = 0

    if socket.recv(128).decode("utf-8") == 'accept':
        with open(path, encoding="utf-8", errors="replace") as ff:
            f = csv.reader(ff)
            for row in f:
                kkk += 1
                if kkk == 1:
                    continue #first useless row
                socket.send((";".join(row)+'\n').encode("utf-8"))

                if kkk > 10:
                    break

def main():
    with socket.create_connection(("127.0.0.1", 30000)) as sock:
        sendData(sock)#, mode="ENTI")
        sock.sendall(b"")
        result = ""
        while True:
            data =sock.recv(1024).decode("utf-8")
            result += data
            if data == "":
                break
        print("Recieved: \n")
        rec= ast.literal_eval(result)
        for i in rec:
            print("\n\t", i, ":\n\t", rec[i])

main()
