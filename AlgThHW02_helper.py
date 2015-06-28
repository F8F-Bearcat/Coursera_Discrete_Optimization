"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

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

def compute_in_degrees(digraph):
    '''
    Input: a dictionary representing a directed graph. Nodes are keys, edges are values in a set
    Output: a dictionary of nodes as keys with values equal to a set including the directed edges
    pointing at that node.
    '''
    if len(digraph) == 0:
        return {}

    # initialize all nodes to empty set, nothing is pointing to a node initially
    pointed_to = {}
    for entry in digraph:
        pointed_to[entry] = set([])  # possible perf optimization if this were combined w below
                                     # +n operations, each node touched once to initialize

    # the loops below establish the edges that point to nodes as dictionary set values
    for element in digraph:
        for item in digraph[element]:
            if item not in pointed_to:
                pointed_to[item] = set([element])
            else:
                temp_set = pointed_to[item]
                temp_set = temp_set | set([element])
                pointed_to[item] = temp_set

    # at this point we have a dictionary with nodes as keys and sets of edges as the values
    # like this { 0:set([2, 4, 5], and so on...)}
    #
    # now convert the sets to counts

    in_degree_count_d = {}
    for iota in pointed_to:
        in_degree_count_d[iota] = len(pointed_to[iota])

    return in_degree_count_d

def in_degree_distribution(digraph):
    '''
    Input: a dictionary representing a directed graph. Nodes are keys, edges are values in a set
    Output: a dictionary of keys as in_degree and values equal to the number of nodes with that
    in-degree
    '''
    pointed_to = compute_in_degrees(digraph)
    #
    # compute_in_degrees(digraph) returns a dictionary (pointed_to) like this {0:1, 1:1, 2:1, etc}
    # integer type for keys and values.
    # Use unique pointed_to[iota] value entries as keys in the output dict (invert_and_count_d)
    # with the corresponding output dictionary (invert_and_count_d) values as the sum of the
    # elements in the input dictionary (pointed_to) with nodes that match the output dictionary's
    # key
    #
    invert_and_count_d = {}
    for iota in pointed_to:
        if pointed_to[iota] not in invert_and_count_d:
            invert_and_count_d[pointed_to[iota]] = 1
        else:
            temp = invert_and_count_d[pointed_to[iota]]
            temp += 1
            invert_and_count_d[pointed_to[iota]] = temp

    return invert_and_count_d

def plot_distribution(distribution, title):
    '''
    Input: a dictionary with keys as in-degree count and values as the number of nodes 
    with that in-degree count, and a string title that will be attached to the plot created
    Output: a matplotlib loglog plot of the distribution
    '''
    xlist = []
    for element in distribution:
        xlist.append(element)

    ylist = []
    for element in distribution:
        ylist.append(distribution[element])

    total_y = float(sum(ylist))
    ylist[:] = [x / total_y for x in ylist]

    plt.loglog(xlist, ylist, 'ro', basex=10)  # len(xlist) needs to equal len(ylist)
    #plt.loglog([1,2,3,10,12],[.5, 5, 50, 500, 520], 'ro', basex=10)  # 'ro' can be removed for default blue line
    #plt.grid(True)
    plt.grid(b=True, which='major', color='b', linestyle='-')
    #plt.grid(b=True, which='minor', color='r', linestyle='--')
    plt.xlabel('In-Degree (Log base 10)')
    plt.ylabel('Normalized (Log base 10)')
    plt.title(title)
    plt.show()
    pass  

def random_order(input_graph):
    '''
    Input: a graph
    Output: a list of nodes from the input graph in random random_order
    '''
    node_list = []
    for ele in input_graph:
        node_list.append(ele)   # this gives me a list of the nodes from the graph
    #print node_list

    random.shuffle(node_list)

    return node_list



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


# create output graph, initialize as complete, will track graph in helper object
start_time = time.time()
upa_graph = make_rand_digraph(2, 1)

# initialize helper object
helper_g = UPATrial(2)
add_nodes = range(2, 5)
for atom in add_nodes:
    upa_graph[atom] = set([])       # add all nodes and initialize to empty set

for item in add_nodes:
    edges = helper_g.run_trial(2)
    for iota in edges:
        #print 'edges are ', edges
        upa_graph[item] = upa_graph[item] | set([iota])         # likely the issue with upa graphs is here
        upa_graph[iota] = upa_graph[iota] | set([item])
                                    # need to insert edges in both directions

print 'upa_graph is ', upa_graph

random_node_list = random_order(upa_graph)
print 'random_node_list is ', random_node_list

UPA_values = compute_resilience(upa_graph, random_node_list)

#print random_node_list

xvals = range(len(random_node_list) + 1 )
yvals1 = UPA_values
#yvals2 = [1, 4, 9, 16, 25]

print 'xvals are ', xvals
print 'yvals1 are ', yvals1

plt.plot(xvals, yvals1, '-b', label='UPA Graph')
#plt.plot(xvals, yvals2, '-r', label='quadratic')
plt.legend(loc='upper right')
plt.show()
'''
in_degree = compute_in_degrees(upa_graph)
#print in_degree
distribution = in_degree_distribution(upa_graph)

end_time = time.time()
print 'Run time is ', end_time - start_time, ' seconds'

#print distribution
plot_distribution(distribution, 'DPA Algorithm In-Degree Distribution' )
'''
