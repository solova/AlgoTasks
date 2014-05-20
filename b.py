import sys
from collections import defaultdict
from heapq import *

#It's a classic Dijkstra algo problem

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
 
    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return cost
 
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))
 
    return float("inf")

def solve():
    cities = []
    edges = []
    n = int(raw_input())
    for _n in xrange(n):
        city = sys.stdin.readline().strip()
        p = int(raw_input())
        cities.append(city)
        for _p in xrange(p):
            nr, cost = map(int, sys.stdin.readline().strip().split())
            edges.append((_n, nr-1, cost))
    r = int(raw_input())
    for _r in xrange(r):
        city1, city2 = sys.stdin.readline().strip().split()
        index1, index2 = cities.index(city1), cities.index(city2)
        print dijkstra(edges, index1, index2)
    
s = int(raw_input())
for _s in xrange(s):
    if _s>0: #skip a line between tests
        sys.stdin.readline()
        print
    solve()
