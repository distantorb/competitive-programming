from collections import defaultdict

# read from input
nb_edges = int(input())

# create a dictionary with the input gathered
g = defaultdict(dict)


# 3 is the number of edges of a graph and each edge is represented by 
# <departure> <arrival> <distance>, using defaultdict to initialise
# the new keys in an e mpty dictoinary, allowing the construction of
# the graph.

for _ in range(nb_edges):
    u, v, weight = input().split()
    g[u][v] = int(weight)
    
    for i, v in enumerate(g):
        print(i, v)
    # g[v][u] = int(weight) # for undirect graph

