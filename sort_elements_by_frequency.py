a = [10, 20, 30, 40, 40, 50, 50, 50]

# sorting on bais of frequency of elements
result = sorted(a, key = a.count, reverse = True)

# printing final result
print(str(result))
# print(sorted(ini_list,key=ini_list.count))
