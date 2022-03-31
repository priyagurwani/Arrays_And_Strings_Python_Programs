# Method 1: Using Two Strings and list and list Comprehension:
a='1234albgj'
b='0123456789'
c=[int(i) for i in a if i in b]
sum=0
for i in c:
    sum+=i
print(sum)

# OR
a='1234albgj'
b='0123456789'
c=''
for i in a:
    if i in b:
        c+=i
    else:
        pass
# print(c)
sum=0
for i in c:
    sum+=int(i)
print(sum)


# Method 2 = Using ord:
String = input('Enter the alphanumeric string :')
sum1 = 0
for i in String:
    if ord(i) >= 48 and ord(i) <= 57:
        sum1 = sum1 + int(i)
print('Sum is :' + str(sum1))
