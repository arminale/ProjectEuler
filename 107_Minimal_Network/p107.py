# https://projecteuler.net/problem=107 Minimal Network
# I'll store the graph in an adjacency list. The i-th element of the list is the list of edges going out of vertex i.
# Each edge itself is a two element list in the form [destination_vertex, weight].
# I will then implement Prim's algorithm

def graph_weight_summer(graph):
    weight_sum = 0
    for vertex in graph:
        for edge in vertex:
            weight_sum += edge[1]
    # Since edges are non-directional, they are present twice in the adjacency list and are double counted
    return weight_sum/2



adj_list = []

with open("p107_network.txt", 'r') as input_file:
    i = 0
    for line in input_file:
        row = line.split(',')
        row[-1] = row[-1][:-1]
        adj_list += [[]]
        for j in range(len(row)):
            if row[j] != "-":
               adj_list[i] += [[j, int(row[j])]]
        i += 1


# start from vertex 0
minimal_adj_list = [[] for i in range(40)]
connected_vertices = [0]

while len(connected_vertices) != len(adj_list):
    min_edge = [0, 100000000]
    origin = 0
    for vertex in connected_vertices:
        for edge in adj_list[vertex]:
            if edge[0] not in connected_vertices and edge[1] < min_edge[1]:
                min_edge = edge
                origin = vertex

    minimal_adj_list[origin].append(min_edge)
    minimal_adj_list[min_edge[0]].append([origin, min_edge[1]])
    connected_vertices.append(min_edge[0])

print(graph_weight_summer(adj_list), graph_weight_summer(minimal_adj_list))
print("savings: ",graph_weight_summer(adj_list) - graph_weight_summer(minimal_adj_list) )