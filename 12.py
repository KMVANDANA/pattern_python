n=7
for i in range(n):
    for j in range(i):
        print("*",end='')
    for k in range(i,n):
        print(" ",end='')
    for l in range(i,n):
        print(" ",end='')
    for m in range(i):
        print("*",end='')
    print('')
for o in range(n):
    for p in range(o,n):
        print("*",end='')
    for q in range(o):
        print(" ",end='')
    for r in range(o):
        print(" ",end='')
    for s in range(o,n):
        print("*",end='')
    print('')