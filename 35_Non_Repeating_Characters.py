greet='Good Morning'
# greet='prepinsta'
new=''
for i in greet:
    count_each=greet.count(i)
    if count_each==1:
        new+=i
    else:
        pass
print(new)

# 
st='Welcome World'
for i in st:
    count=0
    for j in st:
        # print(j,end=',')
        if i==j:
            count+=1
    if count==1:
        print(i,end='')

