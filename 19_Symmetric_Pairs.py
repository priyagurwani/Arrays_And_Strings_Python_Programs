# Symmetric Pairs:
a=[(1,2),(3,4),(9,8),(2,1),(4,3)]
b=set()
for (x,y) in a:
    b.add((x,y))
    if (y,x) in b:
        print((x,y))
