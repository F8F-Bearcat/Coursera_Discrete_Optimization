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

EX_GRAPH0 = {0:set([1, 2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3, 7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1, 2]), 9:set([0, 3, 4, 5, 6, 7])}
EX_GRAPH3 = {}
EX_GRAPH4 = {0:set([]), 1:set([]), 2:set([]), 3:set([])}
EX_GRAPH5 = {0:set([2]), 1:set([3]), 2:set([0]), 3:set([1]), 4:set([5]), 5:set([4]), 6:set([7]), 7:set([6])}
EX_GRAPH6 = {0:set([1, 3]), 1:set([0]), 2:set([5]), 3:set([0]), 4:set([]), 5:set([2])}
print cc_visited(EX_GRAPH6)
