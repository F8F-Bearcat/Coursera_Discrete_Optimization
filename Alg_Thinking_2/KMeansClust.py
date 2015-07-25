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
    copy_clusters.sort(key=lambda cluster: len(cluster.fips_codes()))
    cluster_list = copy_clusters[-num_clusters:]
    cluster_centers = []
    for cluster in cluster_list:
        cluster_centers.append([cluster.horiz_center(), cluster.vert_center()])

    for item in range(1, num_iterations+1):
        ret_clusters = []
        for empty in range(1, num_clusters+1):
            ret_clusters.append(alg_cluster.Cluster(set([]), 0, 0, 0, 0))
        for loop in range(size):
            pass

    return ret_clusters
