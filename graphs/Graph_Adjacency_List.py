# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:49:29 2020

@author: kora
"""

class Vertex:
    def __init__(self,data):
        self.vertex = data 
        self.next = None

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None] * self.V
    
    def add_edge(self,src,dest):
        #addition of the Node to the source node
        node = Vertex(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        
        #Adding the source node to the destination as it is undirected 
        node = Vertex(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
        
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency List of Vertex {}\n head".format(i),end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex),end="")
                temp = temp.next 
            print(" \n")

g = Graph(7)
                
        