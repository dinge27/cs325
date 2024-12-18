from collections import defaultdict

neg = '~'


# directed graph class
#  adapted from:
#  src: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
class dir_graph:
    def __init__(self):
        # create an empty directed graph, represented by a dictionary
        #  The dictionary consists of keys and corresponding lists
        #  Key = node u , List = nodes, v, such that (u,v) is an edge
        self.graph = defaultdict(set)
        self.nodes = set()

    # Function that adds an edge (u,v) to the graph
    #  It finds the dictionary entry for node u and appends node v to its list
    # performance: O(1)
    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.nodes.add(u)
        self.nodes.add(v)

    # Function that outputs the edges of all nodes in the graph
    #  prints all (u,v) in the set of edges of the graoh
    # performance: O(m+n) m = #edges , n = #nodes
    def print(self):
        edges = []
        # for each node in graph
        for node in self.graph:
            # for each neighbour node of a single node
            for neighbour in self.graph[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        return edges


# 2-CNF class
#  Class storing a boolean formula in Conjunctive Normal Form of literals
#  where the size of clauses is at most 2
#  -NOTATION-
#    The CNF is represented as a list of lists
#    e.g [[x, y], [k, z]] == (x or y) and (k or z)
#    i.e Conjunction of inner lists , where the inner lists are disjunctions
#    of literals
#    Negation is represented with ~ .  ~x == negation of literal x
# class two_cnf:
class two_cnf:
    def __init__(self):
        self.con = []

    # adds a clause to the CNF
    # performance O(1)
    def add_clause(self, clause):
        if len(clause) <= 2:
            self.con.append(clause)
        else:
            print("error: clause contains > 2 literals")

    # returns a set of all the variables in the CNF formula
    def get_variables(self):
        vars = set()
        for clause in self.con:
            for literal in clause:
                vars.add(literal)
        return vars

    def print(self):
        print(self.con)


# helper function that applies the double negation rule to a formula
#   the function removes all occurrences ~~ from the formula
def double_neg(formula):
    return formula.replace((neg+neg), '')


# Function that performs Depth First Search on a directed graph
# O(|V|+|E|)
def DFS(dir_graph, visited, stack, scc):
    for node in dir_graph.nodes:
        if node not in visited:
            explore(dir_graph, visited, node, stack, scc)


# DFS helper function that 'explores' as far as possible from a node
def explore(dir_graph, visited, node, stack, scc):
    if node not in visited:
        visited.append(node)
        for neighbour in dir_graph.graph[node]:
            explore(dir_graph, visited, neighbour, stack, scc)
        stack.append(node)
        scc.append(node)
    return visited


# Function that generates the transpose of a given directed graph
# Performance O(|V|+|E|)
def transpose_graph(d_graph):
    t_graph = dir_graph()
    # for each node in graph
    for node in d_graph.graph:
        # for each neighbour node of a single node
        for neighbour in d_graph.graph[node]:
            t_graph.addEdge(neighbour, node)
    return t_graph


# Function that finds all the strongly connected components in a given graph
# Implementation of Kosaraju’s algorithm
# Performance O(|V|+|E|) for a directed graph G=(V,E)
# IN : directed graph, G
# OUT: list of lists containing the strongly connected components of G
def strongly_connected_components(dir_graph):
    stack = []
    sccs = []
    DFS(dir_graph, [], stack, [])
    t_g = transpose_graph(dir_graph)
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            scc.append(node)
            explore(t_g, visited, node, [], scc)
            sccs.append(scc)
    return sccs


# Function that finds a contradiction in a list of strong connected components
# if [a , b , ~a,  c, a] is a connected component then the function returns T
# since a -> ~a -> a exists
# sccs = Strongly Connected Components
#   It is a list of lists representing the connected components
def find_contradiction(sccs):
    for component in sccs:
        for literal in component:
            for other_literal in component[component.index(literal):]:
                if other_literal == double_neg(neg + literal):
                    return True
    return False


# Function that determines if a given 2-CNF is Satisfiable or not
def two_sat_solver(two_cnf_formula):
    # print("Checking if the following 2-CNF is Satisfiable in linear time ")
    # two_cnf_formula.print()

    # setup the edges of the graph
    # G = (V,E) , V = L U ~L where L = set of variables in 2-CNF
    # E =
    # {(~u,v),(~v,u) | for all clauses [u,v] } U {(~u,u) | for all clauses [u]}
    graph = dir_graph()
    for clause in two_cnf_formula.con:
        if len(clause) == 2:
            u = clause[0]
            v = clause[1]
            graph.addEdge(double_neg(neg+u), v)
            graph.addEdge(double_neg(neg+v), u)
        else:
            graph.addEdge(double_neg(neg+clause[0]), clause[0])
    if not find_contradiction(strongly_connected_components(graph)):
        #print("2-CNF Satisfiable")
        return True
    else:
        #print("2-CNF not Satisfiable")
        return False


# [a, b, a, c, ~b, d]
# ======= 2-CNF setup =======
# formula = two_cnf()
# formula.add_clause(['a', 'b'])
# formula.add_clause(['~a', 'b'])
# formula.add_clause(['a', '~b'])
# formula.add_clause(['~a', '~b'])
#two_sat_solver(formula)

'''
This file contains the template for Assignment4. For testing it, I will place
it
in a different directory, call the function <can_turn_off_lights>,
and check its output. So, you can add/remove whatever you want to/from this
file. But,
don't change the name of the file or the name/signature of the following
function.
Also, I will use <python3> to run this code.
'''

# START OF WRITTEN CODE
def iteration(input_file):
    # Setup for all the variables read from file
    skip_line = input_file.readline()
    num_line = input_file.readline().split(',')

    num_switches = int(num_line[0])
    num_lights = int(num_line[1])
    
    light_states = input_file.readline().split(',')
    light_states = list(map(int, light_states))

    lights = [[0 for i in range(0)] for j in range(num_lights)]

    # Creates an array of lights where each index stores 2 switches the light is connected to
    for i in range(num_switches):
        line = input_file.readline().split(',')

        for light in line:
            lights[int(light)-1].append(i)
    
    # Start runtime analysis here
    formula = two_cnf()
    
    #print(lights)

    for i in range(num_lights):
        lights[i] = list(map(str, lights[i]))
        #print(lights[i])

        if light_states[i] == 1:
            formula.add_clause([lights[i][0], lights[i][1]])
            formula.add_clause(['~' + lights[i][0], '~' + lights[i][1]])
        else:
            formula.add_clause(['~' + lights[i][0], lights[i][1]])
            formula.add_clause([lights[i][0], '~' + lights[i][1]])
    
    if (two_sat_solver(formula)):
        return "yes"
    else:
        return "no"


def can_turn_off_lights(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        output1 = iteration(input_file)
        output2 = iteration(input_file)

    # print(output1)
    # print(output2)

    with open(output_file_path, 'w') as output_file:
        output_file.write(output1 + '\n')
        output_file.write(output2)

'''
This function will contain your code. It wil read from the file
<input_file_path>,
and will write its output to the file <output_file_path>.
'''
pass
'''
To test your function, you can uncomment the following command with the the
input/output
files paths that you want to read from/write to.
'''
#can_turn_off_lights('input2.txt', 'output.txt')

