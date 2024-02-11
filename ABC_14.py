n=7
k=ord("A")
for i in range(n):
    for j in range(i):
        print(chr(k),end='')
        k=k+1
    print('')