# Using List
num='(1+2)*{9+0}/2'
brack_list=['{','}','[',']','(',')']
new=''
for i in num:
    if i in brack_list:
        pass
    else:
        new+=i
print(new)

# Using if else
num='(1+2)//{2}*[9]'
without_brack=''
for i in num:
    if i=='{' or i=='}' or i=='[' or i==']' or i=='(' or i==')':
        pass
    else:
        without_brack+=i
print(without_brack)
