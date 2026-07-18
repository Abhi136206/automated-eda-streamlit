#FILE I/O 
#Python can be used to perform operations on file .
#types of all files
#1.Text files : .txt, .docx, .log etc.
#2. Binary files : .mp4, .mov, .png, .jpeg etc.

#OPEN, READ & CLOSE FILE
# f = open("file_name", "mode")
#data = f.read()
#f.close()

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)
f.close()

#Writing to a file
#f = open("demo.txt", "w")
#f.write("new line")

#adds to the file
#f = open("demo.txt", "a")
#f.write("new line")

f = open("demo.txt", "a")
f.write("I want to learn javascript tommorow. 123")
f.write("\n after that nodejs")

f.close()

f = open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close()

#WITH SYNTAX
# with open("demo.txt", "a")as f:
# data = f.read()
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    
with open("demo.txt", "w") as f:
    f.write("new data")
    
    
#DELETING FILE
import os

os.reason("sample.txt")

#CREATE A NEW FILE "PRACTICE.TXT" USING PYTHON.
with open("pratice.txt", "w") as f:
    f.write("Hi everyone \n we are learning file I/O\n")
    f.write("using java.\nI like programing in java.")
    
#WAF THAT REPLACE ALL OCCURRENCES OF "JAVA" WITH "PYTHON" IN ABOVE FILE
with open("pratice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
    
#WAF to find a word "learning" in practice.txt
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word)  != -1):
        print("found")
    else:
        print("no found")