from Weighted_Graph import *
#G = Weighted_Graph('test_graph.txt')
#G.draw_graph()
#print(G.edge_set())
#print(G.vertex_set())
#print(G.edge_dict())
#H = ({0,1,3}, [(0,1),(1,3)])
#G.draw_subgraph(H)

#COST of graph e with respect to graph G
def C(e, G):
    return G.edge_dict()[e]
#check function
#print (C((1,4),G))
#T = ({0},[])
#T = ({2,3},[(2,3)])
#T = [{2,3,5}, [(2,3),(2,5)]]
#For TREE T with respect to graph G
    
"""Find all incident edges that do not form a cycle with our tree"""
def valid_incident_edges(T, G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e and e not in T[1] and e not in edges:
                edges.append(e)
    for e in edges:
        if e[0] and e[1] in T[0]:
            edges.remove(e)
    return edges

#edges = valid_incident_edges(T,G)
#print(T)
#print(edges)
#G.draw_subgraph(T)
#draw incident edges
#G.draw_subgraph((T[0],edges))

def min_incident_edge(T, G):
    edges = valid_incident_edges(T,G)
    min_edge = edges[0]
    min_weight = C(edges[0],G)
    for e in edges:
        this_weight = C(e,G)
        if this_weight < min_weight:
            min_edge = e
            min_weight = this_weight
    return min_edge

#print(min_incident_edge(T, G))

"""If the next minimum incident edge is not already in our Tree, update the 
Tree to include it"""
def update(T,G):
    e = min_incident_edge(T,G)
    if e not in T[1]:
        T[0].add(e[0])
        T[0].add(e[1])
        T[1].append(e)
    return T

