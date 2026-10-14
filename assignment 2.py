students = [
    {
        "name" : "Aarav",
        "age" : 21,
        "courses" : ("python", "SQL"),
        "skills" : {"python", "SQL", "Excel"}
    },
    {
        "name" : "Mehta",
        "age" : 20,
        "courses" : ("HTML","Python"),
        "skills" : {"HTML", "CSS", "Python"}
    },
    {
        "name" : "Rohit",
        "age" : 22,
        "courses" : ("Java","cloud computing"),
        "skills" : {"Java", "AWS"}
    },
    {
        "name" : "sanya",
        "age" : 21,
        "courses" : ("Machine learning", "Python"),
        "skills" : {"Python", "Math", "stats"}
    },
    {
        "name" : "Karan",
        "age" : 18,
        "courses" : ("C++","Data structure"),
        "skills" : {"C++", "Algorithms"}
    }
]

students.append({
    "name" : "Ananya",
    "age" : 20,
    "courses" : ("web dev", "UI/UX"),
    "skills" : {"Figma", "CSS"}
})

students[2].update({"age" : 20})

for student in students:
    if "Python" in student ["courses"]:
        print(student)
        
unique_skills = set()
for student in students:
    unique_skills.update(student["skills"])
    
oldest = students[0]
for student in students:
    if student["age"] > oldest["age"]:
        oldest = student
        
print(oldest["name"])
print(oldest["age"])

print("\n===== Student Dashboard =====")
print(f"Total Students: {len(students)}")

print("\nStudents Enrolled in Python:")
for student in students:
    if "Python" in student["courses"]:
        print(f"- {student}")

print("\nUnique Skills Across All Students:")
print(unique_skills)

print("\nOldest Student:")
print(f"Name: {oldest['name']}")
print(f"Age: {{oldest['age']}}")     
    