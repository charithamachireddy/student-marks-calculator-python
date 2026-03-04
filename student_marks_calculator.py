print("Student Marks Calculator")

# Taking input for 5 subjects
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
mark4 = float(input("Enter marks for subject 4: "))
mark5 = float(input("Enter marks for subject 5: "))

# Calculate total marks
total = mark1 + mark2 + mark3 + mark4 + mark5

# Calculate percentage
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

# Calculate grade
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")