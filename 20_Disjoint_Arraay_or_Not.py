# Disjoint = similar
# Not Disjoint = not similar
# Using function

a1={12,11,44,65,1}
a2={12,33,22,65,6}
def check(x,y):
   for i in a1:
       if i in a2:
           return True
       else:
           return False
print(check(a1,a2))

# OR

def Dis_or_Not(a1,a2):
    for i in range(0,len(a1)):
        for j in range(0,len(a2)):
            if(a1[i]==a2[j]):
                return True
    return False
a1=[12,11,44,65,1]
a2=[12,33,22,5,6]
if(Dis_or_Not(a1,a2)):
    print("Disjoint")
else:
    print("Not Disjoint")
