'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the FastClosestPair function from Homework 3, Project 3
'''
import math
import SlowClosestPair
import cluster_class
import random

def closest_pair_strip(list_of_clusters, mid, dee):
    '''
    Input: a list of points, the x location of the split plane, and dee is half the strip width
    Output: tuple (d, i, j) representing the closest points in the middle closest_strip_tuple
    '''
    clusters_in_strip = []
    for cluster in list_of_clusters:
        if (abs(cluster.horiz_center()-mid)) < dee:
            clusters_in_strip.append(cluster)

    clusters_in_strip.sort(key=lambda cluster: cluster.horiz_center())  # non decreasing order
    #print 'mid is ', mid
    #print 'dee is ', dee
    #print 'clusters_in_strip are '
    #print clusters_in_strip
    #print 'list of points are ', list_of_clusters

    strip_point_count = len(clusters_in_strip)
    ret_tuple = (float('inf'), -1, -1)

    for cluster in clusters_in_strip:
        if clusters_in_strip.index(cluster) == strip_point_count - 1:
            break
        else:
            for check in range(1, 4):  # check 3 points
                r_idx = clusters_in_strip.index(cluster)+check
                if (r_idx) == strip_point_count:
                    break
                else:
                    strip_t = SlowClosestPair.slow_closest_pair([cluster, clusters_in_strip[r_idx]])
                    if strip_t[0] < ret_tuple[0]:
                        answer_list = []
                        answer_list.append(strip_t[0])
                        #put the indices in increasing order
                        first_cl_index = list_of_clusters.index(cluster)
                        second_cl_index = list_of_clusters.index(clusters_in_strip[r_idx])
                        if first_cl_index < second_cl_index:
                            answer_list.append(list_of_clusters.index(cluster))
                            answer_list.append(list_of_clusters.index(clusters_in_strip[r_idx]))
                        else:
                            answer_list.append(list_of_clusters.index(clusters_in_strip[r_idx]))
                            answer_list.append(list_of_clusters.index(cluster))
                        ret_tuple = tuple(answer_list)

    return ret_tuple

def fast_closest_pair(list_of_clusters):
    '''
    Input: a list of clusters
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_clusters
            and i and j are the indexes of the two points that are the closest together
    '''
    size = len(list_of_clusters)
    if size < 4:
        ret_tuple = SlowClosestPair.slow_closest_pair(list_of_clusters)
    else:
        split = int(math.floor(size/2.0))
        #print 'split is ', split
        left = list_of_clusters[:split]
        right = list_of_clusters[split:]
        left_tuple = fast_closest_pair(left)
        right_tuple = fast_closest_pair(right)
        right_list = list(right_tuple)
        right_list[1] += split
        right_list[2] += split
        right_tuple = tuple(right_list)
        if left_tuple[0] < right_tuple[0]:
            l_and_r_min_tuple = left_tuple
        else:
            l_and_r_min_tuple = right_tuple
        m_minus_one = list_of_clusters[split-1].horiz_center()
        m_itself = list_of_clusters[split].horiz_center()
        middle = .5*(m_minus_one + m_itself)
        closest_strip_tuple = closest_pair_strip(list_of_clusters, middle, l_and_r_min_tuple[0])
        #print 'd is ', l_and_r_min_tuple[0]
        #print 'l_and_r_min_tuple[0] is ', l_and_r_min_tuple[0]
        #print 'closest_strip_tuple[0] is ', closest_strip_tuple[0]
        if l_and_r_min_tuple[0] < closest_strip_tuple[0]:
            ret_tuple = l_and_r_min_tuple
        else:
            ret_tuple = closest_strip_tuple
    return ret_tuple

'''
p01 = cluster_class.Cluster(95014, 0, 0, 100, .5)
p02 = cluster_class.Cluster(95014, 0, 1, 100, .5)
p03 = cluster_class.Cluster(95014, 1, 1, 100, .5)

test_list = [p01, p02, p03]

print SlowClosestPair.SlowClosestPair(test_list)
'''
'''
p01 = (0, 0)
p02 = (0, 1)
p03 = (1, 1)
p04 = (1, 0)
p05 = (-1, 1)
p06 = (-1, 0)
p07 = (-1, -1)
p08 = (0, -1)
p09 = (1, -1)
p10 = (1, 1.1)






#print SlowClosestPair(test_list)
'''

p01 = cluster_class.Cluster(set([]), 0, 0, 100, .5)
p02 = cluster_class.Cluster(set([]), 0, 1, 100, .5)
p03 = cluster_class.Cluster(set([]), 1, 1, 100, .5)
p04 = cluster_class.Cluster(set([]), 1, 0, 100, .5)
p05 = cluster_class.Cluster(set([]), -1, 1, 100, .5)
p06 = cluster_class.Cluster(set([]), -1, 0, 100, .5)
p07 = cluster_class.Cluster(set([]), -1, -1, 100, .5)
p08 = cluster_class.Cluster(set([]), 0, -1, 100, .5)
p09 = cluster_class.Cluster(set([]), 1, -1, 100, .5)
p10 = cluster_class.Cluster(set([]), 1, 1.1, 100, .5)
test_list = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]

for element in range(10):
    random.shuffle(test_list)
    test_list.sort(key=lambda cluster: cluster.horiz_center())
    #print test_list
    print fast_closest_pair(test_list)

#print fast_closest_pair(test_list)

'''
    for check in range(strip_point_count-2):
        terminate = min(check+3, strip_point_count-1)
        vee = check + 1
        for item in range(vee, terminate + 1):
            strip_tuple = SlowClosestPair.SlowClosestPair([clusters_in_strip[check], clusters_in_strip[item]])
            if strip_tuple[0] < ret_tuple[0]:
                ret_tuple = strip_tuple
'''
