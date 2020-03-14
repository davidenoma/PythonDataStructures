# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:51:29 2020

@author: kora
"""
#Implementation of a Graph using an Adjacency List
from Vertex import Vertex
class Graph:
    
    def __init__(self):
       self.vertList = {}
       self.numVertices = 0 
       
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None 
        
    def addEdge(self,f,t,cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor (self.vertList[t],cost)
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self,n):
        return n in self.vertList
g = Graph()