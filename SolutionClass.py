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
        
    def __str__(self):
        return "v = " + str(self.visited) + "   " + "g = " + str(self.g)
        
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
        if i>j:
            i, j = j, i
        
        p_im1 = self.visited[i-1]
        p_ip1 = self.visited[i+1]
        p_i = self.visited[i]
        
        p_jm1 = self.visited[j-1]

        try:
            p_jp1 = self.visited[j+1]
        except:
            print("exception")
            print(j)
            print(len(self.visited))
            
        p_j = self.visited[j]
        # on doit differencier le cas ou i+1 = j
        
        # on retire les couts initiaux
        self.g -= self.graph[p_im1,p_i] + self.graph[p_i,p_ip1]
        self.g -= self.graph[p_jm1,p_j] + self.graph[p_j,p_jp1]
        
        if i+1 == j:
            self.g += self.graph[p_i,p_ip1]
        
        # on permute les elements
        self.visited[i], self.visited[j] = self.visited[j], self.visited[i]
        
        # on somme les couts des nouveaux chemins
        p_im1 = self.visited[i-1]
        p_ip1 = self.visited[i+1]
        p_i = self.visited[i]
        
        p_jm1 = self.visited[j-1]
        p_jp1 = self.visited[j+1]
        p_j = self.visited[j]
        
        self.g += self.graph[p_im1,p_i] + self.graph[p_i,p_ip1] + self.graph[p_jm1,p_j] + self.graph[p_j,p_jp1]
        
        if i+1 == j:
            self.g -= self.graph[p_i,p_ip1]
        
            
            
        
        