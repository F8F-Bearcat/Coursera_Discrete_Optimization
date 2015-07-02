import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time
import pickle

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def make_rand_digraph(num_nodes, prob):
    '''
    Make a random directed graph
    Input: number of nodes, probability that an edge exists
    Output: A dictionary with keys as node numbers and values as sets of nodes pointed
    to by the key node
    Edge (i,j) is an edge going from node i to node j, head of edge at node j
    '''
    rand_graph_d = {}
    range_i = range(num_nodes)
    range_j = range(num_nodes)
    for ele in range_i:
        rand_graph_d[ele] = set([])     #initialize graph with values as empty sets for each node

    # generate the edges, iterate through i and j
    for eye in range_i:
        for jay in range_j:
            if eye != jay:
                if random.random() < prob:     # random.random() returns a float between 0 and 1
                    temp_set = rand_graph_d[eye]
                    temp_set = temp_set | set([jay])
                    rand_graph_d[eye] = temp_set

    return rand_graph_d

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order

def fast_targeted_order(ugraph):
    '''
    Input is an undirected graph
    Output is an ordered list of nodes in decreasing order of their degrees
    '''
    if ugraph == {}:
        return []
    #print 'ugraph is ', ugraph
    #print ' '
    # Note!! ugraph.copy() did not work, was mutated did not work !!!  I don't know why
    # switched over to the graph copy lines from the provided code
    # that worked, also don't know why...
    new_ugraph = copy_graph(ugraph)      # avoid mutating the input as nodes are removed
    node_count = len(new_ugraph)
    init = range(node_count)
    degree_sets = []
    for item in init:               # initialize list to all empty set entries
        degree_sets.append(set([]))
        #print 'internal loop degree_sets are ', degree_sets
    for item in ugraph:
        dee = len(new_ugraph[item])          # find the degree of each node and add to corresponding set
        degree_sets[dee] = degree_sets[dee] | set([item])
        #print 'internal loop degree_sets are ', degree_sets
    #print 'Initial degree_sets are ', degree_sets

    fast_target_order = []
    i = 0

    kay = init[node_count-1]
    while kay > -1:                            # bug in line below - was 'if' statement (one pass through), change to while
        while len(degree_sets[kay]) > 0:                       # for non empty sets there are nodes of degree k
            ewe = degree_sets[kay].pop()                    # pick one of the nodes of degree k, does not need to be random
            #ewe = random.choice(list(degree_sets[kay]))
            degree_sets[kay] = degree_sets[kay] - set([ewe])  # then remove that node
            neighbors_of_ewe = new_ugraph[ewe]                  # find all the neighbors of kay and decrement degree
            for element in neighbors_of_ewe:
                new_dee = len(new_ugraph[element])
                degree_sets[new_dee] -= set([element])      # remove element from degree d
                degree_sets[new_dee-1] |= set([element])    # add element to set of degree d-1, shifts element
            fast_target_order.append(ewe)
            #print 'degree sets following insertion into fast target order list (see next line) \n'
            #print 'degree sets are ', degree_sets
            i += 1                                          # using append means variable i is not needed
# now remove node ewe from the graph along with associated edges...
            delete_node = ewe
            delete_edges = new_ugraph[delete_node]
            if delete_node in new_ugraph:           # remove node from graph
                new_ugraph.pop(delete_node, None)   # using pop instead of del provides atomic operation
            for ele in delete_edges:                # remove all edges from removed node
                temp_set = new_ugraph[ele]
                temp_set.remove(delete_node)        # if statement needed? To make sure del node in set
                new_ugraph[ele] = temp_set
        kay -= 1

    return fast_target_order

def bfs_visited(ugraph, start_node):
    '''
    Input:  ugraph, an undirected graph.  start_node, to node to start the search for all
            connected nodes. Assume ugraph has no duplicate edges w no start/end on same node

    Output: a set of all the nodes visited by the algorithm
    '''
    if ugraph == {}:
        return set([])
    queue = deque()
    visited = set([start_node])
    queue.append(start_node)            # enter the queue from the right

    while len(queue) > 0:
        jay = queue.popleft()           # remove elements from the left
        neighbor_nodes = ugraph[jay]
        for element in neighbor_nodes:
            if element not in visited:
                visited = visited | set([element])
                queue.append(element)

    return visited

def cc_visited(ugraph):
    '''
    Input: undirected graph
    Output: list of sets, where each set is connected components in the graph
    '''
    conn_comp = []                       # note this is a list
    remaining_nodes = set([])            # init remaining_nodes w all the nodes in the input graph
    for element in ugraph:
        remaining_nodes = remaining_nodes | set([element])
    while len(remaining_nodes) > 0:
        node = remaining_nodes.pop()
        visited = bfs_visited(ugraph, node)
        conn_comp.append(visited)
        remaining_nodes -= visited
    return conn_comp

def largest_cc_size(ugraph):
    '''
    Input: undirected graph
    Output: an integer representing the size of the largest connected component in ugraph
    '''
    candidate_list = cc_visited(ugraph)
    max_cc_size = 0

    for item in candidate_list:
        if len(item) > max_cc_size:
            max_cc_size = len(item)
    return max_cc_size

