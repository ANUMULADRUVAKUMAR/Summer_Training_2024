def traversal(n):
    if(n==0):
        return
    traversal(n-1)
    print(n)
    print('progrom over')
print(traversal(5))