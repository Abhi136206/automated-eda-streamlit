name = input("enter your name : ")
print("my name is ", name)

val = input("enter some values : ")
print(type(val), val)

name = input("enter name : ")
age = input("enter age : ")
marks = input("enter marks : ")

print("welcome", name)
print("age : ", age)
print("marks : ", marks)

#Write a program to input 2 numbers & print their sum.

first = int(input("enter first number : "))
second = int(input("enter second number : "))

print("sum = ", first + second)

#WAP to input side of a square

side = float(input("enter square side : "))

print("area = ", side * side)

#WAP to input 2floating point numbers & print their average.
a = float(input("enter first : "))
b = float(input("enter second : "))

print("avg =", (a+b)/2)

#WAP to 2int num. a and b, print true if a is greater than or equal to b. if not print false.

a = int(input("enter first : "))
b = int(input("enter second : "))

print(a >= b)

#STRINGS
str1 = "apna"
len1 = len(str1)
print(len1)


str2 = "college"
len2 = len(str2)
print(len2)

final_str = str1 +" " + str2
print(len(final_str))

#SLICING
str = "apna college"
print(str[1 : 4])
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

str = "I am studying python from apnacollege"
print(str.replace("python", "javascript"))

#WAP to input user's first name & print its length.

str = "Abhinadan"
print(str[0:9])
print(len(str))

#WAP to find occurrence of '$' in a string.

str = "Hi, $ I am the $ symbol $ 99.99"
print(str.count("$"))

num = int(input("enter number : "))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")
    
#WAP to find the greatest of 3 number entered by the user
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
d = int(input("enter fourth number : "))


if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest", c)

else:
    print("fourth is largest", d)
    
#LIST TOUPLES
marks = [94.6, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[1])
print(marks[0])

student = ["karan", 95.4, 17, "Delhi"]
print(student[0])
student[0] = "arjun"
print(student)

list = [2, 1, 3]
list.append(4)
print(list)
print(list.sort())
print(list)

list = [2, 1, 3]
list.insert(3 , 5)
print(list)

#TUPLES
#A built in data type that lets us create immutable sequences of values.
tup = (1, 2, 3)
print(type(tup))

#WAP to enter 3 movies in list
movies = []
mov1 = input("enter 1st movie:")
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3rd movies:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

list1 = [1, 2, 3]
list2 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")
    
    
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))
