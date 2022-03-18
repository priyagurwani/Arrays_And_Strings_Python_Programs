# Using List Comprehension: 
a=[10,20,33,44,2,3,43,55,76]
even_n=[i for i in a if i%2==0]
odd_n=[i for i in a if i not in even_n]
print(f"Even numbers are {even_n} and total they are {len(even_n)}")
print(f"Odd numbers are {odd_n} and total they are {len(odd_n)}")
