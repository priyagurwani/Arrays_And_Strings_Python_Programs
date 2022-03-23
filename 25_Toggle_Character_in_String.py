# Using if else
ch=input("Enter a string: ")
# OR
# ch="HeyPriyaG"
t=''
for i in ch:
    if i.islower():
        t+=i.upper()
    else:
        t+=i.lower()
print(t)

# Using swapcase function
name='PriyaGurwani'
print(f"The Toggle case of {name} is {name.swapcase()}")
