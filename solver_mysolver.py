#!/usr/bin/env python3

import sys

from common import print_tour, read_input
import solver_greedy as g
#question: i felt like it’s redundant to have the same function in different scripts, so
#          i imported from solver_greedy but now i feel like it's paying cost for the importing
#          so i wonder which is better


def dist_list(cities, tour, N):
    dist = [0 for _ in range (N)]
    for i in range (N):
        dist[i] = g.distance(cities[tour[i]],cities[tour[(i+1)%N]]) 
    return dist


def solve(cities):
    N = len(cities)
    tour = g.solve(cities)
    dist = dist_list(cities, tour, N)
    for i in range (1,N):                  # take two segments and compare with the switched order
        entry_dot = tour[i]                # when switching reverse entry_dot ~ exit_dot
        for j in range (i+1,N):
            exit_dot = tour[j]
            current_length = dist[i-1]+dist[j]
            switched_length = g.distance(cities[tour[i-1]],cities[tour[j]])+g.distance(cities[tour[i]],cities[tour[(j+1)%N]])
            if switched_length < current_length:
                segment = tour[i:j+1]
                segment.reverse()
                tour[i:j+1] = segment

    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    #print_tour(tour)
