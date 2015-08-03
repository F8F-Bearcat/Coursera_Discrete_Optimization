'''
Module comments
'''
def score_alignment(seq_x, seq_y, scoring_matrix):
    '''
    Inputs:
    Outputs:
    '''
    if min(len(seq_x), len(seq_y)) == 0:
        return 0

    score = 0
    for pointer in range(len(seq_x)):
        score += scoring_matrix[seq_x[pointer]][seq_y[pointer]]

    return score

def compute_local_alignment(seq_x, seq_y, score_m, align_m):
    '''
    Inputs:
    Outputs:
    '''
    len_x = len(seq_x)
    len_y = len(seq_y)
    if min(len_x, len_y) == 0:
        return (0, '', '')       # check for the null input case to find expected return format

    # find maximum entry in the alignment matrix
    x_index_max, y_index_max = -1, -1
    max_val = -float('inf')

    for entry in align_m:
        if max(entry) > max_val:
            max_val = max(entry)
            x_index_max = align_m.index(entry)
    y_index_max = align_m[x_index_max].index(max_val)

    x_prime, y_prime = '', ''
    len_x = x_index_max
    len_y = y_index_max

    while len_x > 0 and len_y > 0:
        score = score_m[seq_x[len_x-1]][seq_y[len_y-1]]
        if align_m[len_x][len_y] == align_m[len_x-1][len_y-1]+score:
            x_prime = seq_x[len_x-1] + x_prime
            y_prime = seq_y[len_y-1] + y_prime
            len_x -= 1
            len_y -= 1
            if align_m[len_x][len_y] == 0:
                return (score_alignment(x_prime, y_prime, score_m), x_prime, y_prime)
        else:
            score = score_m[seq_x[len_x-1]]['-']
            if align_m[len_x][len_y] == align_m[len_x-1][len_y]+score:
                x_prime = seq_x[len_x-1] + x_prime
                y_prime = '-' + y_prime
                len_x -= 1
                if align_m[len_x][len_y] == 0:
                    return (score_alignment(x_prime, y_prime, score_m), x_prime, y_prime)
            else:
                x_prime = '-' + x_prime
                y_prime = seq_y[len_y-1] + y_prime
                len_y -= 1
                if align_m[len_x][len_y] == 0:
                    return (score_alignment(x_prime, y_prime, score_m), x_prime, y_prime)
    while len_x > 0:
        x_prime = seq_x[len_x-1] + x_prime
        y_prime = '-' + y_prime
        len_x -= 1
        if align_m[len_x][0] == 0:
            return (score_alignment(x_prime, y_prime, score_m), x_prime, y_prime)

    while len_y > 0:
        x_prime = '-' + x_prime
        y_prime = seq_y[len_y-1] + y_prime
        len_y -= 1
        if align_m[0][len_y] == 0:
            return (score_alignment(x_prime, y_prime, score_m), x_prime, y_prime)

    return None  #should never get here


result = compute_local_alignment('ATG', 'ACG', {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}, [[0, -4, -8, -12], [-4, 6, 2, -2], [-8, 2, 8, 4], [-12, -2, 4, 14]])
'''
returned incorrect score, expected 14 but received 6
'''
print result
result = compute_local_alignment('ACTACT', 'AGCTA', {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 2, 2], [0, 2, 3, 4, 4, 4], [0, 2, 3, 4, 6, 6], [0, 2, 3, 4, 6, 8], [0, 2, 3, 5, 6, 8], [0, 2, 3, 5, 7, 8]])
#expected ({'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, 
#(8, 'ACTACT', 'AGCTA')
#, True) but received (Exception: IndexError) "string index out of range" at line 45, in compute_global_alignment
print result