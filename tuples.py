t=()
tuples=(1,2,3,4,5,3)
t1=1,2,3  # Tuple without parentheses (implicit)
t2=(1,) #for single element

print(tuples,t1,t2)

print(tuples[2])
print(tuples[1:4])

for i in tuples:
    print(i)

for i,item in enumerate(tuples):
    print(i,item)  

t3=t1+t2
t4=t2*3
t5=tuples.index(5)  # it returns the index of first occurence of index of value 5
x=tuples.count(3)   # it returns the count of values 3 how many times that appears
print(t3,t4,1 in t2,len(t4),t5,x)

details=("chandu",25,"Teeparru") #packing the values using tuple
name,age,village=details  # unpacking the values from tuple // assigning the values to each variable
print(name,age,village)

name,age=age,village  # swapping variables
print(name,age)

nested=((2,"chandu"),(3,"suchendra"),(4,"rayudu"))  # nested tuples
print(nested[1][1])

dictionary={("chandu",25):"person A details",("suchendra",23):"person B details"} # using tuples as dictionary keys
print(dictionary[("chandu",25)])

t=tuple([1,2,3]) #converting list to tuple and vice versa
l=list((4,5,6))
