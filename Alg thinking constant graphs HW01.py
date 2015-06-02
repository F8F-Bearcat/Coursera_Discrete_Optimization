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
    
    for e in node_set:
        complete_dict[e] = node_set - set([e])
        
    return complete_dict


EX_GRAPH0 = { 0:set([1,2]), 1:set([]), 2:set([]) }
EX_GRAPH1 = { 0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([1]), 4:set([1]), 5:set([2]), 6:set([]) }
EX_GRAPH2 = { 0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([1]), 4:set([1]), 5:set([2]), 6:set([]) }

print EX_GRAPH2

two = EX_GRAPH2[2]
new_two = two | set([7])
EX_GRAPH2[2] = new_two

three = EX_GRAPH2[3]
new_three = three | set([7])
EX_GRAPH2[3] = new_three

EX_GRAPH2[7] = set([3])
EX_GRAPH2[8] = set([1,2])
EX_GRAPH2[9] = set([0,3,4,5,6,7])

print EX_GRAPH2
