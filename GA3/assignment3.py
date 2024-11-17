from collections import deque, defaultdict

class Edge:
    def __init__(self, node, neighbor, weight):
        self.node = node
        self.weight = weight
        self.neighbor = neighbor

class UnionFind:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)

        if self.rank[i_root] > self.rank[j_root]:
            self.parent[j_root] = i
        elif self.rank[i_root] < self.rank[j_root]:
            self.parent[i_root] = j_root
        else:
            self.parent[j_root] = i_root
            self.rank[i_root] += 1
        
def base_min_spanning_tree(edges, num_vertices, min_spanning_tree, uf):
    index_of_last_edge_added = 0

    for n in range(num_vertices-2):
        # check = check_cycle(adj_list, edge.node)
        # print(adj_list)
        
        i = uf.find(edges[n].node)
        j = uf.find(edges[n].neighbor)
        if i != j:
            min_spanning_tree.append(edges[n])
            index_of_last_edge_added = n
            uf.union(i, j)
    
    return index_of_last_edge_added

def find_min_spanning_tree(edges, index, uf):
    while index < len(edges):
        i = uf.find(edges[index].node)
        j = uf.find(edges[index].neighbor)
        if i != j:
            return index
        else:
            index += 1 

def three_min_spanning_trees(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        num_vertices = int(input_file.readline())

        # Reads file and turns it into an adjacency matrix
        adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

        for i in range(0, num_vertices):
            line = input_file.readline().split(",")
            adj_matrix[i] = [int(num) for num in line]
    
    # Turns adjacency matrix into array of edge objects
    edges = []
    for i in range(0, num_vertices-1):
        for j in range(i+1, num_vertices):         
            if adj_matrix[i][j] != 0:
                edges.append(Edge(i, j, adj_matrix[i][j]))
    
    # Sorts the edges
    edges = sorted(edges, key=lambda edge: edge.weight)

    min_spanning_tree = []
    uf = UnionFind(num_vertices)

    for node in range(num_vertices):
        uf.parent.append(node)
        uf.rank.append(0)
    index = base_min_spanning_tree(edges, num_vertices, min_spanning_tree, uf)

    sum = 0
    for edge in min_spanning_tree:
        sum += edge.weight

    print(sum)
    
    # with open(output_file_path, 'w') as output_file:
    #     output_file.write(str())

    pass

three_min_spanning_trees('input1.txt', 'output')