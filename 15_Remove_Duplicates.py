# Using set:
a=[10,20,30,20,30,40,50,50]
a=set(a)
print(list(a))

# Using list:

a=[10,20,30,20,30,40,50,50]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)


#Using Array: It works for sorted array only
def removedup(arr,n):
    if n==0 or n==1:
        return n
    j=0
    for i in range(0,n-1):
        if arr[i]!=arr[i+1]:
            arr[j]=arr[i]
            j+=1
    arr[j]=arr[n-1]
    j+=1
    return j
arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
n=len(arr)
n=removedup(arr,n)
for i in range(n):
    print(arr[i],end=' ')
