#!/usr/bin/env python3

import sys
import math
from common import print_tour, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        index = len(tour)-1
        #print(index)
        switch_index = 0
        save_length = 0
        if index > 2:
            for i in range(index-3):
                length = dist[tour[i]][tour[i+1]] + dist[tour[index-1]][tour[index]]
                swiched_length = dist[tour[i]][tour[index-1]] + dist[tour[i+1]][tour[index]]
                if length - swiched_length > save_length:
                    save_length = length - swiched_length
                    switch_index  = i
            segment = tour[switch_index+1:index-1]    #reverse segment so it would be the shortest
            segment.reverse()
            tour[switch_index+1:index-1] = segment
        #print(tour)
        current_city = next_city

    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    #print_tour(tour)
