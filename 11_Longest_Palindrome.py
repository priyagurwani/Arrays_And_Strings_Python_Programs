# 1. Using if-else
a=[101,2321,2002,12]
b=[]
for i in a:
    # print(i)
    if str(i)==str(i)[::-1]:
        b.append(int(i))
    else:
        pass
print(b)
print(f"{max(b)} is the longest palindrome ")

#2. Using List Comprehension
l=[202,1019,5545455,199,2002]
res=[int(i) for i in l if(str(i)==str(i)[::-1])]
print(f"{max(res)} is the longest palindrome")
