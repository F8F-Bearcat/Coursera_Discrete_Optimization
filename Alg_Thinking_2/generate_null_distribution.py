'''
Module comments
'''
import compute_alignment_matrix as CAM
import compute_local_alignment as CLA
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    '''
    Inputs:
    Outputs:
    '''
    scoring_distribution = {}
    split_y = list(seq_y)

    for trial in range(num_trials):
        random.shuffle(split_y)
        rand_y = ''.join(split_y)
        alignment_matrix = CAM.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        result = CLA.compute_local_alignment(seq_x, rand_y, scoring_matrix, alignment_matrix)
        if result[0] in scoring_distribution:
            count = scoring_distribution[result[0]]
            count += 1
            scoring_distribution[result[0]] = count
        else:
            scoring_distribution[result[0]] = 1

    return scoring_distribution

human_eyeless = 'MQNSHSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQMGADGMYDKLRMLNGQTGSWGTRPGWYPGTSVPGQPTQDGCQQQEGGGENTNSISSNGEDSDEAQMRLQLKRKLQRNRTSFTQEQIEALEKEFERTHYPDVFARERLAAKIDLPEARIQVWFSNRRAKWRREEKLRNQRRQASNTPSHIPISSSFSTSVYQPIPQPTTPVSSFTSGSMLGRTDTALTNTYSALPPMPSFTMANNLPMQPPVPSQTSSYSCMLPTSPSVNGRSYDTYTPPHMQTHMNSQPMGTSGTTSTGLISPGVSVPVQVPGSEPDMSQYWPRLQ'
fruitfly_eyeless = 'MRNLPCLGTAGGSGLGGIAGKPSPTMEAVEASTASHPHSTSSYFATTYYHLTDDECHSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQSTGSGSSSTSAGNSISAKVSVSIGGNVSNVASGSRGTLSSSTDLMQTATPLNSSESGGASNSGEGSEQEAIYEKLRLLNTQHAAGPGPLEPARAAPLVGQSPNHLGTRSSHPQLVHGNHQALQQHQQQSWPPRHYSGSWYPTSLSEIPISSAPNIASVTAYASGPSLAHSLSPPNDIESLASIGHQRNCPVATEDIHLKKELDGHQSDETGSGEGENSNGGASNIGNTEDDQARLILKRKLQRNRTSFTNDQIDSLEKEFERTHYPDVFARERLAGKIGLPEARIQVWFSNRRAKWRREEKLRNQRRTPNSTGASATSSSTSATASLTDSPNSLSACSSLLSGSAGGPSVSTINGLSSPSTLSTNVNAPTLGAGIDSSESPTPIPHIRPSCTSDNDNGRQSEDCRRVCSPCPLGVGGHQNTHHIQSNGHAQGHALVPAISPRLNFNSGSFGAMYSNMHHTALSMSDSYGAVTPIPSFNHSAVGPLAPPSPIPQQGDLTPSSLYPCHMTLRPPPMAPAHHHIVPGDGGRPAGVGLGSGQSANLGASCSGSGYEVLSAYALPPPPMASSSAADSSFSAASSASANVTPHHTIAQESCPSPCSSASHFGVAHSSGFSSDPISPAVSSYAHMSYNYASSANTMTPSSASGTSAHVAPGKQQFFASCFYSPWV'
scoring_matrix = {'-': {'-': -100, 'A': -5, 'C': -5, 'B': -5, 'E': -5, 'D': -5, 'G': -5, 'F': -5, 'I': -5, 'H': -5, 'K': -5, 'M': -5, 'L': -5, 'N': -5, 'Q': -5, 'P': -5, 'S': -5, 'R': -5, 'T': -5, 'W': -5, 'V': -5, 'Y': -5, 'X': -5, 'Z': -5}, 'A': {'-': -5, 'A': 5, 'C': -5, 'B': -2, 'E': -1, 'D': -2, 'G': -1, 'F': -7, 'I': -3, 'H': -5, 'K': -5, 'M': -4, 'L': -5, 'N': -2, 'Q': -3, 'P': 0, 'S': 0, 'R': -5, 'T': 0, 'W': -11, 'V': -1, 'Y': -6, 'X': -2, 'Z': -2}, 'C': {'-': -5, 'A': -5, 'C': 9, 'B': -9, 'E': -11, 'D': -11, 'G': -7, 'F': -10, 'I': -5, 'H': -6, 'K': -11, 'M': -11, 'L': -12, 'N': -8, 'Q': -11, 'P': -6, 'S': -2, 'R': -6, 'T': -6, 'W': -13, 'V': -5, 'Y': -3, 'X': -7, 'Z': -11}, 'B': {'-': -5, 'A': -2, 'C': -9, 'B': 5, 'E': 2, 'D': 6, 'G': -2, 'F': -9, 'I': -5, 'H': 0, 'K': -1, 'M': -7, 'L': -7, 'N': 5, 'Q': -2, 'P': -5, 'S': -1, 'R': -5, 'T': -2, 'W': -8, 'V': -6, 'Y': -5, 'X': -3, 'Z': 1}, 'E': {'-': -5, 'A': -1, 'C': -11, 'B': 2, 'E': 7, 'D': 3, 'G': -3, 'F': -11, 'I': -4, 'H': -3, 'K': -3, 'M': -5, 'L': -7, 'N': -1, 'Q': 2, 'P': -4, 'S': -3, 'R': -7, 'T': -4, 'W': -13, 'V': -5, 'Y': -7, 'X': -3, 'Z': 6}, 'D': {'-': -5, 'A': -2, 'C': -11, 'B': 6, 'E': 3, 'D': 7, 'G': -2, 'F': -12, 'I': -6, 'H': -2, 'K': -3, 'M': -8, 'L': -10, 'N': 2, 'Q': -1, 'P': -6, 'S': -2, 'R': -7, 'T': -3, 'W': -12, 'V': -6, 'Y': -9, 'X': -4, 'Z': 2}, 'G': {'-': -5, 'A': -1, 'C': -7, 'B': -2, 'E': -3, 'D': -2, 'G': 6, 'F': -8, 'I': -8, 'H': -7, 'K': -6, 'M': -7, 'L': -9, 'N': -2, 'Q': -5, 'P': -4, 'S': -1, 'R': -7, 'T': -4, 'W': -12, 'V': -4, 'Y': -11, 'X': -4, 'Z': -4}, 'F': {'-': -5, 'A': -7, 'C': -10, 'B': -9, 'E': -11, 'D': -12, 'G': -8, 'F': 9, 'I': -1, 'H': -5, 'K': -11, 'M': -3, 'L': -1, 'N': -7, 'Q': -10, 'P': -8, 'S': -5, 'R': -8, 'T': -7, 'W': -3, 'V': -6, 'Y': 3, 'X': -6, 'Z': -11}, 'I': {'-': -5, 'A': -3, 'C': -5, 'B': -5, 'E': -4, 'D': -6, 'G': -8, 'F': -1, 'I': 8, 'H': -7, 'K': -5, 'M': 0, 'L': 0, 'N': -4, 'Q': -6, 'P': -7, 'S': -5, 'R': -4, 'T': -1, 'W': -11, 'V': 3, 'Y': -5, 'X': -3, 'Z': -5}, 'H': {'-': -5, 'A': -5, 'C': -6, 'B': 0, 'E': -3, 'D': -2, 'G': -7, 'F': -5, 'I': -7, 'H': 9, 'K': -4, 'M': -8, 'L': -5, 'N': 1, 'Q': 2, 'P': -3, 'S': -4, 'R': 0, 'T': -5, 'W': -6, 'V': -5, 'Y': -2, 'X': -4, 'Z': 0}, 'K': {'-': -5, 'A': -5, 'C': -11, 'B': -1, 'E': -3, 'D': -3, 'G': -6, 'F': -11, 'I': -5, 'H': -4, 'K': 6, 'M': -1, 'L': -6, 'N': 0, 'Q': -2, 'P': -5, 'S': -3, 'R': 1, 'T': -2, 'W': -9, 'V': -7, 'Y': -8, 'X': -4, 'Z': -2}, 'M': {'-': -5, 'A': -4, 'C': -11, 'B': -7, 'E': -5, 'D': -8, 'G': -7, 'F': -3, 'I': 0, 'H': -8, 'K': -1, 'M': 10, 'L': 2, 'N': -6, 'Q': -3, 'P': -6, 'S': -4, 'R': -3, 'T': -3, 'W': -10, 'V': 0, 'Y': -8, 'X': -4, 'Z': -4}, 'L': {'-': -5, 'A': -5, 'C': -12, 'B': -7, 'E': -7, 'D': -10, 'G': -9, 'F': -1, 'I': 0, 'H': -5, 'K': -6, 'M': 2, 'L': 6, 'N': -6, 'Q': -4, 'P': -6, 'S': -7, 'R': -7, 'T': -5, 'W': -5, 'V': -1, 'Y': -5, 'X': -5, 'Z': -5}, 'N': {'-': -5, 'A': -2, 'C': -8, 'B': 5, 'E': -1, 'D': 2, 'G': -2, 'F': -7, 'I': -4, 'H': 1, 'K': 0, 'M': -6, 'L': -6, 'N': 7, 'Q': -2, 'P': -4, 'S': 1, 'R': -4, 'T': -1, 'W': -7, 'V': -6, 'Y': -3, 'X': -2, 'Z': -1}, 'Q': {'-': -5, 'A': -3, 'C': -11, 'B': -2, 'E': 2, 'D': -1, 'G': -5, 'F': -10, 'I': -6, 'H': 2, 'K': -2, 'M': -3, 'L': -4, 'N': -2, 'Q': 8, 'P': -2, 'S': -4, 'R': 0, 'T': -4, 'W': -10, 'V': -5, 'Y': -9, 'X': -3, 'Z': 6}, 'P': {'-': -5, 'A': 0, 'C': -6, 'B': -5, 'E': -4, 'D': -6, 'G': -4, 'F': -8, 'I': -7, 'H': -3, 'K': -5, 'M': -6, 'L': -6, 'N': -4, 'Q': -2, 'P': 8, 'S': -1, 'R': -3, 'T': -3, 'W': -11, 'V': -4, 'Y': -11, 'X': -4, 'Z': -3}, 'S': {'-': -5, 'A': 0, 'C': -2, 'B': -1, 'E': -3, 'D': -2, 'G': -1, 'F': -5, 'I': -5, 'H': -4, 'K': -3, 'M': -4, 'L': -7, 'N': 1, 'Q': -4, 'P': -1, 'S': 6, 'R': -2, 'T': 1, 'W': -4, 'V': -4, 'Y': -5, 'X': -2, 'Z': -3}, 'R': {'-': -5, 'A': -5, 'C': -6, 'B': -5, 'E': -7, 'D': -7, 'G': -7, 'F': -8, 'I': -4, 'H': 0, 'K': 1, 'M': -3, 'L': -7, 'N': -4, 'Q': 0, 'P': -3, 'S': -2, 'R': 8, 'T': -5, 'W': -1, 'V': -6, 'Y': -8, 'X': -4, 'Z': -2}, 'T': {'-': -5, 'A': 0, 'C': -6, 'B': -2, 'E': -4, 'D': -3, 'G': -4, 'F': -7, 'I': -1, 'H': -5, 'K': -2, 'M': -3, 'L': -5, 'N': -1, 'Q': -4, 'P': -3, 'S': 1, 'R': -5, 'T': 6, 'W': -10, 'V': -2, 'Y': -5, 'X': -2, 'Z': -4}, 'W': {'-': -5, 'A': -11, 'C': -13, 'B': -8, 'E': -13, 'D': -12, 'G': -12, 'F': -3, 'I': -11, 'H': -6, 'K': -9, 'M': -10, 'L': -5, 'N': -7, 'Q': -10, 'P': -11, 'S': -4, 'R': -1, 'T': -10, 'W': 13, 'V': -12, 'Y': -4, 'X': -9, 'Z': -11}, 'V': {'-': -5, 'A': -1, 'C': -5, 'B': -6, 'E': -5, 'D': -6, 'G': -4, 'F': -6, 'I': 3, 'H': -5, 'K': -7, 'M': 0, 'L': -1, 'N': -6, 'Q': -5, 'P': -4, 'S': -4, 'R': -6, 'T': -2, 'W': -12, 'V': 7, 'Y': -6, 'X': -3, 'Z': -5}, 'Y': {'-': -5, 'A': -6, 'C': -3, 'B': -5, 'E': -7, 'D': -9, 'G': -11, 'F': 3, 'I': -5, 'H': -2, 'K': -8, 'M': -8, 'L': -5, 'N': -3, 'Q': -9, 'P': -11, 'S': -5, 'R': -8, 'T': -5, 'W': -4, 'V': -6, 'Y': 9, 'X': -6, 'Z': -8}, 'X': {'-': -5, 'A': -2, 'C': -7, 'B': -3, 'E': -3, 'D': -4, 'G': -4, 'F': -6, 'I': -3, 'H': -4, 'K': -4, 'M': -4, 'L': -5, 'N': -2, 'Q': -3, 'P': -4, 'S': -2, 'R': -4, 'T': -2, 'W': -9, 'V': -3, 'Y': -6, 'X': -4, 'Z': -3}, 'Z': {'-': -5, 'A': -2, 'C': -11, 'B': 1, 'E': 6, 'D': 2, 'G': -4, 'F': -11, 'I': -5, 'H': 0, 'K': -2, 'M': -4, 'L': -5, 'N': -1, 'Q': 6, 'P': -3, 'S': -3, 'R': -2, 'T': -4, 'W': -11, 'V': -5, 'Y': -8, 'X': -3, 'Z': 6}}

