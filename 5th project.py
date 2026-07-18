#DICTIONARY AND SETS
dict = {
    "name" : "Abhinadan",
    "subjects" : ["python", "c", "Java"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
    
}

dict["name"] = "Abhinadan"
dict["surname"] = "sharma"

print(dict)

#NESTED DICTIONARY
student = {
    "name" : "Abhinadan sharma",
    "subjects" : {
        "phy" : 97,
        "chem" : 98, 
        "math" : 95
    }
}
print(student["subjects"]["chem"])

student = {
    "name" : "Abhinadan sharma",
    "subjects" : {
        "phy" : 97,
        "chem" : 98, 
        "math" : 95
    }
}

print(list(student.items()))


#SETS
collection = {1, 2, 3}
print(collection)
print(type(collection))
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

collection.clear()

print(len(collection))

#SETS
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))

#STORE FOLLOWING WORD MEANINGS IN A PYTHON DICTIONARY:
dict = {
    "cat" : "a small animal", 
    "table" : ("a piece of furniture", "List of facts & figures")
    
}
print(dict)

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)

#Figure out a way to store 9 & 9.0 as seperate values in the set.
values = {9, 9.0}
values = {9, "9.0"}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
    
}
print(values)