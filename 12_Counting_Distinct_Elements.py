from collections import Counter

# Using Counter
def unique(a):
    print(*Counter(a))
a=[10,20,30,40,50,20,30,40]
unique(a)


# Using set
a=[10,20,30,40,50,20,30,40]
a=set(a)
print(list(a))


#Using if-else
a=[10,20,30,40,50,20,30,40]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        pass
print(b)
    
