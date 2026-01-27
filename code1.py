# Student Resource Management System

# String
college = "Tech Valley Institute"

# List
courses = ["Python", "Data Science", "AI"]

# Tuple
departments = ("CSE", "IT", "ECE")

# Set
roll_numbers = {101, 102, 103, 103, 104}

# Dictionary
student = {
    "name": "Rahul",
    "age": 19,
    "course": "Python"
}

# List operations
courses.append("Cyber Security")
courses.extend(["Cloud", "Blockchain"])
course_copy = courses.copy()
course_slice = courses[0:3]

# Set operation
roll_numbers.add(105)

# String operations
college_upper = college.upper()
college_short = college.replace("Institute", "Inst.")

# Dictionary operations
student["year"] = "First Year"
student["status"] = "Active"

# Tuple operation
all_departments = departments + ("ME",)

# Output
print("------ STUDENT SYSTEM REPORT ------")
print("College:", college_upper)
print("Short Name:", college_short)
print("Courses:", courses)
print("Course Copy:", course_copy)
print("Course Slice:", course_slice)
print("Departments:", all_departments)
print("Roll Numbers:", roll_numbers)
print("Student Info:", student)
print("Student Name:", student["name"])
print("System Status: Data Structure Loaded Successfully")
