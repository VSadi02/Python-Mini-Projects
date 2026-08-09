students = []
print("Aditi Vadd\nRoll No:14")
n = int(input("Enter number of students: "))

# Taking input
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Marks": marks
    }

    students.append(student)

# Displaying records
print("\n--- Student Records ---")

for i, student in enumerate(students, start=1):
    print("\nStudent", i)
    print("Name:", student["Name"])
    print("Roll No:", student["Roll No"])
    print("Marks:", student["Marks"])