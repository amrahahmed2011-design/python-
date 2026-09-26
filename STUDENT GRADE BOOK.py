grade = {}
for i in range(5):
    name = input("Enter the name of student:  ")
    score = int(input("Enter the score of student:  "))
    grade[name] = score
print("STUDENT GRADE :", grade)
average = sum(grade.values()) / 5
print("Average score of the class is: ", average)
topper = max(grade.values())
print("Topper of the class is: ", topper)
bottom = min(grade.values())
print("Bottom of the class is: ", bottom)
name = input("Enter the name of student to check the score:  ")
print("GRADE OF", name, "is: ", grade.get(name, "Student not found"))
                 