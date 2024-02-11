n=7
for i in range(n):
    for j in range(i):
        print(" ",end='')
    for k in range(i,n):
        print("*",end='')
    for l in range(i,n-1):
        print("*",end='')
    print('')
for m in range(n-1):
    for o in range(m,n-2):
        print(" ",end='')
    for p in range(m+2):
        print("*",end='')
    for q in range(m+1):
        print("*",end='')
    print('')

    