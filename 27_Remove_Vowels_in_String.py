# Using list and for:
sen='My name is Priya'
l=['a','e','i','o','u','A','E','I','O','U']
for i in sen:
    if i not in l:
        print(i,end='')

# Using if else
s='Hey! Good Morning'
new=''
print("\n")
for i in s:
    if i=='A' or i=='E' or i=='O' or i=='U' or i=='I' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        pass
    else:
        new+=i
print(new)
