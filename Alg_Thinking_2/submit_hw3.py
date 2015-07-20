'''
This is the submit_hw3.py script
It needs to include slow_closest_pair, closest_pair_strip, fast_closest_pair, hierarchial_clusering
and kmeans_clustering
and meet pylint coding guidelines
'''
import math
#import itertools

def euclid_dist(p_one, p_two):
    '''
    Input: two tuples each representing a point in an x-y plane, format (x,y) - first item x
    Output: The euclidian distance between the two points
    Calculates euclidian distance between two points in a plane: math.sqrt((x0-x1)**2 +(y0-y1)**2)
    '''
    #assert len(p_one) == len(p_two), 'the two input points need the same dimension'
    #assert len(p_one) == 2, 'both inputs need two coordinates'
    return math.sqrt((p_one[0]-p_two[0])**2 + (p_one[1]-p_two[1])**2)

def slow_closest_pair(list_of_points):
    '''
    Input: a list of points
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_points
            and i and j are the indexes of the two points that are the closest together
    '''
    ret_list = [float('inf'), -1, -1]
    #all_combinations_two_points = [list(x) for x in itertools.combinations(list_of_points, 2)]
    all_combinations_two_points = []
    for point in list_of_points:
        if list_of_points.index(point) == len(list_of_points)-1:
            break
        init_item_y = list_of_points.index(point)+1
        for item_y in range(init_item_y, len(list_of_points)):
            all_combinations_two_points.append((point, list_of_points[item_y]))
    #print all_combinations_two_points
    for item in all_combinations_two_points:
        distance = euclid_dist(item[0], item[1])
        if distance < ret_list[0]:   # if true, a new minimum distance has been found
            ret_list[0] = distance
            ret_list[1] = list_of_points.index(item[0])
            ret_list[2] = list_of_points.index(item[1])
            low_index = list_of_points.index(item[0])
            hi_index = list_of_points.index(item[1])
            assert low_index < hi_index, 'index order small to large'
    return tuple(ret_list)
