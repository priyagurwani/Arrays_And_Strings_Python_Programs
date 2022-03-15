# 1. Using if-else:
a=[10,20,30,40,50,20,30]
b=[]
common=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        common.append(i)
non_repeated=[i for i in b if i not in common]
print("The non repeated elements are ",non_repeated)

# Using dictionary
a=[10,20,30,40,50,40,50]
d={i:a.count(i) for i in a }
# print(d)
for key,values in d.items():
    if values!=1:
        pass
        # print(key)
    else:
        print(key,end=" ")
print("\n")

# using list
a=[10,20,30,30,40,50,50]
b=[]
for i in a:
    num=a.count(i)
    if num==1:
        b.append(i)
print(b)
