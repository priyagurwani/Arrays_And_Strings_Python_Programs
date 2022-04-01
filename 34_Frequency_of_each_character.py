# Method 1:
st='hey you'
for i in st:
    frequency=st.count(i)
    print(str(i)+":"+str(frequency), end=',')

# Method 2: Using Dictionary:
print("\n")
n='Good morning'
d={}
for value in n:
    if value in d:
        d[value]+=1
    else:
        d[value]=1
print(d)
    
