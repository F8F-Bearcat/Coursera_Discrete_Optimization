'''
This is a test bench environment to verify FastClosestPair implementations.
Class:  Algorithmic Thinking Part 2
Coursera, Rice University
Builds a source of random points, then applies to both the FastClosestPair and a brute force design
The brute force design is viewed as the 'golden reference', easy to implement, but slower
Run millions of verification cases to make sure FastClosestPair delivers the same results
'''
import random
import cluster_class
import SlowClosestPair
import FastClosestPair
import numpy as np
import matplotlib.pyplot as plt


seed = 2        # set random seed so results can be reproducible
size = 20       # number of points generated
loops = 100     # number of  test cases generated and checked
control_vector = [seed, size, loops]
random.seed(control_vector[0])

for cycle in range(loops):

    all_points = []
    for item in range(size):    # make random test points in area bounded by +/- 1 in x,y  0,0 center
        point_x = 2*random.random() - 1
        point_y = 2*random.random() - 1
        point = (point_x, point_y)
        all_points.append(point)
    all_points.sort()

    slow_distance = SlowClosestPair.SlowClosestPair(all_points)
    fast_distance = FastClosestPair.FastClosestPair(all_points)  # just a placeholder tuple at this point

    debug_info = [all_points, seed, cycle, slow_distance, fast_distance]

    print slow_distance

plot_me = debug_info[0]
xval, yval = zip(*plot_me)
plt.scatter(xval, yval, s=20, c='b', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i], yval[i]))
plt.show()


    #print all_points
'''
    cluster_list = []
    for point in all_points:
        first_cluster = cluster_class.Cluster(95014, point[0], point[1], 100, .5)
        cluster_list.append(first_cluster)
'''