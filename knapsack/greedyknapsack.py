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

f.close()
items_l = ll[ 1: ]  # make a list that contains a list for each item

print items_l

items_l.sort( key = lambda what: float( what[ 0 ]/what[ 1 ] ) )

print items_l

weight, value  = 0, 0
for ele in items_l:
    value += ele[ 0 ]
    weight += ele[ 1 ]
    ele.pop()
    ele.append( 1 )
    if( weight > knapsack_capacity ):  # back out item if does not fit
        value -= ele[ 0 ]              # this tries all elements
        weight -= ele[ 1 ]
        ele.pop()
        ele.append( 0 )

print '\nweight is ', weight
print 'value is ', value
print 'items_l is ', items_l
    
items_l.sort( key = lambda what: what[ 2 ] )
print 'items_l in original order is ', items_l

print value, 0

for e in items_l:
    print e[3],  # cute python trick to print on the same line w space
