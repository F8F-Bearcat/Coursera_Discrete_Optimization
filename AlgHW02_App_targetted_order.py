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

    # create output graph, initialize as complete, will track graph in helper object

loop_count = range( 10, 1000, 10)
targeted_order_times = []
for element in loop_count:
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
        TO_node_list = targeted_order(upa_graph)
        #print TO_node_list
        #print loop
        loop -= 1
    end_time = time.time()
    targeted_order_times.append((end_time - start_time)/100)
    print 'element is ', element, ' targeted_order run time is ', (end_time-start_time)/100



xvals = loop_count
yvals1 = targeted_order_times
#yvals2 = ER_values
#yvals3 = Provided_values
#yvals2 = [1, 4, 9, 16, 25]

#print 'xvals are ', xvals
#print 'yvals1 are ', yvals1

plt.plot(xvals, yvals1, '-b', label='Targeted Order')
#plt.plot(xvals, yvals2, '-r', label='ER Graph, p = .002')
#plt.plot(xvals, yvals3, '-g', label='Provided Computer Network')
plt.legend(loc='upper right')
plt.ylabel('Seconds')
plt.xlabel('Number of Nodes')
plt.title('Algorithm Run Time')
plt.show()

pick = open('C:\Users\Dad\Documents\GitHub\Coursera_Discrete_Optimization\Targeted_order_times.p', 'wb')
pickle.dump(targeted_order_times, pick)
pick.close()