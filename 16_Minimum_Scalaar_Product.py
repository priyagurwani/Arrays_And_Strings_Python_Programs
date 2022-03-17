a={10,30,50,20,40}
b={20,40,50,30,10}
a=list(a)
a.sort()
b=list(b)
b.sort(reverse=True)
new_a=a
new_b=b
product_a_b=0

for i in range(len(new_a)):
    product_a_b+=new_a[i]*new_b[i]
print(product_a_b)
