'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the SlowClosestPair function from Homework 3, Project 3
'''
import math
import itertools
import FastClosestPair
import alg_cluster
import random


def KMeansClust(cluster_list, num_clusters, num_iterations):
    '''
    Input: list of clusters, a final target number of clusters and a number of iterations
    Output: a list with num_clusters number of clusters
    '''
    size = len(cluster_list)
    copy_clusters = [c.copy() for c in cluster_list]
    copy_clusters.sort(key=lambda cluster: len(cluster.fips_codes()))
    cluster_list = copy_clusters[-num_clusters:]
    cluster_centers = []
    for cluster in cluster_list:
        cluster_centers.append([cluster.horiz_center(), cluster.vert_center()])

    for item in range(1, num_iterations+1):
        ret_clusters = []
        for empty in range(1, num_clusters+1):
            ret_clusters.append(alg_cluster.Cluster(set([]), 0, 0, 0, 0)
        for loop_1 in range(size):
            


    
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
        cluster_list.sort(key=lambda cluster: cluster.horiz_center())

    return cluster_list
