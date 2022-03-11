a=[22,13,44,56,65,41,2]
a.sort()
print(a)


# Using min method:
arr=[12,13,44,54,4,3,1]
arr2=[]
while(arr!=[]):
    arr2.append(min(arr))
    arr.remove(min(arr))
print(arr2)
