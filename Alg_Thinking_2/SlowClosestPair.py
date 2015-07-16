'''
For Algorithmic Thinking Part 2 - Coursera class
This script implements the SlowClosestPair function from Homework 3, Project 3
'''
import math
import itertools
import random

class Cluster:
    """
    Class for creating and merging clusters of counties
    """
    
    def __init__(self, fips_codes, horiz_pos, vert_pos, population, risk):
        """
        Create a cluster based the models a set of counties' data
        """
        self._fips_codes = fips_codes
        self._horiz_center = horiz_pos
        self._vert_center = vert_pos
        self._total_population = population
        self._averaged_risk = risk
        
        
    def __repr__(self):
        """
        String representation assuming the module is "alg_cluster".
        """
        rep = "alg_cluster.Cluster("
        rep += str(self._fips_codes) + ", "
        rep += str(self._horiz_center) + ", "
        rep += str(self._vert_center) + ", "
        rep += str(self._total_population) + ", "
        rep += str(self._averaged_risk) + ")"
        return rep


    def fips_codes(self):
        """
        Get the cluster's set of FIPS codes
        """
        return self._fips_codes
    
    def horiz_center(self):
        """
        Get the averged horizontal center of cluster
        """
        return self._horiz_center
    
    def vert_center(self):
        """
        Get the averaged vertical center of the cluster
        """
        return self._vert_center
    
    def total_population(self):
        """
        Get the total population for the cluster
        """
        return self._total_population
    
    def averaged_risk(self):
        """
        Get the averaged risk for the cluster
        """
        return self._averaged_risk
   
        
    def copy(self):
        """
        Return a copy of a cluster
        """
        copy_cluster = Cluster(set(self._fips_codes), self._horiz_center, self._vert_center,
                               self._total_population, self._averaged_risk)
        return copy_cluster


    def distance(self, other_cluster):
        """
        Compute the Euclidean distance between two clusters
        """
        vert_dist = self._vert_center - other_cluster.vert_center()
        horiz_dist = self._horiz_center - other_cluster.horiz_center()
        return math.sqrt(vert_dist ** 2 + horiz_dist ** 2)
        
    def merge_clusters(self, other_cluster):
        """
        Merge one cluster into another
        The merge uses the relatively populations of each
        cluster in computing a new center and risk
        
        Note that this method mutates self
        """
        if len(other_cluster.fips_codes()) == 0:
            return self
        else:
            self._fips_codes.update(set(other_cluster.fips_codes()))
 
            # compute weights for averaging
            self_weight = float(self._total_population)                        
            other_weight = float(other_cluster.total_population())
            self._total_population = self._total_population + other_cluster.total_population()
            self_weight /= self._total_population
            other_weight /= self._total_population
                    
            # update center and risk using weights
            self._vert_center = self_weight * self._vert_center + other_weight * other_cluster.vert_center()
            self._horiz_center = self_weight * self._horiz_center + other_weight * other_cluster.horiz_center()
            self._averaged_risk = self_weight * self._averaged_risk + other_weight * other_cluster.averaged_risk()
            return self

    def cluster_error(self, data_table):
        """
        Input: data_table is the original table of cancer data used in creating the cluster.
        
        Output: The error as the sum of the square of the distance from each county
        in the cluster to the cluster center (weighted by its population)
        """
        # Build hash table to accelerate error computation
        fips_to_line = {}
        for line_idx in range(len(data_table)):
            line = data_table[line_idx]
            fips_to_line[line[0]] = line_idx
        
        # compute error as weighted squared distance from counties to cluster center
        total_error = 0
        counties = self.fips_codes()
        for county in counties:
            line = data_table[fips_to_line[county]]
            singleton_cluster = Cluster(set([line[0]]), line[1], line[2], line[3], line[4])
            singleton_distance = self.distance(singleton_cluster)
            total_error += (singleton_distance ** 2) * singleton_cluster.total_population()
        return total_error

def euclid_dist(pOne, pTwo):
    '''
    Input: two tuples each representing a point in an x-y plane, format (x,y) - first item x
    Output: The euclidian distance between the two points
    Calculates euclidian distance between two points in a plane: math.sqrt((x0-x1)**2 +(y0-y1)**2)
    '''
    assert len(pOne) == len(pTwo), 'the two input points need the same dimension'
    assert len(pOne) == 2, 'both inputs need two coordinates'
    return math.sqrt((pOne[0]-pTwo[0])**2 + (pOne[1]-pTwo[1])**2)

def SlowClosestPair(list_of_clusters):
    '''
    Input: a list of points
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Note **** this function will need to change later to a list of CLUSTERS and methods will need
    to be used to pull out the x and y locations
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_clusters
            and i and j are the indexes of the two points that are the closest together
    '''
    ret_list = [float('inf'), -1, -1]
    all_combinations_two_points = [list(x) for x in itertools.combinations(list_of_clusters, 2)]
    for item in all_combinations_two_points:
        distance = item[0].distance(item[1])
        if distance < ret_list[0]:   # if true, a new minimum distance has been found
            ret_list[0] = distance
            ret_list[1] = list_of_clusters.index(item[0])
            ret_list[2] = list_of_clusters.index(item[1])
            assert list_of_clusters.index(item[0]) < list_of_clusters.index(item[1]), 'index order small to large'
    return tuple(ret_list)

p01 = Cluster(95014, 0, 0, 100, .5)
p02 = Cluster(95014, 0, 1, 100, .5)
p03 = Cluster(95014, 1, 1, 100, .5)
p04 = Cluster(95014, 1, 0, 100, .5)
p05 = Cluster(95014, -1, 1, 100, .5)
p06 = Cluster(95014, -1, 0, 100, .5)
p07 = Cluster(95014, -1, -1, 100, .5)
p08 = Cluster(95014, 0, -1, 100, .5)
p09 = Cluster(95014, 1, -1, 100, .5)
p10 = Cluster(95014, 1, 1.1, 100, .5)

test_list = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]

for element in range(100000):
    random.shuffle(test_list)
    print SlowClosestPair(test_list)

#print SlowClosestPair(test_list)