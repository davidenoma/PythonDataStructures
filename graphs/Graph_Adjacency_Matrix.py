# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:03:50 2020

@author: kora
"""
class Graph:
    def __init__(self,numvertex):
        #The next line of code creates a numvertex * numvertex matrix
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices={} 
        self.verticeslist = [0]*numvertex
    def set_vertex(self,vtx,id):
        if 0 <= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id
    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost 
        #If we are created a directed graph, no need to add this section
        #This is because directed graph have a unidirectional cost
        self.adjMatrix[to][frm] = cost 
        
    def get_vertex(self):
        return self.verticeslist
    
    def get_edges(self):
        edges = [] 
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if(self.adjMatrix[i][j] != -1):
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
        return edges 
    def get_matrix(self):
        return self.adjMatrix
        
g = Graph(6)
g.set_vertex(0, 'a')
print(g.get_matrix())