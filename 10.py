n=7
for i in range(n):
    for j in range(i,n):
        print(" ",end='')
    for k in range(i):
        print("*",end='')
    for l in range(i-1):
        print("*",end='')
    print('')
for m in range(n):
    for p in range(m):
         print(" ",end='')
    for o in range(m,n):
        print("*",end='')
    for q in range(m,n-1):
        print('*',end='')
    print('')