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

EX_GRAPH0 = {0:set([1, 2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}
