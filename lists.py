li=[]   #empty list
l1=[1,2,3,5,4]
l2=["chandu",1,True,None,"fill"]
l3=["lion","tiger","cheetha"]
l4=[6,19,23,8,5]

print(l2[3])

nested=[[4,3],[5,8]]
print(nested[1])
print(nested[0][1])

print(l1[2])
print(l1[-2])
print(l1[1:3])
print(l1[4:0:-1])

l1[1]="two"
print(l1)
l1.append(7) #to append 5 at last
print(l1)
l1.insert(1,1.5) #to insert 1.5 at index 1
print(l1)

l1.pop() #last element removd
print(l1)
l1.pop(2) #2 index element removed
print(l1)
l1.remove(1.5) #removing value 
print(l1)
del l1[0] #deleting value at index 0
print(l1)
l1.clear() #removes all values in list (or) making empty list
print(l1)

print(l3+l2) # to concatinate two lists
print(l2*3)  # to rpeate values
print("fill" in l2) # membership. if the value in the list then result is True
print(len(l2)) # to find length of list
print(min(l4)) #to find min value in list
print(max(l4)) # to find maximum value in list
print(sum(l4)) # to find sum of list 

for i in l4:   # to access items one by one
    print(i)

for i,item in enumerate(l4): # to iterate loop along with index i and value item in the list l4
    print(i,item)

squares=[m**2 for m in l4] # comprehension // it iterates the list and squares the each value
print(squares)

even=[m for m in l4 if m%2==0] # comprehension with condition // to add even values into list even with condition
print(even)

# list methods
'''
my_list.append(x)
my_list.extend([x, y])
my_list.insert(i, x)
my_list.remove(x)
my_list.pop(i)
my_list.index(x)
my_list.count(x)
my_list.sort()
my_list.reverse()
my_list.copy()
my_list.clear()   '''

l5=[3,5,1,8,6,9]
l5.sort()   # to sort the list
print(l5)

l6=[3,5,1,8,6,9]
l6_1=sorted(l6)  # the original list remain unchanged that sorted values only stored in another variable
print(l6,l6_1)

l6="chandu"
l6_1=sorted(l6) # it sorts the string and return as a list of each character
print(l6_1)

l7=["chandu","Suchendra","rayudu"]
l7.sort(key=str.lower) # to sot the strings by using key either str.lower or str.upper
print(l7)

matrix1 = [[3,6],[5,2]]  # multi-dimensional lists
print(matrix1[1][0])

matrix=[["chandu" for _ in range(2)] for _ in range(3)] # 2D comprehension // it gives the list with two strings of chandu and creates three lists inside the outer list
print(matrix)

copy1=l7          # copying lists
print(copy1)
copy1=l7[:]
print(copy1)
copy2=l7.copy()
print(copy2)
copy2=list("chandu")
print(copy2)

import copy
deep_copy=copy.deepcopy(l7)
print(deep_copy)

flat=[item for sublist in matrix1 for item in sublist] # to make multidimentional list into one list using comprehension
print(flat)
    # (or)
flat1=[]    
for sublist in matrix1:
    for item in sublist:
        flat1.append(item)
print(flat1)

transposed=list(zip(*matrix1)) # transposed from columns to rows
print(transposed)
transposed=[list(row) for row in zip(*matrix1)] # to convert list of tuples into list of lists
print(transposed)

l9=[3,5,11,15,23]
filtered=list(filter(lambda y:y>10, l9)) # filter(function, iterable) // to filter the values based on condition
print(filtered)

l9=[3,5,11,15,23]
filtered=list(map(lambda x:x+2, l9)) # map // to perform operation on each element
print(filtered)





