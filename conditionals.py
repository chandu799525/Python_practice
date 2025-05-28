x=9
y=6

if x<y:
    print("the value of x is less than the value of y")
elif x>y:
    print("the value of x is greater than y")
else:
    print("the value of x and value of y are equal") 

value=x  if x>y else y  #Ternary Operator (One-liner if-else)
print(value)

if x>y and x!=9:
    print("value of x less than y and not equal to 9")
if x>y or x!=9:
    print("one condition is true")
if not x<9:
    print("x not less than 9")

#None
name=None
if name:
    print("name provided")
else:
    print("name not provided")

#bool
name=False
if name:
    print("name provided")
else:
    print("name not provided")

#empty
name=""
if name:
    print("name provided")
else:
    print("name not provided")

# any empty data
name=[]
if name:
    print("name provided")
else:
    print("name not provided")


#Nested conditions
if x>0:
    if x<10:
        print("less than 10")
    else:
        print("greater than 9")


# match
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
   