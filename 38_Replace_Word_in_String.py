st='sing'
i=input("Enter the word you want to replace:")
j=input("Enter the word you want to replace with: ")
if i in st:
    st=st.replace(i,j)
print(st)
