with open("test.txt" , "w") as f: # w-write file and \n=break the line
    f.write("My Name is Sweetsan \n")

with open("test.txt" , "a") as f: # a-append file 
    f.write("My age is 20 years old \n")
    f.write("My hobby is reading a book \n")
    f.write("My favourite color is blue")

with open("test.txt", "r") as f: # r-readonly file
    content=f.read()
    print(content)

