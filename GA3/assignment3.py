from collections import deque

class edge:
    def __init__(self, weight, i, j):
        self.weight = weight
        self.i = i
        self.j = j

def check_cycle(adj_list, s):
    visited = set()

    queue = deque()
    queue.append(s)
    while (queue):
        v = queue.popleft()
        for neighbor in adj_list[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
            else:
                return True
    
    return False
        
def first_min_spanning_tree(edges, adj_list):
    min_spanning_tree = []
    for i in range(0, len(edges)):
        if (not check_cycle(adj_list, edges[i].i) and not check_cycle(adj_list, edges[i].j)):
            min_spanning_tree.append(edges[i])
    
    sum = 0
    for i in range(0, len(min_spanning_tree)):
        sum += min_spanning_tree[i].weight
    
    return sum

def three_min_spanning_trees(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        num_vertices = int(input_file.readline())
        
        # Reads file and turns it into an adjacency matrix
        adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

        for i in range(0, num_vertices):
            line = input_file.readline().split(",")
            adj_matrix[i] = [int(num) for num in line]
        
        print(adj_matrix)
    
    # Turn adjacency matrix into array of edge objects
    # Turn adjacency matrix into adjacency list
    edges = sorted(edges, key=lambda edge: edge.weight)
    
    # with open(output_file_path, 'w') as output_file:
    #     output_file.write(str())

    pass

three_min_spanning_trees('input2.txt', 'output')