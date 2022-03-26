# Method 1: Using 2 strings
s="I am learning Python:)"
new=""
for i in s:
    if i!=" ":
        new+=i
    else:
        pass
print(new)

# Method 2:       
st="I am learning Python!!"
space=" "
for i in st:
    if i!=space:
        print(i,end="")
