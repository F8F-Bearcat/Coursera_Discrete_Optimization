'''
Graph datastructure work.  Starting with the bfs (breadth first search) algorithm. And then
cc (connected components) will be added
'''
from collections import deque

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


