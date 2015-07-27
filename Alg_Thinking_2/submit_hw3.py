'''
This is the submit_hw3.py script
It needs to include slow_closest_pair, closest_pair_strip, fast_closest_pair, hierarchial_clusering
and kmeans_clustering
and meet pylint coding guidelines
'''
import math
import alg_cluster

def euclid_dist(p_one, p_two):
    '''
    Input: two tuples each representing a point in an x-y plane, format (x,y) - first item x
    Output: The euclidian distance between the two points
    Calculates euclidian distance between two points in a plane: math.sqrt((x0-x1)**2 +(y0-y1)**2)
    '''
    assert len(p_one) == len(p_two), 'the two input points need the same dimension'
    assert len(p_one) == 2, 'both inputs need two coordinates'
    return math.sqrt((p_one[0]-p_two[0])**2 + (p_one[1]-p_two[1])**2)

def slow_closest_pair(list_of_clusters):
    '''
    Input: a list of clusters
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_clusters
            and i and j are the indexes of the two points that are the closest together
    '''
    ret_list = [float('inf'), -1, -1]
    #all_combinations_two_points = [list(x) for x in itertools.combinations(list_of_clusters, 2)]
    all_combinations_two_clusters = []
    for cluster in list_of_clusters:
        if list_of_clusters.index(cluster) == len(list_of_clusters)-1:
            break
        next_cl_index = list_of_clusters.index(cluster)+1
        for item_y in range(next_cl_index, len(list_of_clusters)):
            all_combinations_two_clusters.append((cluster, list_of_clusters[item_y]))
    #print all_combinations_two_clusters
    for cluster_tuple in all_combinations_two_clusters:
        points = []
        for cluster in cluster_tuple:
            points.append([cluster.horiz_center(), cluster.vert_center()])
        distance = euclid_dist(points[0], points[1])
        if distance < ret_list[0]:   # if true, a new minimum distance has been found
            ret_list[0] = distance
            ret_list[1] = list_of_clusters.index(cluster_tuple[0])
            ret_list[2] = list_of_clusters.index(cluster_tuple[1])
            low_index = list_of_clusters.index(cluster_tuple[0])
            hi_index = list_of_clusters.index(cluster_tuple[1])
            assert low_index < hi_index, 'index order small to large'
    return tuple(ret_list)

def closest_pair_strip(list_of_clusters, mid, dee):
    '''
    Input: a list of points, the x location of the split plane, and dee is half the strip width
    Output: tuple (d, i, j) representing the closest points in the middle closest_strip_tuple
    '''
    clusters_in_strip = []
    for cluster in list_of_clusters:
        if (abs(cluster.horiz_center()-mid)) < dee:
            clusters_in_strip.append(cluster)

    clusters_in_strip.sort(key=lambda cluster: cluster.vert_center())  # non decreasing order

    strip_point_count = len(clusters_in_strip)
    ret_tuple = (float('inf'), -1, -1)

    for cluster in clusters_in_strip:
        if clusters_in_strip.index(cluster) == strip_point_count - 1:
            break
        else:
            for check in range(1, 4):  # check 3 points
                r_idx = clusters_in_strip.index(cluster)+check
                if (r_idx) == strip_point_count:
                    break
                else:
                    strip_t = slow_closest_pair([cluster, clusters_in_strip[r_idx]])
                    if strip_t[0] < ret_tuple[0]:
                        answer_list = []
                        answer_list.append(strip_t[0])
                        #put the indices in increasing order
                        first_cl_index = list_of_clusters.index(cluster)
                        second_cl_index = list_of_clusters.index(clusters_in_strip[r_idx])
                        if first_cl_index < second_cl_index:
                            answer_list.append(list_of_clusters.index(cluster))
                            answer_list.append(list_of_clusters.index(clusters_in_strip[r_idx]))
                        else:
                            answer_list.append(list_of_clusters.index(clusters_in_strip[r_idx]))
                            answer_list.append(list_of_clusters.index(cluster))
                        ret_tuple = tuple(answer_list)

    return ret_tuple

def fast_closest_pair(list_of_clusters):
    '''
    Input: a list of clusters
    Output: a tuple (d, i, j) where d is the smallest between any of the points in list_of_clusters
            and i and j are the indexes of the two points that are the closest together
    '''
    size = len(list_of_clusters)
    if size < 4:
        ret_tuple = slow_closest_pair(list_of_clusters)
    else:
        split = int(math.floor(size/2.0))
        left = list_of_clusters[:split]
        right = list_of_clusters[split:]
        left_tuple = fast_closest_pair(left)
        right_tuple = fast_closest_pair(right)
        right_list = list(right_tuple)
        right_list[1] += split
        right_list[2] += split
        right_tuple = tuple(right_list)
        if left_tuple[0] < right_tuple[0]:
            l_and_r_min_tuple = left_tuple
        else:
            l_and_r_min_tuple = right_tuple
        m_minus_one = list_of_clusters[split-1].horiz_center()
        m_itself = list_of_clusters[split].horiz_center()
        middle = .5*(m_minus_one + m_itself)
        closest_strip_tuple = closest_pair_strip(list_of_clusters, middle, l_and_r_min_tuple[0])
        if l_and_r_min_tuple[0] < closest_strip_tuple[0]:
            ret_tuple = l_and_r_min_tuple
        else:
            ret_tuple = closest_strip_tuple
    return ret_tuple


