with open("test.txt" , "w") as f:
    f.write("My Name is Sweetsan \n")

with open("test.txt" , "a") as f:
    f.write("My age is 20 years old")

with open("test.txt", "r") as f:
    content=f.read()
    print(content)

