#!/usr/bin/python3
'''
Module docstring
Pylint told me to write this
Module implements another class Graph which appears to be a Graph,
but now it's weighted. I could just add weights to previous
file and dont use them but who does that
Also modle implements 1 method of searching through Graph
'''
from graph import Graph

def fillarea(graph, weights, path, vert):
    '''subfunction of findpath and thus should not be used outside of context'''
    for i in graph.w[vert].keys():
        if weights[i] == -1:
            weights[i] = graph.w[i][vert] + weights[vert]
            path[i] = path[vert] + i
        elif graph.w[i][vert] + weights[vert] < weights[i]:
            weights[i] = graph.w[i][vert] + weights[vert]
            path[i] = path[i][:-1] + i

def findpath(graph, first, last):
    "Finds minimal weighted path"
    weights = {}
    path = {}
    path[first] = ''
    weights = weights.fromkeys(graph.vert.keys(), -1)
    weights[first] = 0
    for cur in weights.keys():
        fillarea(graph, weights, path, cur)
    return path[last]

if __name__ == '__main__':
    #V = [[0,3,5],[1,3,11],[2,3,56],[4,3,77],[5,4,89]]
    V = list(list(int(j) for j in i.split(',')) for i in input()[2:-2].split('],[')) #eval unsafe
    G = Graph(V)
    P = G.bfs('0')
    path = ''
    v = '4'
    print()
    while v != '-1':
        path += v
        v = P[v]
    print(path[::-1])
    print(findpath(G, '0', '4'))
