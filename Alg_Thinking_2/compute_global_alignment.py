'''
Module comments
'''
def compute_global_alignment(seq_x, seq_y, score_m, align_m):
    '''
    Inputs:
    Outputs:
    '''
    len_x = len(seq_x)
    len_y = len(seq_y)
    if min(len_x, len_y) == 0:
        return (0, '', '')       # check for the null input case to find expected return format

    x_prime, y_prime = '', ''

    while len_x > 0 and len_y > 0:
        score = score_m[seq_x[len_x-1]][seq_y[len_y-1]]
        if align_m[len_x][len_y] == align_m[len_x-1][len_y-1]+score:
            x_prime = seq_x[len_x-1] + x_prime
            y_prime = seq_y[len_y-1] + y_prime
            len_x -= 1
            len_y -= 1
        else:
            score = score_m[seq_x[len_x-1]]['-']
            if align_m[len_x][len_y] == align_m[len_x-1][len_y]+score:
                x_prime = seq_x[len_x-1] + x_prime
                y_prime = '-' + y_prime
                len_x -= 1
            else:
                x_prime = '-' + x_prime
                y_prime = seq_y[len_y-1] + y_prime
                len_y -= 1
    while len_x > 0:
        x_prime = seq_x[len_x-1] + x_prime
        y_prime = '-' + y_prime
        len_x -= 1

    while len_y > 0:
        x_prime = '-' + x_prime
        y_prime = seq_y[len_y-1] + y_prime
        len_y -= 1

    #print 'len(x_prime) is ', len(x_prime)
    #print 'len(seq_x) is ', len(seq_x)
    #print 'len(seq_y) is ', len(seq_y)
    alignment_score = 0
    for index in range(len(x_prime)):
        alignment_score += score_m[x_prime[index]][y_prime[index]]

    return (alignment_score, x_prime, y_prime)


#result = compute_global_alignment('ATG', 'ACG', {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}, [[0, -4, -8, -12], [-4, 6, 2, -2], [-8, 2, 8, 4], [-12, -2, 4, 14]])
'''
returned incorrect score, expected 14 but received 6
'''
#print result
#result = compute_global_alignment('ACTACT', 'AGCTA', {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 2, 2], [0, 2, 3, 4, 4, 4], [0, 2, 3, 4, 6, 6], [0, 2, 3, 4, 6, 8], [0, 2, 3, 5, 6, 8], [0, 2, 3, 5, 7, 8]])
#expected ({'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, 
#(8, 'ACTACT', 'AGCTA')
#, True) but received (Exception: IndexError) "string index out of range" at line 45, in compute_global_alignment
#print result