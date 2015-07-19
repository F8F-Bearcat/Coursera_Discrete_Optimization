'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the SlowClosestPair function from Homework 3, Project 3
'''
import math
import itertools
import FastClosestPair
import cluster_class

def HierClust(point_list, final_cluster_count):
    '''
    Input: list of points to build clusters around, and a final target number of clusters
    Output: a list with final_cluster_count number of clusters
    '''
    size = len(point_list)
    cluster_list = []
    for point in point_list:
        cc = cluster_class.Cluster(set([95014]), point[0], point[1], 1000, .001)
        cluster_list.append(cc)
    i = 0
    while len(cluster_list) > final_cluster_count:
        list_of_points = []
        for item in cluster_list:
            list_of_points.append((item.horiz_center(), item.vert_center()))
        closest_clusters = FastClosestPair.FastClosestPair(list_of_points)
        print closest_clusters
        lower_index_cluster = cluster_list[closest_clusters[1]]
        higher_index_cluster = cluster_list[closest_clusters[2]]
        lower_index_cluster.merge_clusters(higher_index_cluster)
        cluster_list.remove(higher_index_cluster)

    return cluster_list
