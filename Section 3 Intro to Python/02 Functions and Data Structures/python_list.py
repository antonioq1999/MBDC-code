list1 = [1, 2, 3, 4, 5]

# How to print an entire list
print(*list1)

# Alternate version
print(list1, sep=" ")

# Insertion 
list1.insert(len(list1), 6)

print('\nAdded 6 to list with insert() function.')
print(list1, sep=" ")

# Insertion w/o specifying index
list1.append(7)

print('\nAdded 7 to the list using the append() function.')
print(list1, sep=" ")

# Extend
list1.extend([8, 9, 10, 11])

print('\nAdded [8, 9, 10, 11] to the list using the extend() function.')
print(list1, sep=" ")

# Popping the value at index 4
list1.pop(4)

print('\nRemoved value at index 4 using pop() function')
print(list1, sep=" ")

# Deleting the value at index 2
del list1[2]

print('\nRemoved the value at index 2 using del keyword.')
print(list1, sep=" ")

# Iterating through a list
for x in list1:
    print('\nvalue: ', x)


# Different variables can be stored in a list
list2 = ['A', 'B', 'C']

list3 = ['Hello', 1, True, 40.22]

list4 = [1, [2,3,4], 5, 6]

