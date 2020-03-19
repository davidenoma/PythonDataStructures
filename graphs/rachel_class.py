# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:49:22 2020

@author: kora
"""
# import array as arr
# arr.array()
vertices = ["v1","v2","v3","v4","v5","v6","v7"]
mtrxsize = len(vertices)+ 1
matrix = [[0]*mtrxsize for x in range(mtrxsize)]
i =1
#Filling in the columns
for ln in vertices:    
    matrix[0][i] = ln
    i = i+1
i = 1
# Filling in the rows
for ln in vertices:
    matrix[i][0] = ln 
    i = i+1
#Dictionary of vertices
vtxids = {}
i = 1
for v in vertices:
    vtxids[i] = v
    i+=1   

def addEdge(frm,to,weight):
    matrix[frm][to] = weight
    
addEdge(1,2,2)   
addEdge(1,4,1) 
addEdge(2,4,3)
addEdge(2,5,10)
addEdge(3,1,4)
addEdge(3,6,5)
addEdge(4,5,2)
addEdge(4,3,2)
addEdge(4,6,8)
addEdge(4,7,4)
addEdge(5, 7, 6)


print(matrix)



