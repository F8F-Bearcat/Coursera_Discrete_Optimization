'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the SlowClosestPair function from Homework 3, Project 3
'''
import math
import itertools
import FastClosestPair
import alg_cluster
import random


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    '''
    Input: list of clusters, a final target number of clusters and a number of iterations
    Output: a list with num_clusters number of clusters
    '''
    size = len(cluster_list)
    copy_clusters = [c.copy() for c in cluster_list]

    cluster_centers = []
    copy_clusters.sort(key=lambda cluster: len(cluster.fips_codes()))
    largest_initial_clusters = copy_clusters[-num_clusters:]
    for cluster in largest_initial_clusters:
        cluster_centers.append([cluster.horiz_center(), cluster.vert_center()])
    remaining_clusters = copy_clusters[:len(copy_clusters)-num_clusters]

    for item in range(1, num_iterations+1):
        ret_clusters = []
        for count in range(1, num_clusters+1):
            ret_clusters.append(alg_cluster.Cluster(set([]), 0, 0, 0, 0))

        for loop in range(len(size)):
            min_dist = float('inf')
            corresponding_index = -1
            check_clust_dist_x = copy_clusters[loop].horiz_center
            check_clust_dist_y = copy_clusters[loop].vert_center
            check_me = (check_clust_dist_x, check_clust_dist_y)
            for point in cluster_centers:
                compare_dist_squared = (point[0]-check_me[0])**2 + (point[1]-check_me[1])**2
                if compare_dist_squared < min_dist:
                    min_dist = compare_dist_squared
                    corresponding_index = cluster_centers.index(point)
            ret_clusters[corresponding_index].merge_clusters(copy_clusters[loop])
            pass

    return ret_clusters
