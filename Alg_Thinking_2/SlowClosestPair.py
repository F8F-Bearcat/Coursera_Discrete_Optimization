'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the SlowClosestPair function from Homework 3, Project 3
'''
import math
import itertools
import random
import cluster_class

def euclid_dist(pOne, pTwo):
    '''
    Input: two tuples each representing a point in an x-y plane, format (x,y) - first item x
    Output: The euclidian distance between the two points
    Calculates euclidian distance between two points in a plane: math.sqrt((x0-x1)**2 +(y0-y1)**2)
    '''
    assert len(pOne) == len(pTwo), 'the two input points need the same dimension'
    assert len(pOne) == 2, 'both inputs need two coordinates'
    return math.sqrt((pOne[0]-pTwo[0])**2 + (pOne[1]-pTwo[1])**2)

def SlowClosestPair(list_of_points):
    '''
    Input: a list of points
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_points
            and i and j are the indexes of the two points that are the closest together
    '''
    ret_list = [float('inf'), -1, -1]
    all_combinations_two_points = [list(x) for x in itertools.combinations(list_of_points, 2)]
    for item in all_combinations_two_points:
        distance = euclid_dist(item[0], item[1])
        if distance < ret_list[0]:   # if true, a new minimum distance has been found
            ret_list[0] = distance
            ret_list[1] = list_of_points.index(item[0])
            ret_list[2] = list_of_points.index(item[1])
            assert list_of_points.index(item[0]) < list_of_points.index(item[1]), 'index order small to large'
    return tuple(ret_list)
'''
p01 = cluster_class.Cluster(95014, 0, 0, 100, .5)
p02 = cluster_class.Cluster(95014, 0, 1, 100, .5)
p03 = cluster_class.Cluster(95014, 1, 1, 100, .5)
p04 = cluster_class.Cluster(95014, 1, 0, 100, .5)
p05 = cluster_class.Cluster(95014, -1, 1, 100, .5)
p06 = cluster_class.Cluster(95014, -1, 0, 100, .5)
p07 = cluster_class.Cluster(95014, -1, -1, 100, .5)
p08 = cluster_class.Cluster(95014, 0, -1, 100, .5)
p09 = cluster_class.Cluster(95014, 1, -1, 100, .5)
p10 = cluster_class.Cluster(95014, 1, 1.1, 100, .5)

test_list = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]

for element in range(100000):
    random.shuffle(test_list)
    print SlowClosestPair(test_list)

#print SlowClosestPair(test_list)
'''