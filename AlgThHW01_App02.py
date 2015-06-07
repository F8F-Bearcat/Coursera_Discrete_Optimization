'''
Make a random directed graph
Edge (i,j) is an edge going from node i to node j, head of edge at node j
'''
import random
import numpy as np
import matplotlib.pyplot as plt
import pickle
import time

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

start_time = time.time()
file_name_string = 'C:/Users/Dad/Documents/GitHub/Coursera_Discrete_Optimization/citations.p'
file_h = open(file_name_string, 'r')
citation_graph = pickle.load(file_h)
#print citation_graph[1001]
file_h.close()


digraph =  make_rand_digraph(1000, .5)
#print digraph
in_degree = compute_in_degrees(digraph)
#print in_degree
distribution = in_degree_distribution(digraph)

end_time = time.time()
print 'Run time is ', end_time - start_time, ' seconds'

#print distribution
plot_distribution(distribution, 'Random Graph (ER Algorithm) In-Degree Distribution' )

