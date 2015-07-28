'''
Module reads in data from csv file and populates cluster objects from Algorithimic Thinking pt 2
'''
import csv
import alg_cluster

def csv_to_cl():
    '''
    reads csv file and makes a list of singleton cluster_list
    '''
    CANCER_DATA = 'C://Users//andyd//Desktop//unifiedCancerData_3108.csv'  #This is the file primarly used
    FILE_HANDLE = open(CANCER_DATA, 'r')
    reader = csv.reader(FILE_HANDLE)

    cluster_list = []
    for row in reader:
        new_cluster = alg_cluster.Cluster(set([row[0]]), float(row[1]), float(row[2]), int(row[3]), float(row[4]))
        cluster_list.append(new_cluster)

    FILE_HANDLE.close()

    return cluster_list


#print csv_to_cl()
