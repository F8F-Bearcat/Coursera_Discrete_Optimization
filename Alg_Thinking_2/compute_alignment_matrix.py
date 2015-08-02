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
    Outputs:
    '''
    if s_x == '' or s_y == '':
        return [[0]]

    build_s_matrix, col_d = {}, {}
    if global_flag == True:         # set upper left corner to 0, S[0,0] = 0
        col_d[0] = 0                # this will become the upper left corner
        build_s_matrix[0] = col_d

        for column in range(1, len(s_y)+1):   #initialize top row
            col_d[column] = build_s_matrix[0][column-1] + scoring_mat['-'][s_y[column-1]]
            build_s_matrix[0] = col_d

        for row in range(1, len(s_x)+1):      #initialize left column
            col_d = {}
            col_d[0] = build_s_matrix[row-1][0] + scoring_mat[s_x[row-1]]['-']
            build_s_matrix[row] = col_d

        for row in range(1, len(s_x)+1):
            col_d = build_s_matrix[row]   # initial column exists, build on that rather than replace
            for column in range(1, len(s_y)+1):
                first = build_s_matrix[row-1][column-1] + scoring_mat[s_x[row-1]][s_y[column-1]]
                second = build_s_matrix[row-1][column] + scoring_mat[s_x[row-1]]['-']
                third = build_s_matrix[row][column-1] + scoring_mat['-'][s_y[column-1]]
                col_d[column] = max(first, second, third)
            build_s_matrix[row] = col_d

        out = []                                # kludgy assignment did not specifiy type for 
        for ele in build_s_matrix.items():      # matrix. I did dict of dict. they wanted
            row, columns = [], []               # lists apparently. This converts to lists...
            row.append(ele[0])
            #print 'first row is ', row
            #print 'ele[1].items()', ele[1].items()
            for item in ele[1].items():
                columns.append(item[1])
            #print 'columns are ', columns
            out.append(columns)
            #print 'second row is ', row
            #out.append(row)
            #print 'out is ', out
        return out

    else:
        col_d[0] = 0                # this will become the upper left corner
        build_s_matrix[0] = col_d

        for column in range(1, len(s_y)+1):   #initialize top row
            value = build_s_matrix[0][column-1] + scoring_mat['-'][s_y[column-1]]
            if value < 0:
                col_d[column] = 0
            else:
                col_d[column] = value
            build_s_matrix[0] = col_d

        for row in range(1, len(s_x)+1):      #initialize left column
            col_d = {}
            value = build_s_matrix[row-1][0] + scoring_mat[s_x[row-1]]['-']
            if value < 0:
                col_d[0] = 0
            else:
                col_d[0] = value
            build_s_matrix[row] = col_d

        for row in range(1, len(s_x)+1):
            col_d = build_s_matrix[row]   # initial column exists, build on that rather than replace
            for column in range(1, len(s_y)+1):
                first = build_s_matrix[row-1][column-1] + scoring_mat[s_x[row-1]][s_y[column-1]]
                second = build_s_matrix[row-1][column] + scoring_mat[s_x[row-1]]['-']
                third = build_s_matrix[row][column-1] + scoring_mat['-'][s_y[column-1]]
                value = max(first, second, third)
                if value < 0:
                    col_d[column] = 0
                else:
                    col_d[column] = max(first, second, third)
            build_s_matrix[row] = col_d

        out = []
        for ele in build_s_matrix.items():
            row, columns = [], []
            row.append(ele[0])
            #print 'ele[1].items()', ele[1].items()
            for item in ele[1].items():
                columns.append(item[1])
            out.append(columns)
            #print 'out in function is ', out
        return out


# Test function
ALPHABET = {'T', 'A', 'G', 'C'}

scoring_matrix = build_scoring_matrix(ALPHABET, 5, 2, -4)
print 'Scoring matrix M is '
print scoring_matrix

seq_x = 'AC'
seq_y = 'TAG'

s_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
print 'S matrix is '
print s_matrix