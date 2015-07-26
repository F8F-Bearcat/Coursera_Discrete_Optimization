'''
This is a test bench environment to verify FastClosestPair implementations.
Class:  Algorithmic Thinking Part 2
Coursera, Rice University
Builds a source of random points, then applies to both the FastClosestPair and a brute force design
The brute force design is viewed as the 'golden reference', easy to implement, but slower
Run millions of verification cases to make sure FastClosestPair delivers the same results
'''
import random
import alg_cluster
import KMeansClust
import numpy as np
import matplotlib.pyplot as plt



seed = 3        # set random seed so results can be reproducible
size = 30       # number of points generated
loops = 1     # number of  test cases generated and checked
cluster_count = 3
control_vector = [seed, size, loops, cluster_count]
random.seed(control_vector[0])

debug_db = {}
pass_count = 0
for cycle in range(loops):

# make points
    all_points = []
    for item in range(size):    # make random test points in area bounded by +/- 1 in x,y  0,0 center
        point_x = 2*random.random() - 1  # scale the coordinates to (-1, 1)
        point_y = 2*random.random() - 1
        point = (point_x, point_y)
        all_points.append(point)
    all_points.sort()

# make clusters 3 with 3 values for fips
    all_clusters = []
    for point in all_points:
        if all_points.index(point) < 3:
            new_cluster = alg_cluster.Cluster(set([300, 400, 500]), point[0], point[1], 1, .5)
            all_clusters.append(new_cluster)
        else:
            new_cluster = alg_cluster.Cluster(set([all_points.index(point)]), point[0], point[1], 1, .5)
            all_clusters.append(new_cluster)

result = KMeansClust.kmeans_clustering(all_clusters, 3, 1) # three clusters, 4 iterations
print ' '
print 'resulting clusters are ', result
print ' '
    #1print slow_distance, fast_distance

print ' '
print ' pass percentage is ', pass_count*100./(cycle+1)
print ' '
#print debug_db
#print 'result list is ', result

#plot_me = debug_info[0]
plot_me = all_points
xval, yval = zip(*plot_me)
plt.scatter(xval, yval, s=20, c='b', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i]+.02, yval[i]+.02))
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.title('Input: random points in -1 to 1 range')
plt.draw()

#wait = raw_input()  # hit enter to get the second plot shown

all_clusters.sort(key=lambda cluster: len(cluster.fips_codes()))
temp_result = all_clusters[-3:]
plot_cluster_centers = []
for item in temp_result:
    point_x = item.horiz_center()
    point_y = item.vert_center()
    plot_cluster_centers.append((point_x, point_y))

plt.figure()  #makes another window
xval, yval = zip(*plot_cluster_centers)
plt.scatter(xval, yval, s=60, c='g', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i]+.05, yval[i]+.05))
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.title('KMeans Clusters')
plt.show()


    #print all_points
'''
    cluster_list = []
    for point in all_points:
        first_cluster = cluster_class.Cluster(95014, point[0], point[1], 100, .5)
        cluster_list.append(first_cluster)
'''