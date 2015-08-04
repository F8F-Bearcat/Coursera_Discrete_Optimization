'''
Computes mean and std dev of distribution dictionary
'''
import numpy as np

dist_dict = {37: 1, 38: 1, 39: 4, 40: 8, 41: 22, 42: 19, 43: 33, 44: 42, 45: 53, 46: 83, 47: 50, 48: 73, 49: 63, 50: 59, 51: 62, 52: 57, 53: 58, 54: 34, 55: 39, 56: 33, 57: 25, 58: 27, 59: 19, 60: 27, 61: 18, 62: 17, 63: 14, 64: 6, 65: 9, 66: 8, 67: 8, 68: 3, 69: 5, 70: 2, 71: 2, 72: 1, 73: 4, 74: 2, 76: 2, 77: 1, 79: 2, 80: 1, 81: 1, 85: 1, 86: 1}


scores = []

for entry in dist_dict:
    for index in range(dist_dict[entry]):
        scores.append(entry)

print 'number of scores is ', len(scores)
print scores


mean = np.mean(scores)
standard_deviation = np.std(scores)

print 'mean is ', mean
print 'standard_deviation is ', standard_deviation