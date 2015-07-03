some_list = [1, 2, 3, 4, 5]
new_list = []
new_list1 = []

for element in some_list:
    new_list.append(some_list[-element])

print new_list


for element in some_list:
    new_list1 = [element] + new_list1

print '\n'
print new_list1