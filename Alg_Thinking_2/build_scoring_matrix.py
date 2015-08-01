'''
Projects for module 4
build_scoring_matrix first
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
                col_d[column] = off_diag_score

        scoring_matrix_d[key] = col_d

    return scoring_matrix_d


# Test function
ALPHABET = {'T', 'A', 'G'}

scoring_matrix = build_scoring_matrix(ALPHABET, 5, 2, -2)

print scoring_matrix
