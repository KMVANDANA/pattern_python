n=3
x=ord("A")
for i in range(n):
    for j in range(i):
        print(chr(x),end='')
        x=x+1
    for k in range(i,n):
        print(" ",end='')
    for l in range(i,n):
        print(" ",end='')
    for m in range(i):
       print(chr(x),end='')
       x=x+1
    print('')
for o in range(n):
    for p in range(o,n):
       print(chr(x),end='')
       x=x+1
    for q in range(o):
        print(" ",end='')
    for r in range(o):
        print(" ",end='')
    for s in range(o,n):
        print(chr(x),end='')
        x=x+1
    print('')