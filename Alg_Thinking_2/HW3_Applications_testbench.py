'''
This is a test bench environment to verify FastClosestPair implementations.
Class:  Algorithmic Thinking Part 2
Coursera, Rice University
Builds a source of random points, then applies to both the FastClosestPair and a brute force design
The brute force design is viewed as the 'golden reference', easy to implement, but slower
Run millions of verification cases to make sure FastClosestPair delivers the same results
'''
import random
import HierClust
import cluster_class
import csv_to_cluster
import numpy as np
import matplotlib.pyplot as plt

def fips_to_points(cluster, cluster_list):
    '''
    n squared brute force - won't scale...
    cluster_list input is a list of singletons (only one area code)
    returns a list of points, and cluster center
    '''
    points = []
    for ele in cluster.fips_codes():
        for cl in cluster_list:
            if ele == list(cl.fips_codes())[0]:   #[0] gets the single entry out of the set
                point_x = cl.horiz_center()
                point_y = cl.vert_center()
                point = [point_x, point_y]
                points.append(point)
    cluster_center = [cluster.horiz_center(), cluster.vert_center()]
    return points, cluster_center

def next_color(color_list):
    '''
    takes color list, returns color, and shifts color list
    Output: color (matplotlib color string, one char) and modified color_list
    '''
    color = color_list.pop()
    color_list.insert(0, color)
    return color, color_list



seed = 9        # set random seed so results can be reproducible
size = 20       # number of points generated
loops = 1    # number of  test cases generated and checked
cluster_count = 9
control_vector = [seed, size, loops, cluster_count]
random.seed(control_vector[0])

debug_db = {}
pass_count = 0
for cycle in range(loops):
    '''
    all_points = []
    for item in range(size):    # make random test points in area bounded by +/- 1 in x,y  0,0 center
        point_x = 2*random.random() - 1  # scale the coordinates to (-1, 1)
        point_y = 2*random.random() - 1
        point = (point_x, point_y)
        all_points.append(point)
    all_points.sort()   # ensure increasing x
    '''
    cluster_list = csv_to_cluster.csv_to_cl()

    all_points = []
    for item in cluster_list:
        point_x = item.horiz_center()
        point_y = item.vert_center()
        point = (point_x, point_y)
        all_points.append(point)
    all_points.sort()

    '''
    all_clusters = []  # all_clusters will be mutated, so plot points 
    for point in all_points:
        idx = all_points.index(point) # unique index so final set should contain all
        initial_cluster = cluster_class.Cluster(set([idx]), point[0], point[1], idx+1, (idx+1)/2.0)
        all_clusters.append(initial_cluster)
    '''

    #result = HierClust.hierarchical_clustering(all_clusters, cluster_count )
    result = HierClust.hierarchical_clustering(cluster_list, cluster_count )

        #1print slow_distance, fast_distance
    final_cluster_count = 0
    for cluster in result:
        final_cluster_count += len(cluster.fips_codes())

    if final_cluster_count == size:
        pass_count += 1

print ' '
print ' pass percentage is ', pass_count*100./(cycle+1)
print ' '
#print debug_db
print 'result list is ', result

mpl_color_cycle = ['b', 'y', 'c', 'm', 'k', 'g']

#plotting loop, one cluster at a time, 
for cluster in result:
    pt_color, mpl_color_cycle = next_color(mpl_color_cycle)
    fips_points, cluster_center = fips_to_points(cluster, cluster_list)
    xval, yval = zip(*fips_points)
    plt.scatter(xval, yval, s=20, c=pt_color, alpha=0.9)
    plt.scatter(cluster_center[0], cluster_center[1], s=80, c='r', alpha=0.5)
    plt.draw()

plt.title('111 Input clusters and grouped clusters')
plt.show()

'''
###
plot_cluster = []
for item in result:
    point_x = item.horiz_center()
    point_y = item.vert_center()
    plot_cluster.append((point_x, point_y))


#wait = raw_input()  # hit enter to get the second plot shown

plot_cluster = []
for item in result:
    point_x = item.horiz_center()
    point_y = item.vert_center()
    plot_cluster.append((point_x, point_y))

plt.figure()  #makes another window
xval, yval = zip(*plot_cluster)
plt.scatter(xval, yval, s=80, c='r', alpha=0.5)
#n = range(len(xval))
#for i, txt in enumerate(n):
#    plt.annotate(txt, (xval[i]+.05, yval[i]+.05))
#plt.xlim(-1, 1)
#plt.ylim(-1, 1)
plt.title('Hierarchial Clustering of 111 counties')
plt.show()

    #print all_points

    cluster_list = []
    for point in all_points:
        first_cluster = cluster_class.Cluster(95014, point[0], point[1], 100, .5)
        cluster_list.append(first_cluster)

#n = range(len(xval))
#for i, txt in enumerate(n):
#    plt.annotate(txt, (xval[i]+.02, yval[i]+.02))
#plt.xlim(-1, 1)
#plt.ylim(-1, 1)
'''