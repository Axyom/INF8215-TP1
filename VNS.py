#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:18:19 2018

@author: paul
"""

from SolutionClass import Solution
from random import shuffle, randint, choice
import copy
import time

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

def shaking(sol, k):
    """
    Returns a solution on the k-th neighrboohood of sol
    """
    s = copy.deepcopy(sol)
    
    for kk in range(k):
        i = randint(1, len(s.visited)-2)
        j = choice([x for x in range(1,len(s.visited)-1) if x != i])
        s.swap(i,j)
        
    return s;

def local_search_2opt(sol):
    """
    Apply 2-opt local search over sol
    """
    # indices = [(i,j) for (i,j) in (sol.visited[1:-1],sol.visited[1:-1]) if i+1<j and j<len(sol.visited)-1]
    
    sol_opt_local = sol
    
    for i in range(1,len(sol.visited)-3):
        for j in range(i+2,len(sol.visited)-1):
            s = copy.deepcopy(sol)
            # on swappe deux aretes
            s.swap(i,j)
            if s.g < sol_opt_local.g:
                sol_opt_local = s
            
    return sol_opt_local

def vns(sol, k_max, t_max):
    """
    Performs the VNS algorithm
    """
    start_time = time.time()
    
    while time.time() - start_time < t_max:
        k = 1
        while k < k_max:
            # on genere au hasard une solution dans
            # le voisinage d'ordre k autour de la solution
            # courante
            s = shaking(sol,k)
            # on trouve un optimum local 
            s = local_search_2opt(s)
            if s.g < sol.g:
                sol = s
            else:
                k = k+1
                
    return sol
    
# tests    

graph = read_graph()

# test 1  --------------  OPT. SOL. = 27
places=[0, 5, 13, 16, 6, 9, 4]
sol = initial_sol(graph=graph, places=places)
print(sol.g)

start_time = time.time()
vns_sol = vns(sol=sol, k_max=10, t_max=1)
print(vns_sol.g)
print(vns_sol.visited)
print("--- %s seconds ---" % (time.time() - start_time))

#test 2  --------------  OPT. SOL. = 30
places=[0, 1, 4, 9, 20, 18, 16, 5, 13, 19]
sol = initial_sol(graph=graph, places=places)
print(sol.g)

start_time = time.time()
vns_sol = vns(sol=sol, k_max=10, t_max=1)
print(vns_sol.g)
print(vns_sol.visited)

print("--- %s seconds ---" % (time.time() - start_time))

# test 3  --------------  OPT. SOL. = 26
places=[0, 2, 7, 13, 11, 16, 15, 7, 9, 8, 4]
sol = initial_sol(graph=graph, places=places)
print(sol.g)

start_time = time.time()
vns_sol = vns(sol=sol, k_max=10, t_max=1)
print(vns_sol.g)
print(vns_sol.visited)
print("--- %s seconds ---" % (time.time() - start_time))

# test 4  --------------  OPT. SOL. = 40
places=[0, 2, 20, 3, 18, 12, 13, 5, 11, 16, 15, 4, 9, 14, 1]
sol = initial_sol(graph=graph, places=places)
print(sol.g)

start_time = time.time()
vns_sol = vns(sol=sol, k_max=10, t_max=1)
print(vns_sol.g)
print(vns_sol.visited)
print("--- %s seconds ---" % (time.time() - start_time))