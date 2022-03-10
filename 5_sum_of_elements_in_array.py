# Using For loop
arr=[12,22,1,3,4]
sum=0
for i in arr:
    sum+=i
print("The sum of all the elements is",sum)

# Using function
arr2=[11,22,1,3]
def sum_n(args):
    sum=0
    for i in args:
        sum+=i
    return sum

print("The addition of the elements is",sum_n(arr2))

