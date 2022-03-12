# Using for and if
a=[12,23,44,12,12,23,44]
def c_element(n):
    count=0
    for i in a:
        if i==n:
            count+=1
    return count
print("Count of 12 is",c_element(12))
print("Count of 23 is",c_element(23))
print("Count of 44 is",c_element(44))

#  Using dictionary
a=[10,20,30,40,50,40,50]
d={i:a.count(i) for i in a }
print(d)


# using list and append
a=[10,20,30,30,40,50,50]
b=[]
for i in a:
    num=a.count(i)
    # print(f"The count of {i} is {num}")
    # OR
    b.append(f"{i}:{num}")
print(b)
