# Array
a=[22,12,33,44,3,13]
min_num=a[0]

# For Understanding:
# min=22
# a[1]=12 so is 12 < 22 yes min=12
# a[2]=33 so is 33<12 no
# a[3]=44 so is 44<12 no
# a[4]=3 so is 3<12 yes min=3
# a[5]=13 so is 13<3 no
# Therefore,min=3

# 1.Using For loop:
for i in range(len(a)):
    if a[i]<min_num:
        min_num=a[i]
print(min_num)

# 2.Using sort:
a=[22,12,33,44,3,13]
a.sort()
print(a[0])

# 3. using min:

a=[22,12,33,44,3,13]
print(min(a))
