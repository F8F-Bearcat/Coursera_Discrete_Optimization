'''
This is a test bench environment to verify FastClosestPair implementations.
Class:  Algorithmic Thinking Part 2
Coursera, Rice University
Builds a source of random points, then applies to both the FastClosestPair and a brute force design
The brute force design is viewed as the 'golden reference', easy to implement, but slower
Run millions of verification cases to make sure FastClosestPair delivers the same results
'''
import random
import SlowClosestPair
import FastClosestPair
import cluster_class
from datetime import date
import numpy as np
import matplotlib.pyplot as plt


seed = 7        # set random seed so results can be reproducible
size = 40       # number of points generated
loops = 1000     # number of  test cases generated and checked
control_vector = [seed, size, loops]
random.seed(control_vector[0])

debug_db = {}
pass_count = 0
for cycle in range(loops):

    all_clusters = []
    for item in range(size):    # make random test points in area bounded by +/- 1 in x,y  0,0 center
        point_x = 2*random.random() - 1  # scale the coordinates to (-1, 1)
        point_y = 2*random.random() - 1
        new_cluser = cluster_class.Cluster(set([]), point_x, point_y, 1, 1)
        all_clusters.append(new_cluser)
    all_clusters.sort(key=lambda cluster: cluster.horiz_center())

    slow_distance = SlowClosestPair.slow_closest_pair(all_clusters)
    fast_distance = FastClosestPair.fast_closest_pair(all_clusters)  # just a placeholder tuple at this point
    #print slow_distance, fast_distance

    if slow_distance == fast_distance:
        pass_count += 1
    else:
        debug_info = [all_clusters, seed, cycle, slow_distance, fast_distance]
        debug_db[cycle] = debug_info
        print 'failing cycle is ', cycle
        print slow_distance, fast_distance

    #print slow_distance, fast_distance

print ' '
print ' pass percentage is ', pass_count*100./(cycle+1)
print ' '
#print debug_db
'''
print 'failing cycle 1998 is '
failing_info = debug_db[1998]
failing_cluster_list = failing_info[0]
print failing_cluster_list

plot_me = []

for cluster in failing_cluster_list:
    point_x = cluster.horiz_center()
    point_y = cluster.vert_center()
    plot_me.append((point_x, point_y))
print date.today()
print ' '
print 'cluster centers failing case '
print plot_me

xval, yval = zip(*plot_me)
plt.scatter(xval, yval, s=20, c='b', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i]-.05, yval[i]-.05))
plt.title( date.today())
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()



    #print all_clusters

    cluster_list = []
    for point in all_clusters:
        first_cluster = cluster_class.Cluster(95014, point[0], point[1], 100, .5)
        cluster_list.append(first_cluster)
'''