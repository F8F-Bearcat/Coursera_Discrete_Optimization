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
    #size = len(cluster_list)
    copy_clusters = [c.copy() for c in cluster_list]

    cluster_centers = []
    copy_clusters.sort(key=lambda cluster: len(cluster.fips_codes()))
    largest_initial_clusters = copy_clusters[-num_clusters:]
    for cluster in largest_initial_clusters:
        cluster_centers.append([cluster.horiz_center(), cluster.vert_center()])

    for item in range(num_iterations):
        ret_clusters = []
        for count in range(num_clusters):
            ret_clusters.append(alg_cluster.Cluster(set([]), 0, 0, 0, 0))

        for loop in range(len(cluster_list)):
            min_dist = float('inf')
            corresponding_index = -1
            check_clust_dist_x = copy_clusters[loop].horiz_center()
            check_clust_dist_y = copy_clusters[loop].vert_center()
            check_me = (check_clust_dist_x, check_clust_dist_y)
            #print 'cluster_centers are '
            #print cluster_centers
            for point in cluster_centers:
                #print 'index is ', cluster_centers.index(point)
                #print 'point[0] and type(point[0]) are ', point[0], type(point[0])
                #print 'check_me[0] and type(check_me[0]) are ', check_me[0], type(check_me[0])
                #print 'blah'
                #print 'blah'
                #print 'blah'
                compare_dist_squared = (point[0]-check_me[0])**2 + (point[1]-check_me[1])**2
                if compare_dist_squared < min_dist:
                    min_dist = compare_dist_squared
                    corresponding_index = cluster_centers.index(point)
            ret_clusters[corresponding_index].merge_clusters(copy_clusters[loop])

            for index_center in range(num_clusters):
                new_x = ret_clusters[index_center].horiz_center()
                new_y = ret_clusters[index_center].vert_center()
                cluster_centers[index_center] = [new_x, new_y]

    return ret_clusters
