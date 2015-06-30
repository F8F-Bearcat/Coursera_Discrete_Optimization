import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time
import pickle
import cProfile

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
    for item in init:
        dee = len(new_ugraph[item])          # find the degree of each node and add to corresponding set
        degree_sets[dee] = degree_sets[dee] | set([item])
        #print 'internal loop degree_sets are ', degree_sets
    #print 'degree_sets are ', degree_sets

    target_order = []
    i = 0

    kay = init[node_count-1]
    while kay > -1:
        if len(degree_sets[kay]) > 0:                       # for non empty sets there are nodes of degree k
            ewe = degree_sets[kay].pop()                    # pick one of the nodes of degree k, does not need to be random
            #ewe = random.choice(list(degree_sets[kay]))
            degree_sets[kay] = degree_sets[kay] - set([ewe])  # then remove that node
            neighbors_of_ewe = new_ugraph[ewe]                  # find all the neighbors of kay and decrement degree
            for element in neighbors_of_ewe:
                new_dee = len(new_ugraph[element])
                degree_sets[new_dee] -= set([element])      # remove element from degree d
                degree_sets[new_dee-1] |= set([element])    # add element to set of degree d-1, shifts element
            target_order.append(ewe)
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

    return target_order

EX_GRAPH0 = {0:set([1, 2]), 1:set([0]), 2:set([0])}
EX_GRAPH1 = {0:set([1, 3, 4, 5]), 1:set([0, 2, 4, 6]), 2:set([1, 3, 5]), 3:set([0, 2]), 4:set([0, 1]), 5:set([0, 2]), 6:set([1])}
EX_GRAPH2 = {0:set([1, 4, 5, 9]), 1:set([0, 2, 4, 6, 8]), 2:set([1, 3, 5, 7, 8]), 3:set([2, 7, 9]), 4:set([0, 1, 9]), 5:set([0, 2, 9]), 6:set([1, 9]), 7:set([2, 3, 9]), 8:set([1, 2]), 9:set([0, 3, 4, 5, 6, 7])}
EX_GRAPH3 = {}
EX_GRAPH4 = {0:set([]), 1:set([]), 2:set([]), 3:set([])}
EX_GRAPH5 = {0:set([2]), 1:set([3]), 2:set([0]), 3:set([1]), 4:set([5]), 5:set([4]), 6:set([7]), 7:set([6])}
EX_GRAPH6 = {0:set([1, 3]), 1:set([0]), 2:set([5]), 3:set([0]), 4:set([]), 5:set([2])}

# print fast_targeted_order(EX_GRAPH1)

pick = open('C:\Users\\andyd\Documents\GitHub\Coursera_Discrete_Optimization\Targeted_order_times.p', 'rb')
upa_targeted_order_times = pickle.load(pick)
pick.close()

pick = open('C:\Users\\andyd\Desktop\er_graph.p', 'rb')    # gather er_graph
er_graph = pickle.load(pick)    
pick.close()

pick = open('C:\Users\\andyd\Documents\GitHub\Coursera_Discrete_Optimization\er_graph.p', 'wb')
pickle.dump(er_graph, pick)
pick.close()

# create UPA graph of same size

    #print 'element is ', element
upa_graph = make_rand_digraph(5, 1)

# initialize helper object
helper_g = UPATrial(5)
#enn = 10
add_nodes = range(5, 1239)
for atom in add_nodes:
    upa_graph[atom] = set([])       # add all nodes and initialize to empty set

for item in add_nodes:
    edges = helper_g.run_trial(3)
    for iota in edges:
        #print 'edges are ', edges
        upa_graph[item] = upa_graph[item] | set([iota])         # likely the issue with upa graphs is here
        upa_graph[iota] = upa_graph[iota] | set([item])

pick = open('C:\Users\Dad\Documents\GitHub\Coursera_Discrete_Optimization\upa_graph.p', 'wb')
pickle.dump(upa_graph, pick)
pick.close()

# get provided graph
pick = open('C:\Users\Dad\Desktop\provided_graph.p', 'rb')
provided_graph = pickle.load(pick)
pick.close()

pick = open('C:\Users\Dad\Documents\GitHub\Coursera_Discrete_Optimization\provided_graph.p', 'wb')
pickle.dump(provided_graph, pick)
pick.close()

    # create output graph, initialize as complete, will track graph in helper object
edge_count = 0
node_count = 0
for item in upa_graph:
    edge_count += len(upa_graph[item])
    node_count += 1
print 'edge_count should be close to 3047. Actual is ', edge_count/2
print 'node_count should be close to 1239. Actual is ', node_count
'''
loop_count = range( 10, 1000, 10)
fast_targeted_order_times = []
for element in loop_count:
    #print 'element is ', element
    upa_graph = make_rand_digraph(5, 1)

    # initialize helper object
    helper_g = UPATrial(5)
    #enn = 10
    add_nodes = range(5, element)
    for atom in add_nodes:
        upa_graph[atom] = set([])       # add all nodes and initialize to empty set

    for item in add_nodes:
        edges = helper_g.run_trial(5)
        for iota in edges:
            #print 'edges are ', edges
            upa_graph[item] = upa_graph[item] | set([iota])         # likely the issue with upa graphs is here
            upa_graph[iota] = upa_graph[iota] | set([item])

    loop = 100                                    # need to insert edges in both directions
    start_time = time.time()
    while loop > 0:
        TO_node_list = fast_targeted_order(upa_graph)
        #print TO_node_list
        #print loop
        loop -= 1
    end_time = time.time()
    fast_targeted_order_times.append((end_time - start_time)/100)
    print 'element is ', element, ' targeted_order run time is ', (end_time-start_time)/100



xvals = range(10, 1000, 10)
yvals1 = upa_targeted_order_times
yvals2 = fast_targeted_order_times
#yvals3 = Provided_values
#yvals2 = [1, 4, 9, 16, 25]

#print 'xvals are ', xvals
#print 'yvals1 are ', yvals1

plt.plot(xvals, yvals1, '-b', label='UPA Targeted Order')
plt.plot(xvals, yvals2, '-r', label='UPA Fast Targeted Order')
#plt.plot(xvals, yvals3, '-g', label='Provided Computer Network')
plt.legend(loc='upper right')
plt.ylabel('Seconds')
plt.xlabel('Number of Nodes')
plt.title('Targeted Order Run Time on Desktop Python')
plt.show()

pick = open('C:\Users\Dad\Documents\GitHub\Coursera_Discrete_Optimization\Targeted_order_times.p', 'wb')
pickle.dump(targeted_order_times, pick)
pick.close()
'''