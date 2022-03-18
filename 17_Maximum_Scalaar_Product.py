a=[10,30,60,40,20]
b=[20,30,10,50,40]
a.sort()
new_a=a
b.sort()
new_b=b
product_a_b=0
for i in range(len(new_a)):
    product_a_b+=new_a[i]*new_b[i]
print(product_a_b)
