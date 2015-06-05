'''
Make a random directed graph
Edge (i,j) is an edge going from node i to node j, head of edge at node j
'''
import random
def make_rand_digraph(num_nodes, prob):
    '''
	Input: number of nodes, probability that an edge exists
	Output: A dictionary with keys as node numbers and values as sets of edges connected to that node
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

print make_rand_digraph(4, .5)
