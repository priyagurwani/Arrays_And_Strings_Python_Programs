# 1.Using reverse method
a=[12,33,1,34,6]
a.reverse()
print(a)

#2. Using reversed keyword
arr=[11,34,54,67,3]
print(list(reversed(arr)))

# 3.Using slicing
arr=[12,11,45,88,99]
print(arr[::-1])

# 4.Using for loop
arr=[12,22,1,3,55,66]
a2=[]
for i in arr:
    while(arr!=[]):
       i=arr[-1]
       a2.append(i)
       arr.remove(arr[-1])
print(a2)
