'''
Computes alignment matrix for HW 4
'''
def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    '''
    Input: set alphabet, diag_score for alphabet char that match, off_diag_score for no match
           dash_score when there is a dash, or 'indel' (insert / delete)
    Output: dictionary of dictionaries scoring matrix like this: dict[row][column]
    '''
    alpha_list = list(alphabet)
    alpha_list.append('-')  # add the dash, assumed not to be in the alphabet

    scoring_matrix_d = {}
    for row in alpha_list:          #initialize the rows in the scoring to empty
        scoring_matrix_d[row] = {}

    for key in scoring_matrix_d:    # get a row key
        col_d = {}
        for column in alpha_list:   # initialize columns with scoring values
            if key == '-' or column == '-':
                col_d[column] = dash_score
            elif key == column:
                col_d[column] = diag_score
            else:
                col_d[column] = off_diag_score  # this is probably the most common case
                                                # performance better if first?
        scoring_matrix_d[key] = col_d

    return scoring_matrix_d

def compute_alignment_matrix(s_x, s_y, scoring_mat, global_flag):
    '''
    Inputs: s_x, s_y are string / sequence inputs
    Outputs: is a list of lists [ [0, -4, -8, -12], [then row 1's column entries], [ etc.]]
    '''
    if s_x == '' or s_y == '':
        return [[0]]

    build_s_matrix, col_d = [], []
    if global_flag == True:             # set upper left corner to 0, S[0,0] = 0
        col_d.append(0)                 # this will become the upper left corner
        build_s_matrix.append(col_d)

        for column in range(1, len(s_y)+1):   #initialize top row
            value = build_s_matrix[0][column-1] + scoring_mat['-'][s_y[column-1]]
            build_s_matrix[0].append(value)

        for row in range(1, len(s_x)+1):      #initialize left column
            col_d = []
            col_d.append(build_s_matrix[row-1][0] + scoring_mat[s_x[row-1]]['-'])
            build_s_matrix.append(col_d)

        for row in range(1, len(s_x)+1):
            for column in range(1, len(s_y)+1):
                first = build_s_matrix[row-1][column-1] + scoring_mat[s_x[row-1]][s_y[column-1]]
                second = build_s_matrix[row-1][column] + scoring_mat[s_x[row-1]]['-']
                third = build_s_matrix[row][column-1] + scoring_mat['-'][s_y[column-1]]
                build_s_matrix[row].append(max(first, second, third))

        return build_s_matrix

    else:
        col_d.append(0)                 # this will become the upper left corner
        build_s_matrix.append(col_d)

        for column in range(1, len(s_y)+1):   #initialize top row
            value = build_s_matrix[0][column-1] + scoring_mat['-'][s_y[column-1]]
            prev_col_d = build_s_matrix.pop()
            prev_col_d.append(max(0, value))  # if value neg, append 0, avoids two branches if/else
            build_s_matrix.append(prev_col_d)

        for row in range(1, len(s_x)+1):      #initialize left column
            col_d = []
            value = build_s_matrix[row-1][0] + scoring_mat[s_x[row-1]]['-']
            col_d.append(max(0, value))
            build_s_matrix.append(col_d)

        for row in range(1, len(s_x)+1):
            for column in range(1, len(s_y)+1):
                first = build_s_matrix[row-1][column-1] + scoring_mat[s_x[row-1]][s_y[column-1]]
                second = build_s_matrix[row-1][column] + scoring_mat[s_x[row-1]]['-']
                third = build_s_matrix[row][column-1] + scoring_mat['-'][s_y[column-1]]
                build_s_matrix[row].append(max(first, second, third, 0))  # if above neg, append 0

        return build_s_matrix

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
