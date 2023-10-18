my_tuple = (1, 'strings', 4.5, True)
print(my_tuple[1])

# Printing instances of strings in my_tuple
print(my_tuple.count('strings'))

# Finding the index of the first occurrence of 4.5 in my_tuple
print(my_tuple.index(4.5))

# Printing all values in my_tuple
for x in my_tuple:
    print(x)

# Demonstrating immutable error (Uncomment the next line)
# my_tuple[0] = 5