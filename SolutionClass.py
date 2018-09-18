#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:28:49 2018

@author: paul
"""

import copy

class Solution:
    def __init__(self, places, graph):
        """
        places: a list containing the indices of attractions to visit
        p1 = places[0]
        pm = places[-1]
        """
        self.g = 0 # current cost
        self.graph = graph 
        self.visited = [places[0]] # list of already visited attractions
        self.not_visited = copy.deepcopy(places[1:]) # list of attractions not yet visited
        
    def add(self, idx):
        """
        Adds the point in position idx of not_visited list to the solution
        """
        self.g += self.graph[self.visited[-1], self.not_visited[idx]]
        self.visited.append(self.not_visited[idx])
        del self.not_visited[idx]
        
    def swap(self, i, j): # permute la position de deux noeuds dans la solution
        # i et j ne doivent pas etre egaux a 0 ou a len(s.visited)
        # on met a jour le cout total
        # indice i
        if i != j:
            self.g -= self.graph[self.visited[i-1],self.visited[i]] + self.graph[self.visited[i],self.visited[i+1]]
            self.g += self.graph[self.visited[i-1],self.visited[j]] + self.graph[self.visited[j],self.visited[i+1]]
            # indice j
            self.g -= self.graph[self.visited[j-1],self.visited[j]] + self.graph[self.visited[j],self.visited[j+1]]
            self.g += self.graph[self.visited[j-1],self.visited[i]] + self.graph[self.visited[i],self.visited[j+1]]
            # on permute les elements
            self.visited[i], self.visited[j] = self.visited[j], self.visited[i]
        
            
            
        
        