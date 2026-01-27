# Student Activity Manager

# String
project_title = "Student Activity Manager"
college_name = "Digital Learning Campus"

# List
students = ["Amit", "Neha", "Ravi"]
activities = ["Coding", "Design", "Testing"]

# String operations
title_upper = project_title.upper()
short_name = college_name.replace("Campus", "Cmp.")

# List operations
students.append("Kiran")
students.extend(["Pooja", "Arjun"])
students_copy = students.copy()
student_slice = students[1:4]

activities.append("Documentation")
activities.extend(["Debugging", "Presentation"])
activity_slice = activities[0:3]

# Output
print("------ PROJECT REPORT ------")
print("Project Title:", title_upper)
print("Institute:", short_name)
print("Student List:", students)
print("Copied List:", students_copy)
print("Sliced Students:", student_slice)
print("Activities:", activities)
print("Sliced Activities:", activity_slice)
print("Total Students:", len(students))
print("Total Activities:", len(activities))
print("System Status: Data Processed Successfully")