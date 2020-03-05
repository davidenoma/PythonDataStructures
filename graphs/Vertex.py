# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:46:12 2020

@author: kora
"""

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    def __str__(self):
        
        return 'Id is: '+str(self.id) + ' & connected to: ' + str([x.id for x in self.connectedTo])

    