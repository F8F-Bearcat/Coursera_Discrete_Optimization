import string

path = 'C:/Users/andyd/Documents/GitHub/Coursera_Discrete_Optimization/knapsack/data/ks_4_0'
f = open( path, 'r' )

ll, l = [], []
i = 0
#
# file format has the number of lines and knapsack capacity in the first line
# each line following has a value and weight for each item
#
for e in f:
    if( i == 0):
        new_e = string.rstrip( e )  #take off the new line character
        line = new_e.split( " " )
        item_count = int( line[0] )
        knapsack_capacity = int( line[1] )
    new_e = string.rstrip( e )
    line = new_e.split( " " )
#
# Data structure for l is [ value, weight, line number, flag ]
# flag = 1 when the item is placed in the knapsack
#
# Data structure for ll is [ la, lb, lc, etc ], a list of lists
#
    l.append( int( line[0] ) )
    l.append( int( line[1] ) )
    l.append( i )
    l.append( 0 )   # Default is item is not selected
    ll.append( l )  # Create a list of lists
    l = []          # need to clear the list after 
    i += 1

items_l = ll[ 1: ]  # make a list that contains a list for each item

print items_l
        
# l.sort(key = lambda what: what[0][1]*100./what[0][0])

items_l.sort( key = lambda what: float( what[ 0 ]/what[ 1 ] ) )

print items_l
