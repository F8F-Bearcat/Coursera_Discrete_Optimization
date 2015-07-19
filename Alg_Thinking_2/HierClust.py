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
        cc = cluster_class.Cluster(95014, point[0], point[1], 1000, .001)
        cluster_list.append(cc)
    i = 0
    while len(cluster_list) > final_cluster_count:
        list_of_points = []
        for item in cluster_list:
            list_of_points.append((item.horiz_center(), item.vert_center()))
        closest_clusters = FastClosestPair.FastClosestPair(list_of_points)
        print closest_clusters
        i += 1
        if i == 10:
            break

    pass
