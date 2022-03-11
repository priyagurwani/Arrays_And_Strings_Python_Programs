a=[12,22,13,44,66,5]
leng=len(a)//2
asec=[]
dsec=[]
for i in a:
    if(len(asec)!=leng):
        asec.append(i)
    else:
        dsec.append(i)
# print(asec)
# print(dsec)

asec.sort()
# print(asec)

desc_rev=dsec[::-1]
desc_rev.sort()
# print(desc_rev)

print(asec+desc_rev)
