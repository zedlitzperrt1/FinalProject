from Weighted_Graph import *
from functions import *

#edge_file_name should be a string
def Prims(edge_file_name, start_vertex, draw):
    cost = 0
    T = ({start_vertex},[])
    G = Weighted_Graph(edge_file_name)
    while T[0] != G.vertex_set():
        update(T,G)
        if draw == True:
            plt.clf()
            G.draw_subgraph(T)
    for e in T[1]:
        cost += C(e, G)
    return cost

def Prims_step(T,edge_file_name, start_vertex):
    cost = 0
    G = Weighted_Graph(edge_file_name)
    if T[0] != G.vertex_set():
        T = update(T,G)
        plt.clf()
        G.draw_subgraph(T)
    for e in T[1]:
        cost += C(e, G)
    return cost
#cost is the sum of the weight of edges in the Tree        
#    return Cost(T)
       
"""
def update(T,G):
    plt.clf()
    if len(T[0]) < len(G.vertex_set()):
        e = min_incident_edge(T,G)
        if e not in T[1]:
            T[0].add(e[0])
            T[0].add(e[1])
            T[1].append(e)
            G.draw_subgraph(T)
    return T

"""