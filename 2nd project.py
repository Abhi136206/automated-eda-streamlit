#number = range(5)
#print(number)

i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

# FOR LOOP CODE
for item in range(5):
    print(item + 1)
    
#LIST
marks = [95, 98, 97]
print(marks [1:3])

#for loop in list
marks = [95, 98, 97]

for score in marks:
    print(score)
    
#APPEND
marks = [95, 98, 97]
marks.append(99)
print(marks)


marks = [95, 98, 97]
marks.insert(0, 99)
print(92 in marks)

#BREAK AND CONTINUE
students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
    if student == "radha":
        break
    print(student)
    
students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
    if student == "kishan":
        continue
    print(student)
    
#TUPPLE
marks = (95, 98, 97, 97, 97)

print(marks.index(97))

#DICTIONARY

marks = {"English" : 95, "chemistry" : 98}

print(marks["chemistry"])
marks["physics"] = 97
print(marks)

#FUNCTION
import math
print(dir(math))

from math import sqrt
print(sqrt(1))

def print_sum(first, second):
    print(first + second)
    
print_sum(1, 2)

name = "shradha"
age = 23
price = 25.99

print(type(name))
print(type(age))
print(type(price))
      

A,B = 2,3
C = 4
print(A+B*C)

A,B = 10,5.0
C = A*B
print(C)

A,B = 12,5
C = A//B
print(C)
