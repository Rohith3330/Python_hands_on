import random
class StudentRecordSystem:
    def __init__(self):
        self.students = {}

    def generate_unique_id(self):
        # Generate a random ID and check if it already exists
        while True:
            student_id = random.randint(1, 10000)  
            if student_id not in self.students:
                return student_id


    def add_student(self, name, age, grade):
        student_id = self.generate_unique_id()
        self.students[student_id] = {'name': name, 'age': age, 'grade': grade}
        return student_id

    def update_student(self, student_id, new_info):
        if student_id in self.students:
            self.students[student_id].update(new_info)
            return True
        else:
            return False  # Student ID not found

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        else:
            return False  # Student ID not found

    def get_student_details(self, student_id):
        return self.students.get(student_id)

    def get_students_by_grade(self, grade):
        return [(student_id,student_info) for student_id, student_info in self.students.items() if student_info['grade'] == grade]

    def get_all_students(self):
        return self.students.values()


system = StudentRecordSystem()

# Adding students
student1_id = system.add_student("Alice", 15, 10)
student2_id = system.add_student("Bob", 14, 9)

# Updating student information
system.update_student(student1_id, {'name': 'Alice Smith', 'age': 16})

# Retrieving student details
print(system.get_student_details(student1_id))

# Retrieving students by grade
print(system.get_students_by_grade(10))

# Retrieving all students
print(system.get_all_students())

# Removing a student
system.remove_student(student2_id)

# Retrieving student details
print(system.get_student_details(student1_id))

# Retrieving students by grade
print(system.get_students_by_grade(10))

# Retrieving all students
print(system.get_all_students())