def hierarchical_clustering(cluster_list, final_cluster_count):
    '''
    Input: list of points to build clusters around, and a final target number of clusters
    Output: a list with final_cluster_count number of clusters
    '''
    copy_clusters = [c.copy() for c in cluster_list]
    '''
    cluster_list = []
    for point in point_list:
        cc = cluster_class.Cluster(set([95014]), point[0], point[1], 1000, .001)
        cluster_list.append(cc)
    i = 0
    '''
    while len(copy_clusters) > final_cluster_count:
        #print 'copy_clusters is ', copy_clusters
        copy_clusters.sort(key=lambda cluster: cluster.horiz_center())  # sort just before needed
        closest_clusters = fast_closest_pair(copy_clusters)
        #print 'closest_clusters are ', closest_clusters
        lower_index_cluster = copy_clusters[closest_clusters[1]]
        #print 'lower_index_cluster is ', lower_index_cluster
        higher_index_cluster = copy_clusters[closest_clusters[2]]
        #print 'higher_index_cluster is ', higher_index_cluster
        lower_index_cluster.merge_clusters(higher_index_cluster)
        #print 'lower_index_cluster after merge is ', lower_index_cluster
        #print 'copy_clusters is ', copy_clusters
        copy_clusters.remove(higher_index_cluster)
        #print 'copy_clusters after removal of higher index ', copy_clusters
        #print 'copy_clusters after removal of higher index and sort ', copy_clusters

    return copy_clusters

def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    '''
    Input: list of clusters, a final target number of clusters and a number of iterations
    Output: a list with num_clusters number of clusters
    '''
    #size = len(cluster_list)
    copy_clusters = [c.copy() for c in cluster_list]

    cluster_centers = []
    copy_clusters.sort(key=lambda cluster: cluster.total_population(), reverse=True)
    largest_initial_clusters = copy_clusters[:num_clusters]
    for cluster in largest_initial_clusters:
        cluster_centers.append([cluster.horiz_center(), cluster.vert_center()])

    for item in range(num_iterations):
        ret_clusters = []
        for count in range(num_clusters):
            ret_clusters.append(alg_cluster.Cluster(set([]), 0, 0, 0, 0).copy())

        merge_indexes = []
        for loop in range(len(cluster_list)):
            #print 'loop, ret_clusters '
            #print loop, ret_clusters
            min_dist = float('inf')
            corresponding_index = -1
            check_clust_dist_x = copy_clusters[loop].horiz_center()
            check_clust_dist_y = copy_clusters[loop].vert_center()
            check_me = (check_clust_dist_x, check_clust_dist_y)
            #print 'cluster_centers are '
            #print cluster_centers
            # Format list of lists: [ [to, from], etc] use the merge method
            # to merge the from cluster into the to cluster
            if (item == 0) and (loop < num_clusters):
                merge_indexes.append([loop, loop])
                #print 'merge_indexes is ', merge_indexes
            else:
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
                merge_indexes.append([corresponding_index, loop])

            # update/merge all the clusters now, then create the new cluster centers
            #print 'merge_indexes prior to cluster merge are '
            #print merge_indexes
            last_loop = len(cluster_list)-1
            if loop == last_loop:
                for ele in merge_indexes:
                    ##print 'ele is ', ele
                    ##print 'merge into this ', ret_clusters[ele[0]].fips_codes()
                    ##print 'from this ', copy_clusters[ele[1]].fips_codes()
                    #print ' '
                    #print 'ele is ', ele
                    #print 'index, ele[0] is ', merge_indexes.index(ele), ele[0]
                    #print 'index, ele[1] is ', merge_indexes.index(ele), ele[1]
                    ret_clusters[ele[0]].merge_clusters(copy_clusters[ele[1]])
                # create the new cluster_centers
                for index_center in range(num_clusters):
                    new_x = ret_clusters[index_center].horiz_center()
                    new_y = ret_clusters[index_center].vert_center()
                    cluster_centers[index_center] = [new_x, new_y]
                # make a new set of copy clusters
                copy_clusters = [c.copy() for c in cluster_list]

    return ret_clusters
