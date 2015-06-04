'''
This module is used to create the compute_in_degrees function.  This will enumerate the number of
directed edges that point to each node.
'''
def make_complete_graph(num_nodes):
    '''
    Input:  a count of the number of nodes in the desired complete graph

    Complete means every node connects to every other node, without self loops

    Output: a dictionary representation of the desired graph, with the node
    of the graph as the key, and the value returned a set of all the edges
    originating from that node.
    '''

    complete_dict = {}

    if num_nodes == 0:
        return complete_dict

    node_set = set(range(num_nodes))

    for element in node_set:
        complete_dict[element] = node_set - set([element])

    return complete_dict

def compute_in_degrees(digraph):
    '''
    Input: a dictionary representing a directed graph. Nodes are keys, edges are values in a set
    Output: a dictionary of nodes as keys with values equal to the sum of the edges pointing to
    that node
    '''
    if len(digraph) == 0:
        return {}

    pointed_to = {}
    for element in digraph:
        for item in digraph[element]:
            if item not in pointed_to:
                pointed_to[item] = set([element])
            else:
                temp_set = pointed_to[item]
                temp_set = temp_set | set([element])
                pointed_to[item] = temp_set
    return pointed_to

def in_degree_distribution(digraph):
    '''
    Input: a dictionary representing a directed graph. Nodes are keys, edges are values in a set
    Output: a dictionary of nodes as keys with values equal to the integer sum of the edges pointing
    to the node dictionary naming convention trailing _d denotes dictionary
    '''
    if len(digraph) == 0:
        return {}

    histogram_data_d = {}
    for element in digraph:
        histogram_data_d[element] = len(digraph[element])

    return histogram_data_d

EX_GRAPH0 = {0:set([1, 2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}

test_d = compute_in_degrees(EX_GRAPH2)
print test_d
