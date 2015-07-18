'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the FastClosestPair function from Homework 3, Project 3
'''
import math
import itertools
import random
import SlowClosestPair

def ClosestPairStrip(list_of_points, mid, dee):
    '''
    Input: a list of points, the x location of the split plane, and dee is half the strip width
    Output: tuple (d, i, j) representing the closest points in the middle closest_strip_tuple
    '''
    points_in_strip = []
    for point in list_of_points:
        if (abs(point[0]-mid)) < dee:
            points_in_strip.append(point)

    points_in_strip.sort(key=lambda x: x[1])  # non decreasing order
    #print 'mid is ', mid
    #print 'dee is ', dee
    #print 'points_in_strip are '
    #print points_in_strip
    #print 'list of points are ', list_of_points
    
    strip_point_count = len(points_in_strip)
    ret_tuple = (float('inf'), -1, -1)

    for check in range(strip_point_count-2):
        terminate = min(check+3, strip_point_count-1)
        vee = check + 1
        for item in range(vee, terminate + 1):
            strip_tuple = SlowClosestPair.SlowClosestPair([points_in_strip[check], points_in_strip[item]])
            if strip_tuple[0] < ret_tuple[0]:
                ret_tuple = strip_tuple

    return ret_tuple  # this is a placeholder for testing FastClosestPair

def FastClosestPair(list_of_points):
    '''
    Input: a list of points
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_points
            and i and j are the indexes of the two points that are the closest together
    '''
    size = len(list_of_points)
    if size < 4:
        ret_tuple = SlowClosestPair.SlowClosestPair(list_of_points)
    else:
        split = int(math.floor(size/2.0))
        #print 'split is ', split
        left = list_of_points[:split]
        right = list_of_points[split:]
        left_tuple = FastClosestPair(left)
        right_tuple = FastClosestPair(right)
        right_list = list(right_tuple)
        right_list[1] += split
        right_list[2] += split
        right_tuple = tuple(right_list)
        if left_tuple[0] < right_tuple[0]:
            left_and_right_min_tuple = left_tuple
        else:
            left_and_right_min_tuple = right_tuple
        middle = .5*(list_of_points[split-1][0] + list_of_points[split][0])
        closest_strip_tuple = ClosestPairStrip(list_of_points, middle, left_and_right_min_tuple[0])
        #print 'd is ', left_and_right_min_tuple[0]
        #print 'left_and_right_min_tuple[0] is ', left_and_right_min_tuple[0]
        #print 'closest_strip_tuple[0] is ', closest_strip_tuple[0]
        if left_and_right_min_tuple[0] < closest_strip_tuple[0]:
            ret_tuple = left_and_right_min_tuple
        else:
            ret_tuple = closest_strip_tuple
    return ret_tuple

'''
p01 = cluster_class.Cluster(95014, 0, 0, 100, .5)
p02 = cluster_class.Cluster(95014, 0, 1, 100, .5)
p03 = cluster_class.Cluster(95014, 1, 1, 100, .5)

test_list = [p01, p02, p03]

print SlowClosestPair.SlowClosestPair(test_list)
'''
'''
p01 = (0, 0)
p02 = (0, 1)
p03 = (1, 1)
p04 = (1, 0)
p05 = (-1, 1)
p06 = (-1, 0)
p07 = (-1, -1)
p08 = (0, -1)
p09 = (1, -1)
p10 = (1, 1.1)


test_list = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]

for element in range(10):
    random.shuffle(test_list)
    test_list.sort()
    print test_list
    print FastClosestPair(test_list)

#print SlowClosestPair(test_list)
'''
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
'''