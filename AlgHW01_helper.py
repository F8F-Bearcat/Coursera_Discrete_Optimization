"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random

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

    # Make a complete random directed graph with 13 nodes 
    dpa_graph = make_rand_digraph(13, 1)
    print dpa_graph

    trial_obj = DPATrial(13)
    print trial_obj
