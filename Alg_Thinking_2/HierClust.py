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

    while len(copy_clusters) > final_cluster_count:
        copy_clusters.sort(key=lambda cluster: cluster.horiz_center())  # sort just before needed
        closest_clusters = FastClosestPair.fast_closest_pair(copy_clusters)
        lower_index_cluster = copy_clusters[closest_clusters[1]]
        higher_index_cluster = copy_clusters[closest_clusters[2]]
        lower_index_cluster.merge_clusters(higher_index_cluster)
        copy_clusters.remove(higher_index_cluster)

    return copy_clusters
