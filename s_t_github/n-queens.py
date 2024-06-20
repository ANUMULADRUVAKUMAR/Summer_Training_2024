l1=[]
'''def queen(board,a,b,n):
    c=0
    board[a][b]=1
    for i in range(len(board)):
        for j in range(len(board)):
            if safe(board,i,j,n):
                l1.append([i,j])
                c += 1
                board[i][j]=1
    print(board)
    return c'''
def queen(board,a,b,n):
    if b==n-1:
        return
    c=0
    board[a][b]=1
    for i in range(len(board)):
        queen(board,i,j+1,n)
        if safe(board,i,j,n):
            l1.append([i,j])
            c += 1
            board[i][j]=1
    print(board)


def safe(board,r,c,n):
    for i in range(n):
        if board[i][c]==1:
            return False
    for i in range(n):
        if board[r][i]==1:
            return False
    i=r
    j=c
    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i = r
    j = c
    while (i <n and j <n):
        if board[i][j] == 1:
            return False
        i += 1
        j += 1
    i=r
    j=c
    while(i>=0 and j<n):
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    i = r
    j = c
    while (i <n and j>=0):
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

n = 5
for i in range(n):
    for j in range(n):
        if[i,j] not in l1:
            board = [[0 for i in range(n)] for j in range(n)]
            c=queen(board,i,j,n)
            print(c)