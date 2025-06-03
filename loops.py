'''for i in range(10): # breaks the loop with condition
    print(i)
    if i==5:
        break

i=0
while i<5:   # continue the loop(skipping that iteration from that condition)
    i+=1
    if i==2:
        continue
    print(i)

for i in range(5):  # else part runs if no break applies
    print(i)
    if i==3:
        break
else:
    print("execution completed")

i=0
while i<5:   # else part runs if no break applies
    i+=1
    if i==2:
        continue
    print(i)
else:
    print("process completed")

for i in [2,4,6,8]: # loop for printing list items
    print(i)

lists=[2,4,6,8]
i=0
while i <len(lists):
    print(lists[i])
    i+=1

for i in "chandu": # loop for printing string characters
    print(i)

s="chandu"
i=0
while i<len(s):
    print(s[i])
    i+=1

for i in (1,2,3): # loop for printing tuple items
    print(i)

t=(3,2,4,7)
i=0
while i<len(t):
    print(t[i])
    i+=1          

for i in {1,3,5,7}: # loop for printing set items
    print(i)

s={1,3,5,7}
s_loop=iter(s) # it creates iterator for the set
while True:
    try:
        print(next(s_loop)) # to get elements one by one
    except StopIteration:
        break        

d={"chandu":23,"jagadesh":22} # loop for printing dictionaries keys and values
for i in d:
    print(i,d[i]) 

d={"chandu":23,"jagadesh":22,"rayudu":23}
keys=list(d.keys())
i=0
while i<len(keys):
    k=keys[i]
    print(k,d[k])
    i+=1

for key,value in d.items(): # loop for printing dictionaries keys and values
    print(key, value)

d={"chandu":23,"jagadesh":22,"rayudu":23}
items=list(d.items())
i=0
while i<len(items):
    key,value=items[i]
    print(key,value)
    i+=1  '''

li=[2,3,4,1,5]
for i,value in enumerate(li):
    print(i,value)

m=["chandu","suchendra"]
n=[23,30]
for mn, nm in zip(m,n):
    print(mn,nm)







