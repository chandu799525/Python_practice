s={} # ! it creates dictionary not a set

s=set() # creates empty set
s={1,2,3,4,5}
s=set([3,3,4,1,4,5]) # removes duplicates
s.add(7) # adding value 7 to the set s
  # (or)
s.update([8,9]) # adding multiple values
print(s)

s.remove(2)      # Raises error if not found
s.discard(10)    # Safe: no error if not found
s.pop()          # Removes random element
s.clear()        # Removes all elements

a = {1, 2, 3}
b = {3, 4, 5}
a | b     # Union → {1, 2, 3, 4, 5}
a & b     # Intersection → {3}
a - b     # Difference → {1, 2}
a ^ b     # Symmetric difference → {1, 2, 4, 5}

a == b        # Equal sets
a != b        # Not equal
a <= b        # Subset
a >= b        # Superset
a.isdisjoint(b)  # True if no common elements

for item in a:
    print(item)

square={x+2 for x in range(5)} # set comprehension

s1=set([3,1,2,5])   # list to set
l1=list({1,2,3,4,5})  # set to list

f = frozenset([1, 2, 3])
# f.add(4)  Error: frozen sets are immutable

'''s.add(x)
s.update([x, y])
s.remove(x)
s.discard(x)
s.pop()
s.clear()

s.union(t)
s.intersection(t)
s.difference(t)
s.symmetric_difference(t)

s.issubset(t)
s.issuperset(t)
s.isdisjoint(t)'''

