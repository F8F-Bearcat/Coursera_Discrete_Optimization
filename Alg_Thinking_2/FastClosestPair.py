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

    clusters_in_strip.sort(key=lambda cluster: cluster.vert_center())  # non decreasing order
    #print 'mid is ', mid
    #print 'dee is ', dee
    #print 'clusters_in_strip are '
    #print clusters_in_strip
    #print 'list of points are ', list_of_clusters

    strip_point_count = len(clusters_in_strip)
    ret_tuple = (float('inf'), -1, -1)

    for cluster in clusters_in_strip:
        #print 'look at this cluster', clusters_in_strip.index(cluster)
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
        #print 'left is ', left
        right = list_of_clusters[split:]
        #print 'right is ', right
        left_tuple = fast_closest_pair(left)
        #print 'left_tuple is ', left_tuple
        right_tuple = fast_closest_pair(right)
        #print 'right_tuple is ', right_tuple
        right_list = list(right_tuple)
        right_list[1] += split
        right_list[2] += split
        right_tuple = tuple(right_list)
        #print 'second right_tuple is ', right_tuple
        if left_tuple[0] < right_tuple[0]:
            l_and_r_min_tuple = left_tuple
        else:
            l_and_r_min_tuple = right_tuple
        m_minus_one = list_of_clusters[split-1].horiz_center()
        m_itself = list_of_clusters[split].horiz_center()
        middle = .5*(m_minus_one + m_itself)
        #print 'middle is ', middle
        #print 'dee is ', l_and_r_min_tuple[0]
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
test_list = [(-0.5353004213408008, 0.8769450694142287), (-0.055573548533075945, -0.6886736187148934), (0.1000582810382562, 0.40804899650093307), (0.12508086036682675, 0.9796129245098657), (0.14368005661209637, -0.18625701316364385), (0.3661535415505568, -0.7519118099544913)]
#test_list = [alg_cluster.Cluster(set([]), -0.535300421341, 0.876945069414, 1, 1), alg_cluster.Cluster(set([]), -0.0555735485331, -0.688673618715, 1, 1), alg_cluster.Cluster(set([]), 0.100058281038, 0.408048996501, 1, 1), alg_cluster.Cluster(set([]), 0.125080860367, 0.97961292451, 1, 1), alg_cluster.Cluster(set([]), 0.143680056612, -0.186257013164, 1, 1), alg_cluster.Cluster(set([]), 0.366153541551, -0.751911809954, 1, 1)]
test_list_cluster = []
for point in test_list:
    cluster = cluster_class.Cluster(set([]), point[0], point[1], 1, 2)
    test_list_cluster.append(cluster)
print fast_closest_pair(test_list_cluster)
'''

