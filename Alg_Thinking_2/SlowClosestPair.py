'''
This is the submit_hw3.py script
It needs to include slow_closest_pair, closest_pair_strip, fast_closest_pair, hierarchial_clusering
and kmeans_clustering
and meet pylint coding guidelines
'''
import math
import cluster_class

def euclid_dist(p_one, p_two):
    '''
    Input: two tuples each representing a point in an x-y plane, format (x,y) - first item x
    Output: The euclidian distance between the two points
    Calculates euclidian distance between two points in a plane: math.sqrt((x0-x1)**2 +(y0-y1)**2)
    '''
    assert len(p_one) == len(p_two), 'the two input points need the same dimension'
    assert len(p_one) == 2, 'both inputs need two coordinates'
    return math.sqrt((p_one[0]-p_two[0])**2 + (p_one[1]-p_two[1])**2)

def slow_closest_pair(list_of_clusters):
    '''
    Input: a list of clusters
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_clusters
            and i and j are the indexes of the two points that are the closest together
    '''
    ret_list = [float('inf'), -1, -1]
    #all_combinations_two_points = [list(x) for x in itertools.combinations(list_of_clusters, 2)]
    all_combinations_two_clusters = []
    for cluster in list_of_clusters:
        if list_of_clusters.index(cluster) == len(list_of_clusters)-1:
            break
        next_cl_index = list_of_clusters.index(cluster)+1
        for item_y in range(next_cl_index, len(list_of_clusters)):
            all_combinations_two_clusters.append((cluster, list_of_clusters[item_y]))
    #print all_combinations_two_clusters
    for cluster_tuple in all_combinations_two_clusters:
        points = []
        for cluster in cluster_tuple:
            points.append([cluster.horiz_center(), cluster.vert_center()])
        distance = euclid_dist(points[0], points[1])
        if distance < ret_list[0]:   # if true, a new minimum distance has been found
            ret_list[0] = distance
            ret_list[1] = list_of_clusters.index(cluster_tuple[0])
            ret_list[2] = list_of_clusters.index(cluster_tuple[1])
            low_index = list_of_clusters.index(cluster_tuple[0])
            hi_index = list_of_clusters.index(cluster_tuple[1])
            assert low_index < hi_index, 'index order small to large'
    return tuple(ret_list)
'''
p01 = cluster_class.Cluster(set([]), 0, 0, 100, .5)
p02 = cluster_class.Cluster(set([]), 0, 1, 100, .5)
p03 = cluster_class.Cluster(95014, 1, 1, 100, .5)
p04 = cluster_class.Cluster(95014, 1, 0, 100, .5)
p05 = cluster_class.Cluster(95014, -1, 1, 100, .5)
p06 = cluster_class.Cluster(95014, -1, 0, 100, .5)
p07 = cluster_class.Cluster(95014, -1, -1, 100, .5)
p08 = cluster_class.Cluster(95014, 0, -1, 100, .5)
p09 = cluster_class.Cluster(95014, 1, -1, 100, .5)
p10 = cluster_class.Cluster(95014, 1, 1.1, 100, .5)

test_list = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]

for element in range(100000):
    random.shuffle(test_list)
    print SlowClosestPair(test_list)

p01 = (0,0)
p02 = (1,0)

print p01.horiz_center()
test_list = [p01, p02]
print slow_closest_pair(test_list)
'''