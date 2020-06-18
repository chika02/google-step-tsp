#!/usr/bin/env python3

import sys
import math
from common import print_tour, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    #store all the distance between nodes
    dist = [[0] * (N+1) for i in range(N+1)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    for i in range(N+1):
        dist[N][i] = dist[0][i]
        dist[i][N] = dist[i][0]

    current_city = 0
    unvisited_cities = list(range(1, N))
    tour = [current_city]

    while unvisited_cities:

        #append the next closest city to the tour list
        next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)

        #consider switching the new segment with the already drawn segment.
        #compare with all the segments
        #if you can get shorter distance by switching, reverse all the cities in between (switch_point+1 ~ new_city-1).
        new_city = len(tour)-1
        switch_point = -1
        save_length = -1
        if new_city > 2:
            for i in range(new_city-2):
                length = dist[tour[i]][tour[(i+1)]] + dist[tour[new_city-1]][tour[new_city]]
                switched_length = dist[tour[i]][tour[new_city-1]] + dist[tour[i+1]][tour[new_city]]
                if (length - switched_length) > save_length:
                    save_length = length - switched_length
                    switch_point  = i
            if switch_point != -1:
                segment = tour[switch_point+1:new_city]
                segment.reverse()
                tour[switch_point+1:new_city] = segment
        current_city = next_city
        if current_city == N-1:
            unvisited_cities.append(N)
    tour = tour[:N]
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