distribution_d = generate_null_distribution(human_eyeless, fruitfly_eyeless, scoring_matrix, 1000)
print distribution_d

sum = 0
for item in distribution_d:
    sum += distribution_d[item]
out_list = []
for item in distribution_d:
    out_list.append([item, float(distribution_d[item])/sum])

out_list.sort()
#print out_list

xval, yval = zip(*out_list)
plt.bar(xval, yval, .5, color='blue')
#n = range(len(xval))
#for i, txt in enumerate(n):
#    plt.annotate(txt, (xval[i]+.02, yval[i]+.02))
#plt.xlim(0, 1000)
#plt.ylim(50, 450)
plt.xlabel('Alignment Score')
plt.ylabel('Normalized Probability Distribution')
plt.title('HW4 Applications: Null Distribution Human vs Fly, 1000 Trials')
plt.show()

'''
all_clusters.sort(key=lambda cluster: cluster.total_population())
temp_result = all_clusters[-5:]
plot_cluster_centers = []
for item in temp_result:
    point_x = item.horiz_center()
    point_y = item.vert_center()
    plot_cluster_centers.append((point_x, point_y))

plt.figure()  #makes another window
xval, yval = zip(*plot_cluster_centers)
plt.scatter(xval, yval, s=60, c='g', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i]+.05, yval[i]+.05))
plt.xlim(0, 1000)
plt.ylim(50, 450)
plt.title('Coursera test case initial 5 biggest clusters')
plt.draw()

all_clusters = result
all_clusters.sort(key=lambda cluster: len(cluster.fips_codes()), reverse=True)
temp_result = all_clusters[:]
plot_cluster_centers = []
for item in temp_result:
    point_x = item.horiz_center()
    point_y = item.vert_center()
    plot_cluster_centers.append((point_x, point_y))

plt.figure()  #makes another window
xval, yval = zip(*plot_cluster_centers)
plt.scatter(xval, yval, s=60, c='r', alpha=0.5)
n = range(len(xval))
for i, txt in enumerate(n):
    plt.annotate(txt, (xval[i]+.05, yval[i]+.05))
plt.xlim(0, 1000)
plt.ylim(50, 450)
plt.title('Coursera test case RESULT clusters')
plt.show()
'''