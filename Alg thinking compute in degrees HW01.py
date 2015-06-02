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

    for ele in node_set:
        complete_dict[ele] = node_set - set([ele])

    return complete_dict

def compute_in_degrees(digraph):
    '''
    Input: a dictionary representing a directed graph. Nodes are keys, edges are values in a set
    Output: a dictionary of nodes as keys with values equal to the sum of directed edges
    pointing at that node.
    '''
    if len(digraph) == 0:
        return {}

    pointed_to = {}
    for ele in digraph:
        for item in digraph[ele]:
            if item not in pointed_to:
                pointed_to[item] = set([ele])
            else:
                temp_set = pointed_to[item]
                temp_set = temp_set | set([ele])
                pointed_to[item] = temp_set
    return pointed_to



EX_GRAPH0 = {0:set([1, 2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([])}

print EX_GRAPH2

two = EX_GRAPH2[2]
new_two = two | set([7])
EX_GRAPH2[2] = new_two

EX_GRAPH2[7] = set([3])
EX_GRAPH2[8] = set([1, 2])
EX_GRAPH2[9] = set([0, 3, 4, 5, 6, 7])

print EX_GRAPH2

result_d = compute_in_degrees(EX_GRAPH0)
print result_d
print 'node', 'in_degree'
for ele in result_d:
    print ele, '    ', len(result_d[ele])

result_d = compute_in_degrees(EX_GRAPH1)
print result_d
print 'node', 'in_degree'
for ele in result_d:
    print ele, '    ', len(result_d[ele])

result_d = compute_in_degrees(EX_GRAPH2)
print result_d
print 'node', 'in_degree'
for ele in result_d:
    print ele, '    ', len(result_d[ele])

