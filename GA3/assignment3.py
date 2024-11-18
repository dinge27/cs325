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
        
        if i_root == j_root:
            return False

        if self.rank[i_root] > self.rank[j_root]:
            self.parent[j_root] = i
        elif self.rank[i_root] < self.rank[j_root]:
            self.parent[i_root] = j_root
        else:
            self.parent[j_root] = i_root
            self.rank[i_root] += 1

        return True
        
def kruskal(edges, num_vertices, min_spanning_tree):
    uf = UnionFind(num_vertices)

    sum = 0
    for edge in edges:
        if uf.union(edge.node, edge.neighbor):
            min_spanning_tree.append(edge)
            sum += edge.weight
    
    return sum

def find_min_spanning_trees(edges, num_vertices, min_spanning_tree):
    second_sum = float('inf')
    third_sum = float('inf')

    for edge_remove in min_spanning_tree:
        uf = UnionFind(num_vertices)
        sum = 0
        
        for edge in edges:
            if edge == edge_remove:
                continue

            if uf.union(edge.node, edge.neighbor):
                sum += edge.weight

        if sum <= second_sum:
            third_sum = second_sum
            second_sum = sum

    return second_sum, third_sum

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

    sum1 = kruskal(edges, num_vertices, min_spanning_tree)

    sum2, sum3 = find_min_spanning_trees(edges, num_vertices, min_spanning_tree)
    
    print(sum1, sum2, sum3)
    
    # with open(output_file_path, 'w') as output_file:
    #     output_file.write(str())

    pass

three_min_spanning_trees('input2.txt', 'output')