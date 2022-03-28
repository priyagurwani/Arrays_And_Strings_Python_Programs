# ASCII VALUES:
# A- 65 , B - 66 , ......., Z-90
# a-97, b-98 , .........,z-122
s='#4He@[y9Hey0Priya'
for i in s:
    if (ord(i)>=33 and ord(i)<=64) or (ord(i)>=91 and ord(i)<=96):
        s=s.replace(i,'')
    else:
        pass
print(s)
