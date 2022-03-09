# 1.Using max method
a=[12,11,33,55,77]
print(max(a))

#2. Using loop
arr=[11,22,33,44,55,66,77,88]
max_n=a[0]
for i in arr:
    if i>max_n:
        max_n=i
print(max_n)

# 3. Using Sort
arr2=[22,11,3,44,66]
arr2.sort()
print(arr2[-1])
