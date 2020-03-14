# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:38:18 2020

@author: kora
"""
from Stack import Stack
from Queue import Queue
from Graph import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    
    wfile = open(wordFile,'r')
    
    for line in wfile:
        print(line)
        word = line[:-1]
        print(word)
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
                
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
    