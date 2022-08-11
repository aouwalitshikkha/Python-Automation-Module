x = {'a','b','c'}
y = {'d','e','f'}
p = {'a','b'}
# Disjoint Set

# z = x.isdisjoint(y)
# z = p.issubset(x)
z = x.issuperset(p)
print(z)