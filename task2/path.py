#!/usr/bin/python3
'''
Module docstring
Pylint told me to write this
Uses method of Graph struct, implements nothing new
Start and End vertexes of graph should be separated by single space
'''
from graph import Graph

if __name__ == '__main__':
    #V = [[0,3,5],[1,3,11],[2,3,56],[4,3,77],[5,4,89]]
    V = list(list(int(j) for j in i.split(',')) for i in input()[2:-2].split('],[')) #eval unsafe

    G = Graph(V)
    print(' '.join(list(G.findpath(*(str(i) for i in input().split(' '))))))
