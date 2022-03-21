# To Check b is a subset of a or not
a=[12,22,33,14,55,44,30]
b=[12,33,14,10]    #Not a subset as a doesnot contain 10
# b=[12,33,14]     # Is subset as all elements in b are in a  

for i in a:
    if i in b:
        b.remove(i)
def check(a,b):
    if b==[]:
        return True
    else:
        return False
print(check(a,b))

