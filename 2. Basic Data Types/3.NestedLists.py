# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    students = []  # Initialize the list outside the loop to store all students' data
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])  # Append each student's data as a sublist to the students list
    
    students.sort(key=lambda x: x[1])
    
    secondLowestGrade = None
    
    for i in range(1, len(students)):
        if students[i][1] > students[0][1]:
            secondLowestGrade = students[i][1]
            break
    
    names_of_secondLowestGrade = [student[0] for student in students if student[1] == secondLowestGrade ]
    
    names_of_secondLowestGrade.sort()
    for name in names_of_secondLowestGrade:
        print(name)
