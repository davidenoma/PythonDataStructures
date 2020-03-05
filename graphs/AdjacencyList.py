# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:46:12 2020

@author: kora
"""
from Graph import Graph
from Vertex import Vertex

g = Graph()
for i in range(6):
    g.addVertex(i)



g.addEdge(0,1,2)
for vertex in g:
    print (vertex) 
    print(vertex.getConnections()) 
    