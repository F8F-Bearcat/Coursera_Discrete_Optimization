'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the SlowClosestPair function from Homework 3, Project 3
'''
import math
import itertools
import FastClosestPair
import cluster_class

def hierarchical_clustering(cluster_list, final_cluster_count):
    '''
    Input: list of points to build clusters around, and a final target number of clusters
    Output: a list with final_cluster_count number of clusters
    '''
    copy_clusters = [c.copy() for c in cluster_list]
    '''
    cluster_list = []
    for point in point_list:
        cc = cluster_class.Cluster(set([95014]), point[0], point[1], 1000, .001)
        cluster_list.append(cc)
    i = 0
    '''
    while len(copy_clusters) > final_cluster_count:
        #print 'copy_clusters is ', copy_clusters
        closest_clusters = FastClosestPair.fast_closest_pair(copy_clusters)
        #print 'closest_clusters are ', closest_clusters
        lower_index_cluster = copy_clusters[closest_clusters[1]]
        #print 'lower_index_cluster is ', lower_index_cluster
        higher_index_cluster = copy_clusters[closest_clusters[2]]
        #print 'higher_index_cluster is ', higher_index_cluster
        lower_index_cluster.merge_clusters(higher_index_cluster)
        #print 'lower_index_cluster after merge is ', lower_index_cluster
        #print 'copy_clusters is ', copy_clusters
        copy_clusters.remove(higher_index_cluster)
        #print 'copy_clusters after removal of higher index ', copy_clusters
        copy_clusters.sort(key=lambda cluster: cluster.horiz_center())
        #print 'copy_clusters after removal of higher index and sort ', copy_clusters

    return copy_clusters
