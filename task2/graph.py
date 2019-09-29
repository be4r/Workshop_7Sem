#!/usr/bin/python3
'''
Module docstring
Pylint told me to write this
Module implements class Graph which appears to be a Graph
Also modle implements 2 methods of searching through Graph
'''

class Graph:
    '''
    Graph class implements Graph as Graph
    '''
    weighted = False
    vert = {}
    w = {}
    def __init__(self, edges):
        for i in edges:
            s_0 = str(i[0]) #cmon man this is SNAKE CASE and IT SHLD BE respected
            s_1 = str(i[1]) #much better name than s0 and s1(which suck too but still)
            self.vert[s_0] = self.vert[s_0] + s_1 if self.vert.get(s_0) else s_1
            self.vert[s_1] = self.vert[s_1] + s_0 if self.vert.get(s_1) else s_0
            if len(i) > 2:
                self.weighted = True
                if not self.w.get(s_0):
                    self.w[s_0] = {}
                if not self.w.get(s_1):
                    self.w[s_1] = {}
                self.w[s_0][s_1] = int(i[2])
                self.w[s_1][s_0] = int(i[2])

    def __repr__(self):
        return str(self.vert) + (('\n' + str(self.w)) if self.weighted else '')

    def dfs(self):
        "deepth"
        visited = ''
        for i in self.vert:
            if not i in visited:
                print(i, end=' ')
                visited += i
            for j in self.vert[i]:
                if not j in visited:
                    print(j, end=' ')
                    visited += j


    def bfs(self):
        "broad"
        sup = 0
        for i in self.vert:
            sup = len(i) if len(i) > sup else sup
        for j in range(sup):
            for i in self.vert:
                print(i[j] if len(i) > j else '', end=' ')


if __name__ == '__main__':
    G = Graph(eval(input()))
    #[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [2, 6]]
    print(G)
    G.bfs()
    print()
    G.dfs()
    print()
