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


#test function here
print make_complete_graph( 10 )
print make_complete_graph( 1 )
print make_complete_graph( 0 )
