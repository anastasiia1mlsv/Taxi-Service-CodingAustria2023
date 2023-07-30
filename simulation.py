import copy
import itertools
import numpy as np
import random

from itertools import permutations

def dijkstra(src, dest, nodes, edges, parameter):

    dist = {n: 1e7 for n in nodes}
    dist[src] = 0
    visited = {n: False for n in nodes}
    prev = {n: '' for n in nodes}
    
    current = copy.copy(src)
    visited[current] = True
    
    while not visited[dest]:
        
        finished = False
    
        neighbours = [edges[i] for i in range(len(edges)) if current in edges[i]['Nodes']]

        for i in range(len(neighbours)):
            if neighbours[i]['Nodes'][0] == current:
                name = neighbours[i]['Nodes'][1]
            else:
                name = neighbours[i]['Nodes'][0]
            
            if not visited[name]:
                if neighbours[i][parameter]+dist[current] < dist[name]:
                    dist[name] = neighbours[i][parameter]+dist[current]
                    prev[name] = current
              
        visited[current] = True
        
        min_dist = 1e5
        
        if not visited[dest]:

            for n in nodes:
                if not visited[n]:
                    if dist[n] < min_dist:
                        min_dist = dist[n]
                        current = n
                                 
    path = []
    
    while prev[current] != '':
        path.append(current)
        current = prev[current]
        
    path.reverse()
        
        
    return path, dist[dest]

def loss(cars, nodes, edges):
    
    total_dist = 0
    
    for car in cars:
        
        for path in car['paths']:
            
            _, dist = dijkstra(path[0], path[1], nodes, edges, 'Distance')
            
            total_dist += dist
            
    return total_dist

def get_all_permutations(source):
    all_permutations = list(permutations(source))
    return [list(perm) for perm in all_permutations]

def get_all_possible_combinations(source):
    
    state = [[el] for el in source]
    res = [state]
    premutations_res = []

    def loop(state):
        for i in range(len(state) - 1):     
            new_state = state[:-1].copy()
            new_state[i] = new_state[i] + state[-1]
            if len(new_state) == 1:
                res.append(new_state)
                continue
            res.append(new_state)
            loop(new_state)
    
    loop(state)

    for state in res:
        for i in range(len(state)):
            if len(state[i]) > 1:
                perms = get_all_permutations(state[i])
                for perm in perms:
                    new_state = state.copy()
                    new_state[i] = perm
                    premutations_res += [new_state]
                
    
    return res + premutations_res

def spawn_passengers(nodes):
    
    ps = []
    
    for i in range(len(nodes)):
        ps.append({'Name': 'P' + str(i), 'Start': 'a'})
        p_f = random.choice(nodes)
        while p_f == ps[-1]['Start']:
            p_f = random.choice(nodes)
        ps[-1]['Target'] = p_f
        
    return ps

def generate_optimal_paths(ps, nodes, edges):
    
    inds = list(range(len(ps)))
    
    possible_combinations = get_all_possible_combinations(inds)
    
    min_path = 1e10
    
    possible_cars = []
    
    for comb in possible_combinations:
        
        cars = []
        
        for car in comb:
            
            car = list(car)
            
            car1 = {}
            
            car1['passengers'] = [ps[p]['Name'] for p in car]
            
            end_dests = list([ps[p]['Target'] for p in car])
            
            car1['paths'] = []
            
            start_pos = ps[0]['Start']
            
            for i in range(len(end_dests)):
                
                e = end_dests[i]
                
                car1['paths'].append([start_pos, e])
                
                start_pos = copy.copy(e)
                
            cars.append(car1)
        
        l = loss(cars, nodes, edges)
        
#         print(comb, '\n', cars, l, '\n')
        
        if l < min_path:
            min_path = l
            optimal_paths = cars
            
    return optimal_paths