a, b, c, d = [int(input()) for i in range(4)]
for g in range(c, d+1):
    print('\t' + str(g), end='')
print(end='\n')
for i in range(a, b+1):
    print(str(i)+'\t', end='')
    for j in range(c, d+1):
        print(str(i*j), end='\t')
    print(end='\n')