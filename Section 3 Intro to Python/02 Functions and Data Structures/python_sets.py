set_a = {1, 2, 3, 4, 5}

# Adding 6 to set_a
set_a.add(6)
print(set_a)

# Removing the number 2 from set_a
set_a.remove(2)     # set_a.discard(2) will do the same thing
print(set_a)

# Union Join of set_a and set_b
set_b = {5,6,7,8,9}

print(set_a.union(set_b))      # Union will not merge repeating values as a set cannot repeat values
# print(set_a | set_b) has the same functionality

# Intersection
print(set_a - set_b) # or print(set_a.intersection(set_b))