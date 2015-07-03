'''
This is a module to test pickle file transfers which I have hit some issues with...
'''
import pickle
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

Test_g = make_rand_digraph(1239, 1)

try:
    pick = open('C:\\Users\\Dad\\Documents\\GitHub\\Coursera_Discrete_Optimization\\Test_g.p', 'rb')
    Test_g_2 = pickle.load(pick)
    pick.close()
    print 'try path followed'
except:
    pick = open('C:\\Users\\Dad\\Documents\\GitHub\\Coursera_Discrete_Optimization\\Test_g.p', 'wb')
    pickle.dump(Test_g, pick)
    pick.close()
    print 'except path followed'

# get provided graph
print len(Test_g)
print len(Test_g_2)

if Test_g == Test_g_2:
    print 'The two graphs Test_g and Test_g_2 match !'
else:
    print 'The two graphs Test_g and Test_g_2 do not match !'


