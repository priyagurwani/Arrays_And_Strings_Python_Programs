# Count vowels in string 
# 1. Using list and for:
sen="My name is Priya"
l=['a','e','i','o','u','A','E','I','O','U']
count=0
for j in sen:
    for i in l:
        if i==j:
            count+=1
print("The total count of vowels is",count)

# 2.Using if else
s='Hey! Good Morning'
count_vowels=0
for i in s:
    if i=='A' or i=='E' or i=='O' or i=='U' or i=='I' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count_vowels+=1
    else:
        pass
print("The count of vowels in ", s,"is",count_vowels)
