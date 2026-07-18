name = input("name : ")
age = int(input("age : "))
price = float(input("price : "))

print("My name is ",name, "and I am ",age, "years old")

#TRAFFIC LIGHTS CODE
light = input("light color : ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

    
#GRADES OF STUDENTS
marks = int(input("marks : "))

if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")
      
      
#PRINT OUTPUT PRACTICE:
A = int(input("A : "))
G = input("M/F :")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")
    
#SINGLE LINE/TERNARY OPERATOR
food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

food = input("food : ")
print("sweet")if food == "cake" or food == "jalebi"else print("not sweet")

#CLEVER IF
age = int(input("age : "))
vote = ("yes", "no") [age < 18]

sal = float(input("salary : "))
tax = sal*(0.1, 0.2) [sal<=50000]
print(tax)

#ASSIGNMENT OPERATORS
num = 10
num += 10
print("num : ", num)