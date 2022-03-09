# 1. Using sort
arr=[11,1,22,12,23,43,44,4]
arr.sort()
print(f"Smallest element is {arr[0]} and largest element is {arr[-1]}")

# 2. Using Loop
arr2=[11,33,66,99,23,4,6]
min_a=arr2[0]
max_a=arr2[0]
for i in arr2:
    if i<min_a:
        min_a=i
    elif i>max_a:
        max_a=i
    else:
        pass
print(f"The smallest element is {min_a} and largest element is {max_a}")

# 3. Using max and min:
a=[2,22,12,44,65,76,88]
print(f"The smallest element is {min(a)} and largest element is {max(a)}")
