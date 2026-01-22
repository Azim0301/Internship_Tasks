student1 = {"Math", "Python", "DBMS", "OS"}
student2 = {"Python", "Java", "OS", "CN"}

common_subjects = student1 & student2
only_student1 = student1 - student2
only_student2 = student2 - student1

print("Common Subjects:", common_subjects)
print("Only Student 1 Subjects:", only_student1)
print("Only Student 2 Subjects:", only_student2)
