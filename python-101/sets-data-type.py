# Sets - immutable list

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union => 1, 2, 3, 4, 5
print(set1 | set2)
# intersection => 3
print(set1 & set2)
# different => 1, 2, 4, 5
print(set1 - set2)

