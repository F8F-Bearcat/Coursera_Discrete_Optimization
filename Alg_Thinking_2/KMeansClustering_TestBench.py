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

    coursera_test_case = [['01073', 704.191210749, 411.014665198, 662047, 7.3e-05], ['06059', 113.997715586, 368.503452566, 2846289, 9.8e-05], ['06037', 105.369854549, 359.050126004, 9519338, 0.00011], ['06029', 103.787886113, 326.006585349, 661645, 9.7e-05], ['06071', 148.402461892, 350.061039619, 1709434, 7.7e-05], ['06075', 52.7404001225, 254.517429395, 776733, 8.4e-05], ['08031', 371.038986573, 266.847932979, 554636, 7.9e-05], ['24510', 872.946822486, 249.834427518, 651154, 7.4e-05], ['34013', 906.236730753, 206.977429459, 793633, 7.1e-05], ['34039', 905.587082153, 210.045085725, 522541, 7.3e-05], ['34017', 909.08042421, 207.462937763, 608975, 9.1e-05], ['36061', 911.072622034, 205.783086757, 1537195, 0.00015], ['36005', 912.315497328, 203.674106811, 1332650, 0.00011], ['36047', 911.595580089, 208.928374072, 2465326, 9.8e-05], ['36059', 917.384980291, 205.43647538, 1334544, 7.6e-05], ['36081', 913.462051588, 207.615750359, 2229379, 8.9e-05], ['41051', 103.293707198, 79.5194104381, 660486, 9.3e-05], ['41067', 92.2254623376, 76.2593957841, 445342, 7.3e-05], ['51013', 865.681962839, 261.222875114, 189453, 7.7e-05], ['51840', 845.843602685, 258.214178983, 23585, 7.1e-05], ['51760', 865.424050159, 293.735963553, 197790, 8.6e-05], ['55079', 664.855000617, 192.484141264, 940164, 7.4e-05], ['54009', 799.221537984, 240.153315109, 25447, 7.7e-05], ['11001', 867.470401202, 260.460974222, 572059, 7.7e-05]]
    all_points = []
    for ele in coursera_test_case:
        point_x = ele[1]
        point_y = ele[2]
        point = (point_x, point_y)
        all_points.append(point)
    all_points.sort()

    print 'all_points after initialization '
    print all_points
    # make clusters 3 with 3 values for fips
    all_clusters = []
    for point in all_points:
        if all_points.index(point) < 3:
            new_cluster = alg_cluster.Cluster(set([300, 400, 500]), point[0], point[1], 1, .5)
            all_clusters.append(new_cluster)
        else:
            new_cluster = alg_cluster.Cluster(set([all_points.index(point)]), point[0], point[1], 1, .5)
            all_clusters.append(new_cluster)

    #  coursera test case
    all_clusters = []
    for item in coursera_test_case:
        new_cluster = alg_cluster.Cluster(set([item[0]]), item[1], item[2], item[3], item[4])
        all_clusters.append(new_cluster)
    print ' '
    print 'all_clusters after initialization'
    print all_clusters

result = KMeansClust.kmeans_clustering(all_clusters, 15, 1) # three clusters, 4 iterations
print ' '
print 'resulting clusters are ', result
print ' '
    #1print slow_distance, fast_distance

print ' '
print ' pass percentage is ', pass_count*100./(cycle+1)
print ' '
#print debug_db
#print 'result list is ', result

plot_me = all_points
xval, yval = zip(*plot_me)
plt.scatter(xval, yval, s=20, c='b', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i]+.02, yval[i]+.02))
plt.xlim(0, 1000)
plt.ylim(50, 450)
plt.title('Input: Coursera test case points')
plt.draw()

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
plt.xlim(0, 1000)
plt.ylim(50, 450)
plt.title('Coursera test case initial biggest clusters')
plt.draw()

all_clusters = result
all_clusters.sort(key=lambda cluster: len(cluster.fips_codes()), reverse=True)
temp_result = all_clusters[:]
plot_cluster_centers = []
for item in temp_result:
    point_x = item.horiz_center()
    point_y = item.vert_center()
    plot_cluster_centers.append((point_x, point_y))

plt.figure()  #makes another window
xval, yval = zip(*plot_cluster_centers)
plt.scatter(xval, yval, s=60, c='r', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i]+.05, yval[i]+.05))
plt.xlim(0, 1000)
plt.ylim(50, 450)
plt.title('Coursera test case RESULT clusters')
plt.show()


    #print all_points
'''
    cluster_list = []
    for point in all_points:
        first_cluster = cluster_class.Cluster(95014, point[0], point[1], 100, .5)
        cluster_list.append(first_cluster)
'''