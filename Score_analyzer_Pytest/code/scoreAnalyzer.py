def input_student_data(num_students, num_subjects):
    student_list = []
    for i in range(num_students):

        name = input(f"Enter name of student {i+1}: ")
        marks = []
        for j in range(num_subjects):

            mark = float(input(f"Enter marks of {name} in subject {j+1}: "))
            marks.append(mark)

        student_list.append({'name': name, 'marks': marks})
    return student_list

def calculate_student_averages(students):
    averages = {}
    for student in students:
        name = student['name']
        marks = student['marks']
        average = sum(marks) / len(marks)

        averages[name] = average
    return averages

def find_highest_average(averages):
    highest_avg_student = max(averages, key=averages.get)
    
    highest_avg = averages[highest_avg_student]

    return highest_avg_student, highest_avg
def find_highest_subject_marks(students):
    highest_marks = []
    num_subjects = len(students[0]['marks'])
    
    for i in range(num_subjects):
        highest_mark = float('-inf')
        highest_scorers = []
        
        for student in students:
            mark = student['marks'][i]
            
            if mark > highest_mark:
                highest_mark = mark
                highest_scorers = [student['name']]
            elif mark == highest_mark:
                highest_scorers.append(student['name'])
        
        highest_marks.append(highest_scorers)
    
    return highest_marks

def main():
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    student_data = input_student_data(num_students, num_subjects)

    student_averages = calculate_student_averages(student_data)
    highest_avg_student, highest_avg = find_highest_average(student_averages)
    highest_scorers = find_highest_subject_marks(student_data)

    print("\nAverage of every student:")
    for student, average in student_averages.items():
        print(f"{student}: {average}")

    print(f"\nStudent with the highest average: {highest_avg_student} with average {highest_avg}")
    print("Names of students with highest marks in each subject:")
    for i, highest_scorer in enumerate(highest_scorers):
        print(f"Subject {i+1}: {', '.join(highest_scorer)}")

if __name__ == "__main__":
    main()
