d={}
d={"name":"chandu","age":25,}
d=dict(name="suchendra",age=23)
d=dict([("name","rayudu"),("age",25)])

print(d["name"])
print(d.get("name"))
print(d.get("job","not in the dictionary"))# if job key not presents then comment

d["name"]="raju" # update
d["city"]="vizag" # adding new key

del d["age"] # deleting key
d.pop("name") # remove keys and return values
d.clear()   # empty dictionary

"name" in d # checking key in dict

for key in d:
    print(key,d[key])

for key, value in d.items():
    print(key,value)

for value in d.values():
    print(value)

for key in d.keys():
    print(key)
    
                
