#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:18:19 2018

@author: paul
"""

from SolutionClass import Solution
from random import shuffle, randint

import numpy as np

def read_graph():
    return np.loadtxt("montreal", dtype='i', delimiter=',')

def initial_sol(graph, places):
    """
    Return a completed initial solution
    """
    s = Solution(places, graph)
    while len(s.not_visited[0:-1]) != 0:
        s.add(randint(0, len(s.not_visited)-2))
    s.add(0)
    
    return s
    
# tests    

graph = read_graph()

places = [1, 5, 9, 15, 2]

s = initial_sol(graph, places)

print("V = " + str(s.visited))
print("Cost = " + str(s.g))