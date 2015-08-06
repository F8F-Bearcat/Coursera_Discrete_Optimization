import requests
import build_scoring_matrix as BSM
import compute_alignment_matrix as CAM
import compute_global_alignment as CGA
import compute_local_alignment as CLA

def score_alignment_a(seq_x, seq_y, scoring_matrix):
    '''
    Inputs:
    Outputs:
    A little helper function
    '''
    sum = 0
    for char_index in range(len(seq_x)):
        sum += scoring_matrix[seq_x[char_index]][seq_y[char_index]]
    return sum

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
url = 'http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt'
my_headers = {'User-Agent': ua,'Accept-Language':'en-US,en;q=0.8','Referer':'https://www.google.com','Connection':'keep-alive','Accept': '*.*', 'Accept-Encoding':'gzip, deflate, sdch'}

r = requests.get( url, headers=my_headers)

word_dict = {}
for line in r.iter_lines():
    #if line: print line
    key = len(line)
    if key in word_dict:
        old = word_dict[key]
        old = old | set([line])
        word_dict[key] = old
    else:
        word_dict[key] = set([line])

word_list = []
for item in word_dict:
    word_list.append([item, len(word_dict[item])])

word_list.sort()
#print word_list

alpha = 'abcdefghijklmnopqrstuvwxyz'
diag_score = 2
off_diag_score = -1
dash_score = 0

score_matrix = BSM.build_scoring_matrix(alpha, diag_score, off_diag_score, dash_score)
#print score_matrix

score_keys_words_values = {}
for initialize in range(-10, 17):
    score_keys_words_values[initialize] = set([])

word = 'firefly'
word_set_len = word_dict[len(word)]

for check_word in word_set_len:
    result = score_alignment_a(word, check_word, score_matrix)
    old_set = score_keys_words_values[result]
    old_set |= set([check_word])
    score_keys_words_values[result] = old_set

word_set_len = word_dict[len(word)-1]

for check_word in word_set_len:
    align_matrix = CAM.compute_alignment_matrix(word, check_word, score_matrix, True)
    result_tuple = CGA.compute_global_alignment(word, check_word, score_matrix, align_matrix)
    old_set = score_keys_words_values[result_tuple[0]]
    old_set |= set([check_word])
    score_keys_words_values[result_tuple[0]] = old_set
'''
word_set_len = word_dict[len(word)-2]

for check_word in word_set_len:
    align_matrix = CAM.compute_alignment_matrix(word, check_word, score_matrix, True)
    result_tuple = CGA.compute_global_alignment(word, check_word, score_matrix, align_matrix)
    old_set = score_keys_words_values[result_tuple[0]]
    old_set |= set([check_word])
    score_keys_words_values[result_tuple[0]] = old_set
'''
word_set_len = word_dict[len(word)+1]

for check_word in word_set_len:
    align_matrix = CAM.compute_alignment_matrix(word, check_word, score_matrix, True)
    result_tuple = CGA.compute_global_alignment(word, check_word, score_matrix, align_matrix)
    old_set = score_keys_words_values[result_tuple[0]]
    old_set |= set([check_word])
    score_keys_words_values[result_tuple[0]] = old_set

print score_keys_words_values[12]
print score_keys_words_values[11]
print score_keys_words_values[10]
print score_keys_words_values[9]
print score_keys_words_values[8]
print ' '
print ' '
print ' '
'''
score_keys_words_values = {}
for initialize in range(-9, 17):
    score_keys_words_values[initialize] = set([])

word = 'firefly'
word_set_len = word_dict[len(word)]

for check_word in word_set_len:
    result = score_alignment_a(word, check_word, score_matrix)
    old_set = score_keys_words_values[result]
    old_set |= set([check_word])
    score_keys_words_values[result] = old_set

word_set_len = word_dict[len(word)-1]

for check_word in word_set_len:
    align_matrix = CAM.compute_alignment_matrix(word, check_word, score_matrix, False)
    result_tuple = CLA.compute_local_alignment(word, check_word, score_matrix, align_matrix)
    old_set = score_keys_words_values[result_tuple[0]]
    old_set |= set([check_word])
    score_keys_words_values[result_tuple[0]] = old_set

word_set_len = word_dict[len(word)+1]

for check_word in word_set_len:
    align_matrix = CAM.compute_alignment_matrix(word, check_word, score_matrix, False)
    result_tuple = CLA.compute_local_alignment(word, check_word, score_matrix, align_matrix)
    old_set = score_keys_words_values[result_tuple[0]]
    old_set |= set([check_word])
    score_keys_words_values[result_tuple[0]] = old_set

#print score_keys_words_values

word_set_len = word_dict[len(word)-2]

for check_word in word_set_len:
    align_matrix = CAM.compute_alignment_matrix(word, check_word, score_matrix, False)
    result_tuple = CLA.compute_local_alignment(word, check_word, score_matrix, align_matrix)
    old_set = score_keys_words_values[result_tuple[0]]
    old_set |= set([check_word])
    score_keys_words_values[result_tuple[0]] = old_set

print score_keys_words_values
'''