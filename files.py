f=open("fly.txt","r")       # file read
   # (or)
with open("fly.txt","r") as f:
    file_content=f.read()
    line=f.readline()
    line1=f.readlines()
    print(file_content)

f=open("fly.txt","w")     # file write
f.write("my name is chandu\n")
f.writelines(["clear output\n","from this file\n"])
f.close()

f=open("fly.txt","a")    # appending
f.write("from teeparru")
f.close()

f=open("fixed.txt","x") # to create a file


f=open("fly.txt","r+")  #reading and writing mode // updating mode
f.seek(0) # pointer from begining
print(f.read())
f.seek(8,0)  # from 8 byte of beginning 
print(f.read())
f.write("\nnew line formed")
f.close()

f=open("fly.png","rb")  # reading binary // file should be in object form
r=f.read()
print(r)
f.close()

f=open("fly.png","wb") # writing binary // file should be in object form
f.write(r)
f.close()

import os     # checking file exists
if os.path.exists("fly.txt"):
    print("exists")

os.remove("fly.txt")  # to delete file

import os    # renaming or moving files
os.rename("flyingwithjoy.txt","flying.txt",)




