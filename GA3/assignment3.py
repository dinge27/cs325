from collections import deque, defaultdict

class Edge:
    def __init__(self, node, neighbor, weight):
        self.node = node
        self.weight = weight
        self.neighbor = neighbor

class UnionFind:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))

def check_cycle(adj_list, s, new_edge):
    new_adj_list = adj_list.copy()
    new_adj_list[new_edge.node].append(new_edge)

    visited = set()
    queue = deque([(s, None)])

    visited.add(s)
    while (queue):
        #print(visited, queue)

        v, parent = queue.popleft()

        for neighbor in new_adj_list[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, v))
            elif neighbor != parent:
                #print(neighbor, parent)
                return True
    
    return False
        
def first_min_spanning_tree(edges):
    adj_list = defaultdict(list)
    min_spanning_tree = set()
    for edge in edges:
        # check = check_cycle(adj_list, edge.node)
        # print(adj_list)
        if (not check_cycle(adj_list, edge.node, edge) and not check_cycle(adj_list, edge.neighbor, edge)):
            min_spanning_tree.add(edge)
            adj_list[edge.node].append(edge)
    
    sum = 0
    for edge in min_spanning_tree:
        sum += edge.weight
    
    return sum

def three_min_spanning_trees(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        num_vertices = int(input_file.readline())

        # Reads file and turns it into an adjacency matrix
        adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

        for i in range(0, num_vertices):
            line = input_file.readline().split(",")
            adj_matrix[i] = [int(num) for num in line]
    
    # Turns adjacency matrix into array of edge objects
    edges = set()
    for i in range(0, num_vertices-1):
        for j in range(i+1, num_vertices):         
            if adj_matrix[i][j] != 0:
                edges.add(Edge(i, j, adj_matrix[i][j]))
    
    
    for edge in edges:
        print(edge.node, edge.neighbor)
    
    # Sorts the edges
    edges = sorted(edges, key=lambda edge: edge.weight)

    first = first_min_spanning_tree(edges)

    print(first)
    
    # with open(output_file_path, 'w') as output_file:
    #     output_file.write(str())

    pass

three_min_spanning_trees('input1.txt', 'output')