def compute_resilience(ugraph, attack_order):
    '''
    Input: an undirected graph and a list of nodes to be removed in attack_order
    Output: a list of the largest connected component after each node is removed.
            the first entry in the list is the size of the original largest connected component
    '''
    new_attack = list(attack_order)             # input parameters cannot be mutated per the grader
    new_ugraph = ugraph.copy()                  # so make clean copies of ugraph and attack_order

    under_attack_largest_cc = []                # list to hold largest cc as nodes removed
    if new_ugraph == {}:                        # cover the empty graph input case
        return [0]
    largest = largest_cc_size(new_ugraph)       # save the value of largest cc prior to node removal
    under_attack_largest_cc.append(largest)

    while len(new_attack) > 0:                  # main proc section, delete nodes in attack vector
        delete_node = new_attack.pop(0)       # remove nodes to attack from the left
        delete_edges = new_ugraph[delete_node]
        if delete_node in new_ugraph:           # remove node from graph
            new_ugraph.pop(delete_node, None)   # using pop instead of del provides atomic operation
        for ele in delete_edges:                # remove all edges from removed node
            temp_set = new_ugraph[ele]
            temp_set.remove(delete_node)        # if statement needed? To make sure del node in set
            new_ugraph[ele] = temp_set
        largest_left = largest_cc_size(new_ugraph)
        under_attack_largest_cc.append(largest_left)

    return under_attack_largest_cc



EX_GRAPH0 = {0:set([1, 2]), 1:set([0]), 2:set([0])}
EX_GRAPH1 = {0:set([1, 3, 4, 5]), 1:set([0, 2, 4, 6]), 2:set([1, 3, 5]), 3:set([0, 2]), 4:set([0, 1]), 5:set([0, 2]), 6:set([1])}
EX_GRAPH2 = {0:set([1, 4, 5, 9]), 1:set([0, 2, 4, 6, 8]), 2:set([1, 3, 5, 7, 8]), 3:set([2, 7, 9]), 4:set([0, 1, 9]), 5:set([0, 2, 9]), 6:set([1, 9]), 7:set([2, 3, 9]), 8:set([1, 2]), 9:set([0, 3, 4, 5, 6, 7])}
EX_GRAPH3 = {}
EX_GRAPH4 = {0:set([]), 1:set([]), 2:set([]), 3:set([])}
EX_GRAPH5 = {0:set([2]), 1:set([3]), 2:set([0]), 3:set([1]), 4:set([5]), 5:set([4]), 6:set([7]), 7:set([6])}
EX_GRAPH6 = {0:set([1, 3]), 1:set([0]), 2:set([5]), 3:set([0]), 4:set([]), 5:set([2])}

# get er graph
pick = open('C:\Users\\andyd\Documents\GitHub\Coursera_Discrete_Optimization\er_graph.p', 'rb')
er_graph = pickle.load(pick)
pick.close()

# get provided graph
pick = open('C:\Users\\andyd\Desktop\provided_graph.p', 'rb')
provided_graph = pickle.load(pick)
pick.close()

'''
# get provided graph
pick = open('C:\Users\\andyd\Documents\GitHub\Coursera_Discrete_Optimization\provided_graph.p', 'rb')
pick.close()

pick = open('C:\Users\\andyd\Documents\GitHub\Coursera_Discrete_Optimization\upa_graph.p', 'rb')
provided_graph = pickle.load(pick)
upa_graph = pickle.load(pick)
pick.close()
'''
#print 'er_graph is ', er_graph
#print ' '

deg_dict = {}
node_count = 0
edge_count = 0
for ele in er_graph:
    node_count += 1
    edge_count += len(er_graph[ele])/2.0
    if len(er_graph[ele]) not in deg_dict:
        deg_dict[len(er_graph[ele])] = 1
    else:
        deg_dict[len(er_graph[ele])] += 1

#print 'node_count is ', node_count
#print 'edge_count is ', edge_count
#print 'deg_dict is ', deg_dict
#print ' '

prioritized_attack = fast_targeted_order(er_graph)
#print 'prioritized attack is ', prioritized_attack
largest_cc = compute_resilience(er_graph, prioritized_attack)
#print 'largest cc is ', largest_cc

provided_attack = fast_targeted_order(provided_graph)
largest_cc_provided = compute_resilience(provided_graph, provided_attack)

xvals = range(len(largest_cc))
yvals1 = largest_cc
yvals2 = largest_cc_provided
#yvals3 = Provided_values
#yvals2 = [1, 4, 9, 16, 25]

#print 'xvals are ', xvals
#print 'yvals1 are ', yvals1

plt.plot(xvals, yvals1, '-b', label='ER Targeted Attack')
plt.plot(xvals, yvals2, '-r', label='Computer Network (Provided) Targeted Attack')
#plt.plot(xvals, yvals3, '-g', label='Provided Computer Network')
plt.legend(loc='upper right')
plt.ylabel('Largest Connected Component in the Graph')
plt.xlabel('Number of Nodes Removed')
plt.title('Reliliance of Graphs under Targeted Attack')
plt.show()

