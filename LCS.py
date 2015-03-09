#! /usr/bin/python

# Initialize the two list to find their common sequence
list_1 = ['a', 'b', 'c', 'a', 'd', 'a', 'c', 'b', 'c', 'a', 'd', 'c']
list_2 = ['a', 'b', 'a', 'd', 'a', 'a', 'a', 'c', 'c', 'c', 'a', 'd', 'c']

# Initialize the 2-dimensional list for common sequence marks
list_direct = []
list_count = []
list_direct = [[0 for i in xrange(len(list_2) + 1)] for i in xrange(len(list_1) + 1)]
list_count = [[0 for i in xrange(len(list_2) + 1)] for i in xrange(len(list_1) + 1)]

print("The list_direct:", list_direct)
print("The list_count:", list_count)

for i in range(1, len(list_1) + 1):
    for j in range(1, len(list_2) + 1):
        print("%d %d" % (i, j))
        if list_1[i-1] == list_2[j-1]:
            list_direct[i][j] = 3
            list_count[i][j] = list_count[i-1][j-1] + 1
        elif list_count[i][j-1] >= list_count[i-1][j]:
            list_direct[i][j] = 1
            list_count[i][j] = list_count[i][j-1]
        else:
            list_direct[i][j] = 2
            list_count[i][j] = list_count[i-1][j]

# print out the list:
for i in range(len(list_1) + 1):
    for j in range(len(list_2) + 1):
        print '%3s' % list_count[i][j],
    print('\n')
print 'change to direct'
for j in range(len(list_2)):
    print '%3s' % list_2[i-1]
for i in range(len(list_1) + 1):
    if i != 0:
        print '%3s' % list_1[i-1]
    for j in range(len(list_2) + 1):
        print '%3s' % list_direct[i][j],
    print('\n')