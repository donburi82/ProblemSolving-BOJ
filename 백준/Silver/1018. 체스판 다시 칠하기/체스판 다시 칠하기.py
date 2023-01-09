import sys

m, n = map(int, sys.stdin.readline().split())
a = []
for _ in range(m):
    a.append(list(sys.stdin.readline().strip()))
counts = []
for row in range(m-8+1):
    for col in range(n-8+1):
        temp = [a[i][col:col+8] for i in range(row, row+8)]
        # check for left top corner as W
        count = 0
        for i in range(8): # loop through rows
            for j in range(8): # loop through columns
                if i%2==0: # start as W and flip
                    if j%2==0 and temp[i][j]!='W': # should be W
                        count += 1
                    elif j%2==1 and temp[i][j]!='B': # should be B
                        count += 1
                else: # start as B and flip
                    if j%2==0 and temp[i][j]!='B': # should be B
                        count += 1
                    elif j%2==1 and temp[i][j]!='W': # should be W
                        count += 1
        counts.append(count)
        # check for left top corner as B
        count = 0
        for i in range(8): # loop through rows
            for j in range(8): # loop through columns
                if i%2==1: # start as B and flip
                    if j%2==0 and temp[i][j]!='W': # should be W
                        count += 1
                    elif j%2==1 and temp[i][j]!='B': # should be B
                        count += 1
                else: # start as W and flip
                    if j%2==0 and temp[i][j]!='B': # should be B
                        count += 1
                    elif j%2==1 and temp[i][j]!='W': # should be W
                        count += 1
        counts.append(count)
print(min(counts))