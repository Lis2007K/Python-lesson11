file_path = "C:/Users/Student/Desktop/Python-lesson11/Python-lesson11/leximi.txt"

# file = open(file_path,"r")

# content = file.read()

# print(content)

with open(file_path, "r") as file:
    content = file.read()
    print(content)

with open(file_path, "r") as file:
    line1 = file.readline()
    print(line1)

with open(file_path, "w") as file:
    file.write("Hello World")

with open(file_path, "r") as file:
    file.seek(2)
    data = file.read()
    print(data)