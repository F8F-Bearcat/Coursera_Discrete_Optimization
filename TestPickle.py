import pickle

file_name_string = 'C:/Users/Dad/Documents/GitHub/Coursera_Discrete_Optimization/citations.p'
file_h = open(file_name_string, 'r')
citation_graph = pickle.load(file_h)
print citation_graph[1001]
